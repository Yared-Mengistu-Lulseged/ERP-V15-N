from odoo import models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    remark = fields.Selection([
        ('remark1', 'NR'), ('remark2', 'NW'),
        ('remark3', 'SWOFF'), ('remark4', 'BUSSY'),
        ('remark5', 'ME'), ('remark6', 'NI'),
        ('remark 7', 'DR'), ('remark 8', 'WNO'),
        ('remark 9', 'NQ'), ('remark 10', 'BKD'),
        ('remark 11', 'RS'), ('remark 12', 'SHOW'),
        ('remark 13', 'DEAL')
    ], string='Remark')
    team_idd = fields.Many2one(
             'res.users', string='Sales consultant', default=lambda self: self.env.user,
             domain="['&', ('share', '=', False), ('company_ids', 'in', user_company_ids)]",
             check_company=True, index=True, tracking=True)

    project_ids = fields.Many2many(
        'project.project',
        'project_lead_rel',
        'lead_id',
        'project_id',
        string='Projects'
    )
    tele_marketer = fields.Many2one(
        'res.users', string='Tele Marketer', default=lambda self: self.env.user,
        domain="['&', ('share', '=', False), ('company_ids', 'in', user_company_ids)]",
        check_company=True, index=True, tracking=True)
    interested_in = fields.Selection([
        ('residential', 'Residential'),
        ('commercial', 'Commercial')
    ], string='Interested In')
# class CrmLead(models.Model):
#     _inherit = 'crm.lead'
#
#     team_id = fields.Many2one(
#         'res.users', string='Sales consultant', default=lambda self: self.env.user,
#         domain="['&', ('share', '=', False), ('company_ids', 'in', user_company_ids)]",
#         check_company=True, index=True, tracking=True)
