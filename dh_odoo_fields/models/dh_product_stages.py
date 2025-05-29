from odoo import _, api, fields, models

class DhProductStages(models.Model):
    _name = 'dh.product.stages'

    name = fields.Char(string="Name",copy=False)
    active = fields.Boolean(default=True)
    description = fields.Html(string="Description", required=True)
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ], string="Priority")


