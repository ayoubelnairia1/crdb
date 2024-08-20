# -*- coding: utf-8 -*-
# from odoo import http


# class AgHrEmployee(http.Controller):
#     @http.route('/ag_hr_employee/ag_hr_employee', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ag_hr_employee/ag_hr_employee/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ag_hr_employee.listing', {
#             'root': '/ag_hr_employee/ag_hr_employee',
#             'objects': http.request.env['ag_hr_employee.ag_hr_employee'].search([]),
#         })

#     @http.route('/ag_hr_employee/ag_hr_employee/objects/<model("ag_hr_employee.ag_hr_employee"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ag_hr_employee.object', {
#             'object': obj
#         })
