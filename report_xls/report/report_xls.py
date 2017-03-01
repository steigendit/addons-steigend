# -*- coding: utf-8 -*-

import cStringIO

from odoo.report.report_sxw import report_sxw
from odoo.api import Environment

import logging
_logger = logging.getLogger(__name__)

try:
    import xlwt
except ImportError:
    _logger.debug('Can not import xls writer`.')


class ReportXls(report_sxw):

    def create(self, cr, uid, ids, data, context=None):
        self.env = Environment(cr, uid, context)
        report_obj = self.env['ir.actions.report.xml']
        report = report_obj.search([('report_name', '=', self.name[7:])])
        if report.ids:
            self.title = report.name
            if report.report_type == 'xls':
                return self.create_xlsx_report(ids, data, report)
        return super(ReportXls, self).create(cr, uid, ids, data, context)

    def create_xlsx_report(self, ids, data, report):
        self.parser_instance = self.parser(
            self.env.cr, self.env.uid, self.name2, self.env.context)
        objs = self.getObjects(
            self.env.cr, self.env.uid, ids, self.env.context)
        self.parser_instance.set_context(objs, data, ids, 'xls')
        file_data = cStringIO.StringIO()
        wb = xlwt.Workbook(encoding='utf-8')
        self.generate_xls_report(wb, data, objs)
        n = cStringIO.StringIO()
        wb.save(n)
        n.seek(0)
        return (n.read(), 'xls')

    def generate_xls_report(self, workbook, data, objs):
        raise NotImplementedError()
