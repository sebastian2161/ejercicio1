# -*- coding: utf-8 -*-
{
    'name': 'Odoo 14 Development Tutorials',
    'version': '14.0.2.1.0',
    'summary': 'Odoo 14 Development Tutorials',
    'sequence': -100,
    'description': """Odoo 14 Development Tutorials""",
    'category': 'Tutorials',
    'author': 'Odoo Mates',
    'maintainer': 'Odoo Mates',
    'website': 'https://www.odoomates.tech',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'mail',
        'website_slides',
        'hr',
        'report_xlsx'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/slide_data_v12.xml',
        # 'data/slide_data_v12_2.xml',
        'data/slide_data_v13.xml',
        'data/slide_data_v14.xml',
        'wizard/create_appointment_view.xml',
        'wizard/search_appointment_view.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/appointment_view.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
        'views/sale.xml',
        'report/patient_details_template.xml',
        'report/patient_card.xml',
        'report/report.xml'
    ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}


#update #25-09-2021
#update #27-09-2021
#update #299-09-2021
#update #299-09-2021
#update #299-09-2021
#update #299-09-2021