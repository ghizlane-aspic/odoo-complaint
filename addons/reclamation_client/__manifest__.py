{
    "name": "Customer Complaint Management",
    "version": "19.0.1.0.0",
    "category": "Customer Service",
    "summary": "Create, assign, track and close customer complaints with a full workflow and PDF report.",
    "description": """
Customer Complaint Management
=============================
Manage the full lifecycle of customer complaints:

* Register complaints with auto-generated references (REC/YYYY/NNN)
* Assign complaints to responsible users
* Track progress through a clear workflow (New, In Progress, Resolved, Closed)
* Prioritize complaints (Low, Medium, High)
* Built-in chatter (messages, activities, tracking)
* Printable QWeb PDF report
""",
    "author": "Reclamation Client",
    "website": "https://www.example.com",
    "depends": ["base", "mail", "contacts"],
    "data": [
        "security/reclamation_security.xml",
        "security/ir.model.access.csv",
        "data/reclamation_data.xml",
        "report/reclamation_report.xml",
        "report/reclamation_report_action.xml",
        "views/reclamation_views.xml",
        "views/menu.xml",
    ],
    "images": ["static/description/icon.png"],
    "price": 18.0,
    "currency": "EUR",
    "license": "OPL-1",
    "application": True,
    "installable": True,
}
