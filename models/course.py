from odoo import models, fields, api

class Course(models.Model):
    _name = 'myacademy.course'
    _description = "MyAcademy Courses"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    duration = fields.Float(digits=(6, 2), help="Duration in hours")
    theme=fields.Many2one("myacademy.theme", String="Theme")