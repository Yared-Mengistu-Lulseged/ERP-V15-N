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
                existing_customers = self.env['crm.lead'].search(domain)
                if existing_customers.filtered(lambda c: c.id != partner.id):
                    raise UserError("Phone number or mobile number alreadyy exists!")


class CRMPhone(models.Model):
    _inherit = 'crm.lead'

    def _check_duplicate_phone_mobile(self):
        for customer in self:
            if customer.phone or customer.mobile:
                domain = [
                    '|',
                    '&', ('phone', '=', customer.phone), ('phone', '!=', False),
                    '&', ('mobile', '=', customer.mobile), ('mobile', '!=', False),
                    ('id', '!=', customer.id)
                ]
                existing_customers = self.env['crm.lead'].search(domain)
                if existing_customers.filtered(lambda c: c.id != customer.id):
                    raise UserError("Phone number or mobile numberr already exists!")
