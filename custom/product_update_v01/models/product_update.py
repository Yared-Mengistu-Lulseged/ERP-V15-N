from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    M2 = fields.Float(string='Square Meter')
    Kitchen = fields.Integer(string='Kitchen')
    Bath_room = fields.Integer(string='Bath Room')
    Maids_room = fields.Char(string='Maids Room')

