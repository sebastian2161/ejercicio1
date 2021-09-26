# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    'summary': """Academy app to manage training""",
    'description': """
        Academy module to manage training:
         -courses
         -sessions
         -attendes
     """,
    
    'author': 'seba',
    'website': 'https://www.odoo.com/',
    'category': 'Training',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
    
}

# Manifiesto de hoy 20-09-2021
# Manifiesto de hoy 22-09-2021
# Manifiesto de hoy 23-09-2021
# Manifiesto de hoy 24-09-2021
# Manifiesto de hoy 25-09-2021