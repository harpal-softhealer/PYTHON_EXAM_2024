# Dabhi Harpal Test Code.

{
    'name': 'Odoo Fields ',
    'version': '0.1',
    'description': """Odoo Moduel - that describe use of differnt fields""",
    'depends': [
        'sale_management'
    ],
    'data': [
        # Security & Access Rights
        'security/product_stage_security.xml',
        'security/ir.model.access.csv',

        # Views
        'views/dh_product_stages_views.xml',
        'views/product_template_views.xml',
        # 'views/sale_order_views.xml',

    ],

}
