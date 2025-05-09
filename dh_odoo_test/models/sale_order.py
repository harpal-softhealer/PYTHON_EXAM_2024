from odoo import _, api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"


    partner_id = fields.Many2one("res.partner")
    harpal dabhii is here

    # mass update sale order state.
    def action_mass_draft_sale(self):
        for sale_order in self:
            sale_order.state = "draft"

    
