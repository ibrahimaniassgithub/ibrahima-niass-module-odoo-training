from odoo import models, fields, api
from datetime import date


class student(models.Model):
    _inherit = 'res.partner'
    age = fields.Integer(string="Age")
    birth_date = fields.Date(string="Date de naissance")
    majeur = fields.Boolean(string="Majeur",default=True)
    sexe = fields.Selection([('H','Homme'),('F','Femme')], 'sexe', default='H')
    teacher_ids = fields.Many2many(comodel_name='res.partner', relation='student_teacher_rel', column1='etudiant_ids', column2='teacher_ids')

    _sql_constraints = [
        ('_majeur_true',
         'check(majeur)', "L'etudiant doit étre majeur ...!")]

    @api.onchange('birth_date')
    def calcul_age(self):
        if self.birth_date and type(self.birth_date)!='bool':
             _logger.error(type(self.birth_date))
             today = date.today()
             self.age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

class teacher(models.Model):
    _inherit = 'res.partner'
    grade =fields.Char(string='Grade')
    etudiant_ids =fields.Many2many(comodel_name='res.partner',relation='teacher_student_rel',column1='etudiant_ids',column2='teacher_ids')

class types(models.Model):
    _inherit = 'res.partner'
    types = fields.Selection([('et', 'ETUDIANT'), ('en', 'ENSEIGNANT')],'Types' , default='et', required=True)