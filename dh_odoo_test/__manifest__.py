# Dabhi Harpal Test Code.

{
    'name': 'Odoo Test ',
    'version': '0.1',
    'description': """Test""",
    'depends': [
        'base','sale'
    ],
    'data': [
        # Security & Access Rights
        'security/ir.model.access.csv',

        'data/sale_data.xml',
        'data/product_template_data.xml',

        'views/sale_order_views.xml',
        'views/res_partner_views.xml',

        'wizard/dh_state_selection_views.xml',
    ],
    # 'demo': [
    #     'data/product_demo.xml',
    # ],

}
