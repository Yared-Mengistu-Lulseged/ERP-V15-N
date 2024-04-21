from odoo import api, fields, models
from odoo.exceptions import ValidationError
class UILimitUser(models.Model):
    _name='ui.user.limit'
    Allowed_Users = fields.Integer(default=10, required=True, string='Allowed Users')
    Granted_By = fields.Many2one('res.users',string='Granted By')
    Granted_for=fields.Char(string='Granted For',required=True)
    Granted_Time = fields.Date(string='Granted Date',required=True,default=fields.Date.today(),constraints='_check_granted_date')

    def _default_partner(self):
        return self.env['res.users'].search([('name', '=', 'Administrator')], limit=1)

    @api.constrains('Granted_for')
    def _check_granted_date(self):
        for record in self:
            if record.Granted_Time > fields.Date.today():
                raise ValidationError('Grant Date can not be in the future!')
    @api.model
    def _get_max_user_limit(self):
        return self.Allowed_Users



