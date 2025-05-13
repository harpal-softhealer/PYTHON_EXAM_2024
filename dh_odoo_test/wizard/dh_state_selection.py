from odoo import _, api, fields, models


class DhStateSelection(models.TransientModel):
    _name = "dh.state.selection"
    _description = "Wizard to selection of state"

    dh_sale_order_state = fields.Selection([
        ('draft', "Quotation"),
        ('sent', "Quotation Sent"),
        ('sale', "Sales Order"),
        ('cancel', "Cancelled"),
    ])

    

    @api.model_create_multi
    def create(self,vals):
        ctx = self.env.context
        res = super().create(vals)
        if ctx and ctx.get("active_ids"):
            print(f'\n res.dh_sale_order_state ===========> ')
            print('\n', res.dh_sale_order_state)
            sale_order_ids = self.env["sale.order"].browse(ctx.get('active_ids'))
            print(f'\n sale_order_ids ===========> ')
            print('\n', sale_order_ids)
            for sale_order in sale_order_ids:
                if sale_order.state!=res.dh_sale_order_state:
                    sale_order.with_context(action_mass_sale_draft=True).state = res.dh_sale_order_state
        return res

    