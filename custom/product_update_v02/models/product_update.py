from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    M2 = fields.Float(string='Square Meter')
    Kitchen = fields.Integer(string='Kitchen')
    Bath_room = fields.Integer(string='Bath Room')
    Maids_room = fields.Char(string='Maids Room')
    Bed_room = fields.Char(string='Bed Room')
    Floor_no = fields.Integer(string='Floor No')
    Room_no = fields.Integer(string='Room No')
    parking = fields.Integer(string='Parking')
    status = fields.Selection([('sold', 'Sold'), ('not_sold', 'Not Sold'), ('reserved', 'Reserved')], string='Status')
    PricePerSquare = fields.Integer(string='Price per Square')
    SquareMeter = fields.Integer(string='Square meter with Corridor')
    total = fields.Float(string="Total", compute="_compute_total")

    @api.depends('PricePerSquare', 'SquareMeter')
    def _compute_total(self):
        for record in self:
            record.total = record.PricePerSquare * record.SquareMeter



# class SaleOrderLine(models.Model):
#     _inherit = 'sale.order.line'
#
#     M2 = fields.Float(related='product_id.M2', string='Square Meter', readonly=True)
#     Kitchen = fields.Integer(related='product_id.Kitchen', string='Kitchen', readonly=True)
#     Bath_room = fields.Integer(related='product_id.Bath_room', string='Bath Room', readonly=True)
#     Maids_room = fields.Char(related='product_id.Maids_room', string='Maids Room', readonly=True)
#     Bed_room = fields.Char(related='product_id.Bed_room', string='Bed Room', readonly=True)
#     Floor_no = fields.Integer(related='product_id.Floor_no', string='Floor No', readonly=True)
#     Room_no = fields.Integer(related='product_id.Room_no', string='Room No', readonly=True)