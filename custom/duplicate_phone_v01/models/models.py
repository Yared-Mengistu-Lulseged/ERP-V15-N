from odoo import models, fields, api
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('phone', 'mobile')
    def _check_duplicate_phone_mobile(self):
        for partner in self:
            if partner.phone or partner.mobile:
                domain = [
                    '|',
                    '&', ('phone', '=', partner.phone), ('phone', '!=', False),
                    '&', ('mobile', '=', partner.mobile), ('mobile', '!=', False),
                    ('id', '!=', partner.id)
                ]
                existing_partner = self.env['res.partner'].search(domain, limit=1)
                if existing_partner:
                    raise UserError("Phone number or mobile number already exists!")


class CRMPhone(models.Model):
    _inherit = 'crm.lead'

    @api.constrains('phone', 'mobile')
    def _check_duplicate_phone_mobile(self):
        for customer in self:
            if customer.phone or customer.mobile:
                domain = [
                    '|',
                    '&', ('phone', '=', customer.phone), ('phone', '!=', False),
                    '&', ('mobile', '=', customer.mobile), ('mobile', '!=', False),
                    ('id', '!=', customer.id)
                ]
                existing_customer = self.env['crm.lead'].search(domain, limit=1)
                if existing_customer:
                    raise UserError("Phone number or mobile number already exists!")
