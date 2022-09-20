# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'School Management',
    'version': "15.0.1.0",
    'summary': """
        with this module you can view your sales reports by regions(using customer states)""",

    'description': """This module aims to provide you best advantage of sale report by giving you detailed sales report by state, from which you can know which geographic area is the best to concentrate on.
              """,
    'author': "Smart Do.",
    'company': "Smart Do.",
    'category': 'School',
    'sequence': 15,
    
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/student_profile.xml',
    ],
    'website': "https://smartdo-tech.com/",
    'images': ['static/description/banner.png'],
    'support':"info@smartdo-tech.com",
    'license': 'OPL-1',
    'price': 15,
    'currency': 'USD',
    'auto_install': False,
    'installable': True,
}
