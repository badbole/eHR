# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    jmbg = fields.Char(string="JMBG")

    _sql_constraints = [
        ('name_uniq', 'unique(jmbg)', 'Not valid, please try again' )
         ]


