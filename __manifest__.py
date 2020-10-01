# -*- coding: utf-8 -*-
{
    'name': "MY Academy",
    'summary': "Manage trainings",
    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
    """,
    'author': "Ibrahima NIASS",
    'category': 'Test_Technique',
    'version': '1.0',
    'depends': ['crm'],
    'installable': True,
    'application': True,
    'demo': [ ],
    'data': [
        'views/teacher.xml',
        'views/student.xml',
        'views/course.xml',
        'views/session.xml',
        'views/theme.xml',
        #'security/ir.model.access.csv',
        #'security/security.xml'
    ],
}
