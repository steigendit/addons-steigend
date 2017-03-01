# -*- coding: utf-8 -*-

from odoo import api, models


class IrActionsReportXml(models.Model):
    _inherit = 'ir.actions.report.xml'

    @api.model
    def _check_selection_field_value(self, field, value):
        if field == 'report_type' and value == 'xls':
            return
        return super(IrActionsReportXml, self)._check_selection_field_value(field, value)
