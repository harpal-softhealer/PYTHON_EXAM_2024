from odoo import _, api, fields, models
from random import randint

class ProductTemplate(models.Model):
    _inherit = "product.template"


    def update_product_color(self):
        for product in self:
            product.color = randint(1,11)