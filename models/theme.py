from odoo import models, fields, api

class theme(models.Model):
    _name = 'myacademy.theme'
    _description = "MyAcademy Theme"

    name = fields.Char(string="Title", required=True)

