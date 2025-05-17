from odoo import _, api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    used_in_sale_order_product_ids = fields.Many2many("product.template",string="Sale Order Used Products",help="The Products were used in Customer's Sale Order", compute="_compute_sale_order_products")

    def _compute_sale_order_products(self):
        for partner in self:
            print(f'\n partner ===========> ')
            print(f'\n partner.sale_order_ids.mapped("order_line") ===========> ')
            print('\n', partner.sale_order_ids.mapped("order_line"))
            print(f'\n partner.sale_order_ids.mapped("order_line").mapped("product_template_id") ===========> ')
            print('\n', partner.sale_order_ids.mapped("order_line").mapped("product_template_id"))
            print('\n', partner.sale_order_ids.mapped("order_line").mapped("product_template_id").ids)
            product_template_ids = partner.sale_order_ids.mapped("order_line").mapped("product_template_id").ids

            if product_template_ids:
                partner.used_in_sale_order_product_ids = [(6, 0, product_template_ids)]
            else:
                partner.used_in_sale_order_product_ids = False


