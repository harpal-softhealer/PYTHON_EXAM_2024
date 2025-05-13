from odoo import _, api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"


    is_change_with_mass_action = fields.Boolean(string="Change With Mass Action",tracking=True)


    # mass update sale order state.
    def action_mass_draft_sale(self):
        # for sale_order in self:
        #     if sale_order.state!= "draft":
        #         sale_order.with_context(action_mass_sale_draft=True).state = "draft"
        action = {
            'name': _('Sale Order'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'dh.state.selection',
            'view_id': self.env.ref('dh_odoo_test.dh_state_selection_view_form').id,
            'context': self.env.context,
            'target': 'new'
        }

        return action


    def write(self,vals_list):
        if vals_list and vals_list.get("state"):
            if self.env.context.get("action_mass_sale_draft"):
                self.is_change_with_mass_action = True
            if not self.env.context.get("action_mass_sale_draft"):
                self.is_change_with_mass_action = False
        res = super(SaleOrder,self).write(vals_list)
        return res

    
