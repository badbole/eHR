# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    jmbg = fields.Char(string="JMBG", size = 13, required = False)

    _sql_constraints = [
        ('name_uniq', 'unique(jmbg)', 'JMBG already entered, no duplicates allowed!')
    ]

    @api.constrains('jmbg')
    def _check_jmbg(self):
        multiply = [7,6,5,4,3,2,7,6,5,4,3,2]
        control_num = int(self.jmbg[12])
        sum = 0
        for i in range(12):
            sum += int(self.jmbg[i])*multiply[i]
        rest = sum % 11
        diff = 11 - rest

        jmbg_valid = True
        if rest == 1:
            jmbg_valid = False
        elif rest == 0 and control_num == 0:
            jmbg_valid  =  True
        elif 1 < rest < 11 and control_num == diff:
            jmbg_valid == True
        elif control_num != diff:
            jmbg_valid = False
        if not jmbg_valid:
            raise ValidationError('Incorrect JMBG!')
