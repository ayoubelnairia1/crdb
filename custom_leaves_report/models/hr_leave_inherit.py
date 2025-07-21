from odoo import models

class HrLeave(models.Model):
    _inherit = 'hr.leave'

    # Example helper: get employee's grade or any custom logic
    def get_employee_grade(self):
        return self.employee_id.grade_id.name if hasattr(self.employee_id, 'grade_id') else ''