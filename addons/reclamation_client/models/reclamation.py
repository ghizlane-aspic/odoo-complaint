from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ReclamationClient(models.Model):
    _name = "reclamation.client"
    _description = "Customer Complaint"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "date_open desc, id desc"

    name = fields.Char(
        string="Reference",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _("New"),
        tracking=True,
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Customer",
        required=True,
        tracking=True,
    )
    date_open = fields.Date(
        string="Opening Date",
        default=fields.Date.context_today,
        tracking=True,
    )
    date_close = fields.Date(
        string="Closing Date",
        readonly=True,
        copy=False,
        tracking=True,
    )
    description = fields.Text(
        string="Description",
    )
    priority = fields.Selection(
        selection=[
            ("low", "Low"),
            ("medium", "Medium"),
            ("high", "High"),
        ],
        string="Priority",
        default="medium",
        required=True,
        tracking=True,
    )
    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Assigned To",
        default=lambda self: self.env.user,
        tracking=True,
    )
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("in_progress", "In Progress"),
            ("resolved", "Resolved"),
            ("closed", "Closed"),
        ],
        string="Status",
        default="new",
        required=True,
        tracking=True,
    )
    delay_days = fields.Integer(
        string="Resolution Delay (days)",
        compute="_compute_delay_days",
        store=True,
        help="Number of days between the opening date and the closing date.",
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.company,
    )

    @api.depends("date_open", "date_close")
    def _compute_delay_days(self):
        for record in self:
            if record.date_open and record.date_close:
                record.delay_days = (record.date_close - record.date_open).days
            else:
                record.delay_days = 0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get("name") or vals.get("name") == _("New"):
                vals["name"] = self.env["ir.sequence"].next_by_code(
                    "reclamation.client"
                ) or _("New")
        return super().create(vals_list)

    def action_start(self):
        for record in self:
            if record.state != "new":
                raise UserError(_("Only new complaints can be started."))
            record.state = "in_progress"

    def action_resolve(self):
        for record in self:
            if record.state != "in_progress":
                raise UserError(
                    _("Only complaints in progress can be marked as resolved.")
                )
            record.state = "resolved"

    def action_close(self):
        for record in self:
            if record.state not in ("resolved", "in_progress"):
                raise UserError(
                    _("Only resolved or in-progress complaints can be closed.")
                )
            record.write({
                "state": "closed",
                "date_close": fields.Date.context_today(record),
            })

    def action_reset(self):
        for record in self:
            record.write({
                "state": "new",
                "date_close": False,
            })
