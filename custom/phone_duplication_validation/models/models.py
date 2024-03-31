from odoo import models, fields, api
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('phone', 'mobile')
    def _check_duplicate_phone_mobile(self):
        print(self)
        for partner in self:
            if partner.phone or partner.mobile:
                domain = [
                    '|',
                    '&', ('phone', '=', partner.phone), ('phone', '!=', False),
                    '&', ('mobile', '=', partner.mobile), ('mobile', '!=', False),
                    ('id', '!=', partner.id)
                ]
                existing_customers = self.env['res.partner'].search(domain)
                print(existing_customers.id)
                if existing_customers.filtered(lambda c: c.id != partner.id):
                    raise UserError("Phone number or mobile number already exists in contact! Contact Your Supervisor.")
                else:
                    return True
            else:
                raise UserError('Phone Number can not be empty!')


class CRMPhone(models.Model):
    _inherit = 'crm.lead'

    @api.constrains('phone', 'mobile')
    def _check_duplicate_phone_mobile(self):
        print(self)
        for customer in self:
            if customer.phone or customer.mobile:
                domain = [
                    '|',
                    '&', ('phone', '=', customer.phone), ('phone', '!=', False),
                    '&', ('mobile', '=', customer.mobile), ('mobile', '!=', False),
                    ('id', '!=', customer.id),
                    ('type', '=', 'lead')
                ]
                existing_customers = self.env['crm.lead'].search(domain)
                print(existing_customers)
                if existing_customers.filtered(lambda c: c.id != customer.id):
                    raise UserError("Phone number or mobile number already exists in lead!Contact Your Supervisor.")
                else:
                    return True
            else:
                raise UserError('Phone Number can not be empty!')


