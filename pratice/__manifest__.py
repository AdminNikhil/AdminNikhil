# -*- coding: utf-8 -*-
{
    'name': "pratice",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/pratice.xml',
        'views/Sale_Inherit.xml',
        'views/contacts_int.xml',
        'reports/purchase_report.xml',
        'reports/purchase_temp.xml',
        'reports/custom_header_footer.xml',
        'reports/sale_invoice.xml',
        'wizard/sale_summary.xml',
        'views/cron.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
