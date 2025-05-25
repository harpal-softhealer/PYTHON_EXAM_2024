from odoo import _, api, fields, models

class DhProductStages(models.Model):
    _name = 'dh.product.stages'

    name = fields.Char(string="Name",copy=False)