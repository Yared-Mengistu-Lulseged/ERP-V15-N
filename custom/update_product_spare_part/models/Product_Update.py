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
    total_tax = fields.Float(string='Total Tax($) ', compute='_compute_list_price')
    total_tax_etb = fields.Float(string='Total Tax(ETB) ', compute='_compute_list_price')
    standard_price_usd = fields.Float(string='Cost($)', compute='_compute_list_price')
    standard_price = fields.Float(string='Cost(ETB)', compute='_compute_list_price')
    profit_usd = fields.Float(string='Profit($)', compute='_compute_list_price')
    profit = fields.Float(string='Profit(ETB)', compute='_compute_list_price')
    exchange_rate = fields.Float(string='Exchange Rate(ETB)', default=1)
    sales_price_etb = fields.Float(string='Sales Price(ETB)', compute='_compute_list_price')

    @api.onchange('fob_etb', 'fob_usd', 'freight_cost_usd', 'freight_cost_etb', 'exchange_rate')
    def _compute_list_price(self):
        for product in self:
            if product.fob_usd and product.freight_cost_usd and product.exchange_rate:
                product.total_tax = 0.75 * (product.fob_usd + product.freight_cost_usd)
                product.fob_etb = product.fob_usd * product.exchange_rate
                product.freight_cost_etb = product.freight_cost_usd * product.exchange_rate
                product.total_tax_etb = 0.75 * ((product.fob_usd * product.exchange_rate) + (product.freight_cost_usd * product.exchange_rate))
                product.standard_price_usd = product.fob_usd + product.freight_cost_usd + product.total_tax
                product.profit_usd = 0.3 * product.standard_price_usd
                product.sales_price_etb = product.profit + product.standard_price

            if product.fob_etb and product.freight_cost_etb:
                product.total_tax_etb = 0.75 * (product.fob_etb + product.freight_cost_etb)
                product.standard_price = product.fob_etb + product.freight_cost_etb + product.total_tax_etb
                product.profit = 0.3 * product.standard_price

            else:
                product.total_tax = product.total_tax
                product.standard_price = product.standard_price
                product.profit = product.profit
                product.exchange_rate = product.exchange_rate
                product.sales_price_etb = product.sales_price_etb
                product.freight_cost_etb = product.freight_cost_etb
                product.fob_etb = product.fob_etb
                product.fob_usd = product.fob_usd
                product.freight_cost_usd = product.freight_cost_usd
                product.total_tax_etb = product.total_tax_etb
                product.standard_price_usd = product.standard_price_usd
                product.profit_usd = product.profit_usd








