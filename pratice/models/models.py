# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
import logging
_logger = logging.getLogger(__name__)

class pratice(models.Model):
    _name = 'pratice.pratice'
    _description = 'pratice.pratice'

    commponet_name = fields.Char(string= "Commponet_Name", required=True)
    quantity = fields.Integer(string="Quantity", required=True, default=1)
    note = fields.Text(srting="Description")
    currency_id = fields.Many2one('res.currency', string='Currency')
    unit_price = fields.Integer('Unit price',currency_field='currency_id')

    tax_ids = fields.Many2many('account.tax', string='Taxes')

    subtotal=fields.Integer(string="Sub Total", compute="_computesubtotal")
    
    @api.depends('unit_price','quantity')
    def _computesubtotal(self):
        for rec in self:
            rec.subtotal = rec.unit_price * rec.quantity
            print("\n\nsubtotal",rec.subtotal)
            return rec.subtotal
    
    
    electronicsshop=fields.Many2one('pratice.electronicsshop')
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100


class ElectronicShop(models.Model):
    _name = 'pratice.electronicsshop'
    _description = 'All Electronic Commponet'
    customer_name= fields.Many2one("res.partner",string= "Customer")
    payment_terms= fields.Many2one("account.payment.terms", string="Payment Terms")
    date_action = fields.Datetime('Current Date & Time', required=False, readonly=False, select=True, default=lambda self: fields.datetime.now())

    
   
    att = fields.Boolean(string="Att")
    pratice_line_ids = fields.One2many('pratice.pratice', 'electronicsshop',string='Lines')
    # cashbox_lines_ids = fields.One2many('account.cashbox.line' , string='Cashbox Lines')

    @api.onchange('email_id')
    def validate_mail(self):
       if self.email_id:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email_id)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')
    
    email_id=fields.Char(string="Email", required=True, default="admin@test.com")
    # description = fields.Html(string='Description')

    gender= fields.Selection([('male','Male'),('female','Female')])
    
    
 

    @api.model
    def _cron_reminder_print(self):
        _logger.info("NIkhil VVVVVVVVVVVVVVVVVVV1212312")
        for rec in self:
            print("Nikhi VVVVV", rec)
            _logger.info("NIkhil VVVVVVVVVVVVVVVVVVV1212312%s", rec)


    # image=fields.Binary(string="Image", attachment=True)
    # admin_email=fields.Char('Admin Email',default='admin@test.com',readonly=False) #for user_id use ('res.users')
    # field_name = models.EmailField(max_length=254)
   
    
