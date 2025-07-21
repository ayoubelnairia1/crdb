from odoo import models, fields

class LeaveReportWizard(models.TransientModel):
    _name = 'leave.report.wizard'
    _description = 'Leave Report Wizard'

    date_from = fields.Date("Date From", required=True)
    date_to = fields.Date("Date To", required=True)
    employee_id = fields.Many2one("hr.employee", "Employee", required=False)

    def action_generate_report(self):
        domain = [
            ("request_date_from", ">=", self.date_from),
            ("request_date_to", "<=", self.date_to)
        ]
        if self.employee_id:
            domain.append(("employee_id", "=", self.employee_id.id))
        return {
            'type': 'ir.actions.act_window',
            'name': 'Leaves',
            'res_model': 'hr.leave',
            'view_mode': 'tree,form',
            'domain': domain,
        }