from datetime import datetime
from datetime import date, datetime, time
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api,_
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
from odoo.exceptions import ValidationError
import logging
logger = logging.getLogger(__name__)

class PracticeSaleWizard(models.TransientModel):
    _name = 'practice.sale.wizard'

    start_date = fields.Date(string="Start date")
    end_date = fields.Date(string="End Date")
    # default=fields.Date.today()

    def button_fun(self):
        for rec in self:
            raise ValidationError("I Dont know")