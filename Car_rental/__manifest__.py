# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Car Rental",
    'version':"15.0.1.0",
    'summary': "Task Generation from Sales Orders",
    'description': """
Allows to create task from your sales order
=============================================
This module allows to generate a project/task from sales orders.
""",
    #'category': 'car',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/car_data.xml',
        
    ],
    'auto_install': True,
    'installable':True
    #'license': 'LGPL-3',
}
