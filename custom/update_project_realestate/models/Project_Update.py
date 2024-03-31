from odoo import models, fields

class ProjectUpdate(models.Model):
    _inherit = 'project.project'

    building_name = fields.Char(string='Building Name')
    apt_name = fields.Char(string='Apartment Name')
    location = fields.Char(string='Location')
    square_size = fields.Char(string='Total Landing Size(M2)')
    number_of_unit = fields.Char(string='Total Number House ')
    floors = fields.Char(string='Number Floor')
    house_floors = fields.Char(string='House Per Floor')




