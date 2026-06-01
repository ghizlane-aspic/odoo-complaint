from odoo import http
from odoo.http import request


class ReclamationClientController(http.Controller):
    @http.route(
        [
            '/odoo/reclamation-client',
            '/odoo/reclamations',
            '/reclamation-client',
            '/reclamations',
        ],
        type='http',
        auth='user',
    )
    def reclamation_client_redirect(self, **kw):
        return request.redirect('/web#action=reclamation_client.reclamation_action_all')
