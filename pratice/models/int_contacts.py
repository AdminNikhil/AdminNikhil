from odoo import models, fields, api

class Contacts(models.Model):
    _inherit = 'res.partner'

    nationality = fields.Many2one("res.country", string = 'Nationality')
    passport = fields.Char(string="Passport No")
    other_id = fields.Integer(string="Other Id")    

   