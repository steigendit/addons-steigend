# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016-2017 Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################
{
    'name': "Mail Shipment Tracking Details",
    'summary':"Send mails to customers regarding the shipment tracking details",
    'description': """
Send mails to customers regarding the shipment tracking details
    """,
    'author': "Steigend IT Solutions",
    'license': 'LGPL-3',
    'website': "https://www.steigendit.com",
    'category': 'Technical Settings',
    'version': '1.0',
    'depends': ['delivery', 'mail'],
    'data': [
        'views/mail_template_data.xml',
        'views/stock_view.xml'
    ],
    'application':True,
    'images': [],
    'demo': [
    ],
    
}
