from odoo import models, fields

class LeadUpdate(models.Model):
    _inherit = 'crm.lead'


    lead_status = fields.Selection([
        ('Interested', 'Interested'),
        ('Not Interested', 'Not Interested'),
        ('No Answer', 'No Answer'),
        ('Wrong Number', 'Wrong Number'),
        ('Call Back Requested ', 'Call Back Requested '),
        ('Information Requested', 'Information Requested'),
        ('Follow-up Scheduled', 'Follow-up Scheduled'),
        ('Appointment Set', 'Appointment Set'),
        ('Show Site', 'Show Site')

    ], string='Lead Status')
    interested_in = fields.Selection([
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial')
    ], string='Interested In')
    # project_ids = fields.Many2many(
    #     'project.project',
    #     string='Projects'
    # )
    tele_marketer = fields.Many2one(
        'res.users', string='Tele Marketer', default=lambda self: self.env.user,
        domain="['&', ('share', '=', False), ('company_ids', 'in', user_company_ids)]",
        check_company=True, index=True, tracking=True)
    surveyor = fields.Many2one(
        'res.users', string='Surveyor', default=lambda self: self.env.user,
        domain="['&', ('share', '=', False), ('company_ids', 'in', user_company_ids)]",
        check_company=True, index=True, tracking=True)




