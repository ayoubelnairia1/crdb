# -*- coding: utf-8 -*-

from odoo import models, fields


class HREmployee(models.Model):
    _inherit = 'hr.employee'

    family_paper_number = fields.Integer(string="Family Paper no.", help="Family paper number of employee")
    family_registration_number = fields.Integer(string="Family Registration No.", help="Family registration number of employee")
    mother_name = fields.Char(string="Mother Name", help="Mother name of employee")
    job_grade = fields.Integer(string="Job Grade", required=True, help="Job grade of employee")
    experience_years = fields.Integer(string="Experience Years", help="Experience years of employee")
    job_transfer_process = fields.Selection([('hiring', 'Hiring'), ('mandate', 'Mandate'), ('contract', 'Contract'),
                                             ('secondment', 'Secondment')], string="Job Transfer Process",
                                            default='hiring', help="Job transfer process of employee")
    employee_number = fields.Integer(string="Employee Number", required=True, help="Employee number of employee")
    financial_number = fields.Integer(string="Financial Number", required=True, help="Financial number of employee")
    functional_structure_number = fields.Integer(string="Functional Structure Number", required=True, help="Functional structure number of employee")
    social_security_number = fields.Integer(string="Social Security Number", required=True, help="Social security number of employee")
    insurance_number = fields.Char(string="Insurance Number", size=15, help="Insurance number of employee")
    certificate_info_ids = fields.One2many('hr.certificate.info', 'employee_id', string="Certificate Info")
    bank_name = fields.Char(string="Bank Name", help="Bank name of employee")
    bank_account_number = fields.Char(string="Bank Account Number", help="Bank account number of employee")
    rakam_watany = fields.Char(string="RAKAM_WATANY", size=12, help="National Unique Number (max 12 chars)")


class HRCertificateInfo(models.Model):
    _name = 'hr.certificate.info'
    _description = 'HR Certificate Info'

    name = fields.Char(string="Study", required=True, help="Name of certificate")
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True, help="Employee of certificate")
    certification_level = fields.Selection([('graduate', 'Graduate'), ('bachelor', 'Bachelor'), ('master', 'Master'),
                                    ('doctor', 'Doctor'), ('other', 'Other')], 'Certificate Level', default='other')
    organization = fields.Char(string="Organization", help="Organization of certificate")
    graduation_date = fields.Date(string="Graduation Date", help="Graduation date of certificate")


class HRContract(models.Model):
    _inherit = 'hr.contract'

    work_start_date = fields.Date(string="Work Start Date", help="Work start date of employee")
