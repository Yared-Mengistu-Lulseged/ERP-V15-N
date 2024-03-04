from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)


class IncomingLetter(models.Model):
    _name = 'incoming.letter'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Incoming Letters'

    reference_number = fields.Char(string='Reference Number')
    sender = fields.Many2one('res.partner', string='Sender', required=True)
    received_date = fields.Date(string='Received Date')
    issued_date = fields.Date('Issued Date')
    name = fields.Char(string='Subject')
    content = fields.Text(string='Summary')
    received_by = fields.Many2one('hr.employee', string='Received By', tracking=1)
    assigned_to = fields.Many2one('hr.employee', string='Assigned To', tracking=1)
    attachment = fields.Binary(string='Letter Scan', attachment=True)
    attachment_add = fields.Boolean('attachment')
    link = fields.Char('Url Link')
    index = fields.Char('Index Number')
    stage = fields.Many2one('letter.stage', string='Stage', tracking=1)