from odoo import models, fields, api, _


class LetterStage(models.Model):
    _name = 'letter.stage'
    _description = 'Letter Stages'

    name = fields.Char('Name')
    requirements = fields.Text('Requirements')