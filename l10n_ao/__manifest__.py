# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016 Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################
{
    'name': 'Angolan - Accounting',
    'version': '0.5',
    'category': 'Localization/Account Charts',
    'description': """
Angolan Accounting Module
=========================

Angolan accounting basic charts and localizations.

Also:
    - activates regional currency.
    - sets up taxes.
    """,
    'author': 'Steigend IT Solutions',
    'website': 'http://www.steigendit.com',
    'depends': ['account_parent','l10n_multilang'],
    'data': [
             'data/account_chart_template.xml',
             'data/account.account.template.csv',
             'data/account_chart_template_updated.xml',
            'data/account.tax.template.csv',
             'data/account_chart_template.yml',
             'data/localisation.xml',
             'data/res.bank.csv',
             'data/res.country.state.csv'
             ],
    'demo': [],
    'installable': True,
    'images': [],

    'post_init_hook': 'load_translations'
}
