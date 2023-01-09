from odoo import api, fields, models, _


class Student(models.Model):
    _name = 'school.section'
    _description = 'section'
    name = fields.Char('Section_name', required=True)
    email = fields.Char('code')
