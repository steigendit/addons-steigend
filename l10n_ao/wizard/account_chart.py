# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016 Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################

from openerp import models, fields, api,_

class WizardMultiChartsAccounts(models.TransientModel):
    _inherit = 'wizard.multi.charts.accounts'

    @api.multi
    def execute(self):
        """Inherited execute function to avoid creating new bank accounts, automatically applying taxes to products etc."""
        if self.chart_template_id.id == self.env.ref('l10n_ao.l10n_ao_chart_template').id:
            self.bank_account_ids = [(6,0,[])]
            self.sale_tax_id = False
            self.purchase_tax_id = False
        return super(WizardMultiChartsAccounts, self).execute()
    
    @api.multi
    def _create_bank_journals_from_o2m(self, company, acc_template_ref):
        '''
        This function creates bank journals and its accounts for each line encoded in the field bank_account_ids of the
        wizard (which is currently only used to create a default bank and cash journal when the CoA is installed).

        :param company: the company for which the wizard is running.
        :param acc_template_ref: the dictionary containing the mapping between the ids of account templates and the ids
            of the accounts that have been generated from them.
        '''
        super(WizardMultiChartsAccounts, self)._create_bank_journals_from_o2m(company, acc_template_ref)
        
        self.ensure_one()
        # Create the journals that will trigger the account.account creation
        if self.chart_template_id.id == self.env.ref('l10n_ao.l10n_ao_chart_template').id:
            jounral_data = [{
                'type': 'bank',
                'name': _('Bank'),
                'company_id': company.id,
                'default_credit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_431101').id,False),
                'default_debit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_431101').id,False),
#                 'refund_sequence': True,
                'show_on_dashboard': True,
            }, {
                'type': 'cash',
                'name': _('Cash'),
                'company_id': company.id,
                'default_credit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_451101').id,False),
                'default_debit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_451101').id,False),
#                 'refund_sequence': True,
                'show_on_dashboard': True,
            }]
        for journaldata in jounral_data:
            self.env['account.journal'].create(journaldata)
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
