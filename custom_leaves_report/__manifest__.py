{
    "name": "Leave Arabic Custom Reports",
    "version": "16.0.1.0.0",
    "depends": ["hr_holidays"],
    "category": "Human Resources",
    "author": "Afaqalghad",
    "summary": "Custom Arabic leave request reports for Odoo",
    "description": "Generates annual, emergency, and medical leave reports in Arabic with employee data.",
    "data": [
        "report/leave_annual_report_template.xml",
        "report/leave_annual_report_action.xml",
        "report/leave_emergency_report_template.xml",
        "report/leave_emergency_report_action.xml",
        "report/leave_medical_report_template.xml",
        "report/leave_medical_report_action.xml"
    ],
    "installable": True,
    "application": False,
}