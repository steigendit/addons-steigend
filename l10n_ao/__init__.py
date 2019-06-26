# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016 - Today Steigend IT Solutions (Omal Bastin)
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################


from odoo import api, SUPERUSER_ID
import models
import wizard

def load_translations(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    chart_template = env.ref('l10n_ao.l10n_ao_chart_template')
    chart_template.process_coa_translations()
