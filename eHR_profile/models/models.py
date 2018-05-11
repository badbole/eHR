# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EmployeeProfile (models.Model):
    _name = 'employee.profile' #DB table employee_profile
    _rec_name = 'name'
    _description = 'Profile'
    #_inherit = 'hr.employee'

    marital = fields.Selection(string="Marital Status", selection=[('single', 'Single'),
                                                                   ('married', 'Married'),
                                                                   ('widower', 'Widower'),
                                                                   ('divorced', 'Divorced'),
                                                                   ],
                                                                    required=True,
                                                                    groups='hr.group_hr_user')
    Identification_id = fields.Char(string="Identification No",  groups='hr.group_hr_user', required=True, )
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'),
                                                          ('female', 'Female'),
                                                          ('other', 'Other'),
                                                          ], groups='hr.group_hr_user',required=True, )
    name = fields.Char(string="Name", required=True, )
    father_name = fields.Char(string="Father Name", required=True, )





