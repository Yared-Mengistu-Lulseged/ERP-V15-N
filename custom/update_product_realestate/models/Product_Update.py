from odoo import models, fields, api

class ProductUpdate(models.Model):
    _inherit = 'product.template'
    # add field from project
    building_name = fields.Char(string='Building Name')
    apt_name = fields.Char(string='Apartment Name')
    location = fields.Char(string='Location')
    # add new field
    square_meter_price = fields.Float(string='Price Per Square ')
    square_size = fields.Float(string='Total Landing Size(M2)')
    room_number = fields.Char(string='Room Number')
    bed_room = fields.Char(string='Bed Rooms')
    bath = fields.Char(string='Bath Room')
    kitchen = fields.Char(string='Kitchen Room')
    maids = fields.Char(string='Maids Room')
    parking = fields.Char(string='Parking place')
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

    @api.onchange('project_ids')
    def _onchange_project_ids(self):
        if self.project_ids:
            self.building_name = self.project_ids.building_name
            self.apt_name = self.project_ids.apt_name
            self.location = self.project_ids.location

        else:
            self.building_name = False
            self.apt_name = False
            self.location = False

    @api.depends('square_size', 'square_meter_price')
    def _compute_list_price(self):
        for product in self:
            if product.square_size and product.square_meter_price:
                product.list_price = product.square_size * product.square_meter_price
            else:
                product.list_price = product.list_price  # Use the original value if dependencies are not set

    list_price = fields.Float(string='Sale Price', compute='_compute_list_price', store=True)





