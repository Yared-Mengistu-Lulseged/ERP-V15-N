from odoo import models, fields, api

class ProductUpdate(models.Model):
    _inherit = 'product.template'
    # add field
    watt = fields.Char(string='Bulb Watt')
    color = fields.Char(string='Color')
    size = fields.Char(string='Lamp Size')












