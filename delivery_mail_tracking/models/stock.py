# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016-TODAY Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################

from odoo import models, fields, api, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    @api.multi
    def action_tracking_sent(self):
        """ Open a window to compose an email, with the shipment tracking template
            message loaded by default
        """
        self.ensure_one()
        template = self.env.ref('delivery_mail_tracking.mail_template_shipment_tracking_tracking', False)
        compose_form = self.env.ref('mail.email_compose_message_wizard_form', False)
        ctx = dict(
            default_model='stock.picking',
            default_res_id=self.id,
            default_use_template=bool(template),
            default_template_id=template and template.id or False,
            default_composition_mode='comment',
        )
        return {
            'name': _('Compose Email'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
            'context': ctx,
        }    
        
    