# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016 Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################
{
    'name': 'Auto Switch Company',
    'category': 'Technical Settings',
    'Summary': 'Automatically switch company when a company specific menu is clicked.',
    'sequence': 100,
    'version': '1.00',
    'website': 'https://www.steigendit.com',
    'author': 'Steigend IT Solutions',
    'description': """
Switch Companies Automatically
==============================
If there is company specific menus
in your multi-company environment
install this module to switch
company automatically when clicking
such menu item. All you need is to
add the following key-value pair in
the context of the action of such menu item:
context: {'auto_switch_company_id': <id_of_the_company>}  
    """,
    'depends': [
        'web',
    ],
    'external_dependencies' : {
        'python' : [],
    },
    'data': [
        'views/auto_switch_company.xml',
    ],
    'license': 'LGPL-3',
    'currency': 'EUR',
    'demo': [],
    'qweb':[],
    'installable': True,
    'application': False,
}
