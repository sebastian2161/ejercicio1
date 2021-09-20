# -*- coding: utf-8 -*-

{
    'name': 'viaje Espacial Odoo',
    'summary': """Organizacion de logistica Mision Espacial""",
    'description': """
        Organizacion de logistica Mision Espacial:
         -Nave Espacial
         -Tripulacion
     """,
    
    'author': 'seba01',
    'website': 'https://www.odoo.com/',
    'category': 'Espacial',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/nave_security.xml',
        'security/ir.model.access.csv',
        'views/nave_menuitems.xml',
        'views/nave_view.xml',
    ],
    'demo': [
        'demo/mision_espacial.xml',
    ],
    
    
}