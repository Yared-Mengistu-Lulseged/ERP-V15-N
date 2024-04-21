from odoo import models, fields, api

class ProductUpdate(models.Model):
    _inherit = 'product.template'
    # add field from project
    building_name = fields.Char(string='Building Name')
    apt_name = fields.Char(string='Apartment Name')
    location = fields.Char(string='Location')
    # add new field
    square_meter_price = fields.Float(string='Price Per Square ($)')
    square_size = fields.Float(string='Total Landing Area(M2)')
    floor_size = fields.Float(string='Floor Area(M2)')
    proportion_size = fields.Float(string='Proportion Area(M2)')
    room_number = fields.Char(string='Room Number')
    bed_room = fields.Char(string='Bed Rooms')
    store_laundry_room = fields.Char(string='Store & laundry')
    bath = fields.Char(string='Bath Room')
    kitchen = fields.Char(string='Kitchen Room')
    dining = fields.Char(string='Dining Room')
    maids = fields.Char(string='Maids Room')
    parking = fields.Char(string='Parking Place')
    uint_status = fields.Selection([
        ('Free', 'Free'),
        ('Sold', 'Sold'),
        ('Reserved', 'Reserved')
    ], string='Status')

    project_ids = fields.Many2one(
        'project.project',
        string='Projects'
    )
    tag_ids = fields.Many2many('project.tags',  string='Tags')
    exchange_rate = fields.Float(string='Exchange Rate(ETB)', default=1)
    @api.depends('project_ids', 'building_name', 'apt_name', 'location')
    def _onchange_project_ids(self):
        if self.project_ids or self.location or self.apt_name:
            self.building_name = self.project_ids.building_name
            self.apt_name = self.project_ids.apt_name
            self.location = self.project_ids.location

        else:
            self.building_name = False
            self.apt_name = False
            self.location = False

    @api.depends('square_size', 'square_meter_price', 'floor_size', 'proportion_size', 'exchange_rate')
    def _compute_list_price(self):
        for product in self:
            if product.floor_size and product.proportion_size:
                product.square_size = product.floor_size + product.proportion_size
            if product.square_size and product.square_meter_price and product.exchange_rate:
                product.list_price = product.square_size * product.square_meter_price * product.exchange_rate
            else:
                product.list_price = product.list_price  # Use the original value if dependencies are not set

    list_price = fields.Float(string='Sale Price', compute='_compute_list_price', store=True)





