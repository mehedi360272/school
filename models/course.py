from odoo import api, fields, models, _


class Student(models.Model):
    _name = 'school.course'
    _description = 'course'
    name = fields.Char('course_name', required=True)
    email = fields.Char('code')

