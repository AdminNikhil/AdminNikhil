from odoo import models, fields, api
import logging
logger = logging.getLogger(__name__)


# class Sale_Summary_Xlsx(models.AbstractModel):
#     _name = 'report.inventory_reports.create_sales_summary_report'
#     _inherit = 'report.report_xlsx.abstract'

class SaleOrderView(models.Model):
    _inherit = 'sale.order'

    gmail=fields.Char(string="Email", required=True, default="admin@test.com")
    
    # @api.model
    # def _cron_reminder_print(self):
    #     for rec in self:
    #         print("Nikhi VVVVV", rec)
    #         _logger.info("NIkhil VVVVVVVVVVVVVVVVVVV1212312%s", rec)
