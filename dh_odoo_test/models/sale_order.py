from odoo import _, api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    # mass update sale order state.
    def action_mass_draft_sale(self):
        for sale_order in self:
            sale_order.state = "draft"

    
