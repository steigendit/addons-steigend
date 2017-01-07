# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016 Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################

from odoo import api, fields, models, _
    
class AccountChartTemplate(models.Model):
    _inherit = "account.chart.template"
    
    @api.multi
    def _prepare_all_journals(self, acc_template_ref, company, journals_dict=None):
        
        journal_data = super(AccountChartTemplate, self)._prepare_all_journals(acc_template_ref,
                                                            company,journals_dict=journals_dict)
        
        for journal in journal_data:
            if journal['name'] == _('Customer Invoices') and acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_611100').id,False):
                journal['default_credit_account_id'] = acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_611100').id,False)
                journal['default_debit_account_id'] = acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_611100').id,False)
            elif journal['name'] == _('Vendor Bills') and acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_212100').id,False):
                journal['default_credit_account_id'] = acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_212100').id,False)
                journal['default_debit_account_id'] = acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_212100').id,False)
            elif journal['name'] == _('Exchange Difference') and acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_662100').id,False):
                journal['default_credit_account_id'] = acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_662100').id,False)
                journal['default_debit_account_id'] = acc_template_ref.get(
                                                    self.env.ref('l10n_ao.ao_762100').id,False)
        
        if acc_template_ref.get(self.env.ref('l10n_ao.ao_431101').id,False) and \
                    acc_template_ref.get(self.env.ref('l10n_ao.ao_451101').id,False):
            #this checking is for verifying whether the loading chart is l10n_ao
            journal_data.extend([ {
                'type': 'general',
                'name': _('Sale Debit Notes'),
                'code': _('SCNJ'),
                'company_id': company.id,
                'default_credit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_611100').id,False),
                'default_debit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_611100').id,False),
#                 'refund_sequence': True,
#                 'show_on_dashboard': True,
            }, {
                'type': 'general',
                'name': _('Supplier Debit Notes'),
                'code': _('PCNJ'),
                'company_id': company.id,
                'default_credit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_212100').id,False),
                'default_debit_account_id': acc_template_ref.get(self.env.ref('l10n_ao.ao_212100').id,False),
#                 'refund_sequence': True,
#                 'show_on_dashboard': True,
            },])
        return journal_data
    
    @api.multi
    def generate_account(self, tax_template_ref, acc_template_ref, code_digits, company):
        account_tmpl_pool = self.env['account.account.template']
        account_pool = self.env['account.account']
        account_template_account_dict = super(AccountChartTemplate, self).generate_account(tax_template_ref, acc_template_ref, code_digits, company)
        account_template_objs = account_tmpl_pool.browse(account_template_account_dict.keys())
        for account_template_obj in account_template_objs:
            account_template_obj.update_template_property_field(account_template_account_dict[account_template_obj.id],company)
            if not account_template_obj.parent_id:
                continue
            account_parent_id = account_template_account_dict.get(account_template_obj.parent_id.id,False)
            account_obj = account_pool.browse(account_template_account_dict[account_template_obj.id])
            account_obj.write({'parent_id': account_parent_id})
        return account_template_account_dict
    

    
