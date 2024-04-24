# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api

class UserAudit(models.Model):
    _name = "sh.user.audit"
    _description = "User Audit"

    name = fields.Char(string="Name", required=True)
    is_full_log = fields.Boolean(string="Full Log")
    is_read = fields.Boolean(string="Read")
    is_write = fields.Boolean(string="Write")
    is_create = fields.Boolean(string="Create")
    is_delete = fields.Boolean(string="Delete")
    is_all_users = fields.Boolean(string="All Users")
    user_ids = fields.Many2many('res.users',
                                string="Users",
                                domain="[('share','=',False)]")
    model_ids = fields.Many2many("ir.model")
    field_ids = fields.Many2many("ir.model.fields")
    last_sh_user_audit_log_id = fields.Many2one('sh.user.audit.log', string='Last User Audit Log')
    selected_model_ids = []

    @api.onchange("model_ids")
    def _onchange_model_ids(self):
        for i in self.model_ids:
            self.selected_model_ids.append(i.name)
