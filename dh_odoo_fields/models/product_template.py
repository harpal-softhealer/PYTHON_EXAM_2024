from odoo import _, api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    sh_product_status = fields.Many2one("dh.product.stages",string="Product Status")
    