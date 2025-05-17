from odoo import _, api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    used_in_sale_order_product_ids = fields.Many2many("product.template",string="Sale Order Used Products",help="The Products were used in Customer's Sale Order", compute="_compute_sale_order_products")
    use_in_sale_order_product_count = fields.Integer()

    def _compute_sale_order_products(self):
        for partner in self:
            product_template_ids = partner.sale_order_ids.mapped("order_line").mapped("product_template_id").ids

            if product_template_ids:
                partner.used_in_sale_order_product_ids = [(6, 0, product_template_ids)]
                partner.use_in_sale_order_product_count = len(partner.used_in_sale_order_product_ids)
            else:
                partner.used_in_sale_order_product_ids = False

    # Method that show the count of partner's sale order products and open it.
    def action_view_partner_sale_order_products(self):
        return {
            'name': ("Products"),
            'type': 'ir.actions.act_window',
            'res_model': 'product.template',
            'domain': [('id', 'in', self.used_in_sale_order_product_ids.ids)],
            'view_mode': 'kanban,list,form',
            'view_type': 'kanban',
            'context':{
            'create':False,
            }
        }



