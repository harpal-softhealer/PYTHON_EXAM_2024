from odoo import _, api, fields, models

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.model_create_multi
    def create(self,vals_list):
        result = super(SaleOrderLine,self).create(vals_list)

        for vals in vals_list:
            print(f'\n vals ===========> ')
            print('\n', vals)
        for record in result:
            print(f'\n record ===========> ')
            print('\n', record)
        return result