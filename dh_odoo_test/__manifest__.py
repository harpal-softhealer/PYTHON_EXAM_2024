# Dabhi Harpal Test Code.

{
    'name': 'Odoo Test ',
    'version': '0.1',
    'description': """Test""",
    'depends': [
        'base','sale'
    ],
    'data': [
        'security/ir.model.access.csv',

        'data/sale_data.xml',
        'views/sale_order_views.xml',

        'wizard/dh_state_selection_views.xml',
    ],
    # 'demo': [
    #     'data/product_demo.xml',
    # ],

}
