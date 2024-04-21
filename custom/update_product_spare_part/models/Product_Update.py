from odoo import models, fields, api

class ProductUpdate(models.Model):
    _inherit = 'product.template'
    # add field
    manufacturer = fields.Char(string='Manufacturer')
    model = fields.Char(string='Model')
    year = fields.Char(string='year')
    part_number = fields.Char(string='Part Number')
    vin = fields.Char(string='VIN Number')
    # add new field
    fob_usd = fields.Float(string='FOB Unit Price($)')
    fob_etb = fields.Float(string='FOB Unit Price(ETB)',  compute='_compute_list_price')
    freight_cost_usd = fields.Float(string='Freight cost($)')
    freight_cost_etb = fields.Float(string='Freight cost (ETB)',  compute='_compute_list_price')
    total_tax_etb = fields.Float(string='Total Tax(ETB) ')
    standard_price_etb = fields.Float(string='Total Cost(ETB)', compute='_compute_list_price')
    profit = fields.Float(string='Profit(ETB)')
    exchange_rate = fields.Float(string='Exchange Rate(ETB)', default=1)
    sales_price_etb = fields.Float(string='Sales Price(ETB)', compute='_compute_list_price')
    other_cost = fields.Float(string='Other Cost (ETB)',)
    direct_cost = fields.Float(string='Direct Cost (ETB)', compute='_compute_list_price')
    admin_cost = fields.Float(string='Admin(Indirect Cost) (ETB)')


    @api.onchange('fob_etb', 'fob_usd', 'freight_cost_usd', 'freight_cost_etb', 'exchange_rate', 'total_tax_etb', 'admin_cost', 'direct_cost', 'profit')
    def _compute_list_price(self):
        for product in self:
            if product.fob_usd and product.freight_cost_usd and product.exchange_rate and product.total_tax_etb:
                product.fob_etb = product.fob_usd * product.exchange_rate
                product.freight_cost_etb = product.freight_cost_usd * product.exchange_rate
                product.direct_cost = product.fob_etb + product.freight_cost_etb + product.other_cost + product.total_tax_etb
                product.standard_price_etb = product.direct_cost + product.admin_cost
                product.sales_price_etb = product.profit + product.standard_price_etb

            else:
                product.profit = product.profit
                product.exchange_rate = product.exchange_rate
                product.sales_price_etb = product.sales_price_etb
                product.freight_cost_etb = product.freight_cost_etb
                product.fob_etb = product.fob_etb
                product.fob_usd = product.fob_usd
                product.freight_cost_usd = product.freight_cost_usd
                product.total_tax_etb = product.total_tax_etb
                product.standard_price_etb = product.standard_price_etb
                product.other_cost = product.other_cost
                product.direct_cost = product.direct_cost
                product.admin_cost = product.admin_cost








