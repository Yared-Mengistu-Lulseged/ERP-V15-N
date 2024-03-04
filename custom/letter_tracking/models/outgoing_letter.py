from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)


class OutgoingLetter(models.Model):
    _name = 'outgoing.letter'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Outgoing Letters'

    reference_number = fields.Char(string='Reference Number')
    receiver = fields.Many2one('res.partner', string='Receiver', required=True)
    sent_date = fields.Date(string='Issue Date')
    name = fields.Char(string='Subject')
    content = fields.Text(string='Summery')
    sent_by = fields.Many2one('hr.employee', string='Sent By', tracking=1)
    attachment = fields.Binary(string='Letter Scan', attachment=True)
    attachment_add = fields.Boolean('attachment')
    stage = fields.Many2one('letter.stage', string='Stage', tracking=1)
    index = fields.Char('Index Number')
    link = fields.Char('Url Link')
    cc = fields.Text('CC')

    _sql_constraints = [
        ('reference_number', 'UNIQUE(reference_number)', 'The reference number must be unique!'),
    ]