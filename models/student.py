from  odoo import api, fields, models, _

class Student(models.Model):
    _name = 'school.student'
    _description = 'student'
    name = fields.Char('Student_name', required=True)
    email = fields.Char('Email')
    phone = fields.Char('phone')
    birth_date = fields.Char('Date of Birth')
    gender = fields.Selection([('M','Male'),('F','Female')],'Gender')
