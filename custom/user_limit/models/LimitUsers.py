from odoo import models, api, _
from odoo.exceptions import UserError

class LimitUser(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):
        get_LimitUser_Model = self.env['ui.user.limit'].search([])
        for records in get_LimitUser_Model:
             max_users = records._get_max_user_limit()
             if self.search_count([]) >= max_users:
                    raise UserError(_("Max allowable users have reached the limit"))
             else:
                    return super(LimitUser, self).create(vals)


