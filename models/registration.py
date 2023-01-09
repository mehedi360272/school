from odoo import api, fields, models, _


class Student(models.Model):
    _name = 'school.registration'
    _description = 'registration'
    section_id = fields.Many2one('Section','school.section')
    course_id = fields.Many2one('course','school.course')
    teacher_id = fields.Many2one('Teacher','school.teacher')
    student_ids = fields.Many2many('school.student','registration_student_rel','registration_id','student_id','Student List')
