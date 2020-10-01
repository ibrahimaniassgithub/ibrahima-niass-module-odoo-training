# -*- coding: utf-8 -*-

from odoo.tests import common
from symbol import try_stmt

class TestRes_partner(common.TransactionCase):
    def setUp(self):
        super(TestModule, self).setUp()
        
        self.partner_student=self.env['res.partner'].create({
            'name' : 'Ibrahima Niass',
            'age' : '27',
            'birth_date' : '01/10/2020',
            'majeur' : True,
            'sexe' : 'Homme'  })
        
        self.session=self.env['myacademy.session'].create({
            'name' : 'Session 1',
            'start_date' :'01/10/2020',
            'end_date' :'01/10/2021',
            'duration' :'365',
            'seats' : '10'})
        
        self.courses=self.env['myacademy.course'].create({
            'name' : 'Cours 1',
            'description' :'mon cours numero 1',
            'duration' : '10'})

    def test_class(self):

        self.assertEqual(self.partner_student.name,'Ibrahima Niass');
        self.assertEqual(self.partner_student.age,'27');
        self.assertTrue(self.partner_student.majeur);

        self.assertEqual(self.session.name,'Session 1');
        self.assertEqual(self.session.duration,'365');
        

        self.assertEqual(self.courses.name,'Cours 1');
        self.assertEqual(self.courses.description,'mon cours numero 1');
        self.assertEqual(self.courses.duration,'10');
        