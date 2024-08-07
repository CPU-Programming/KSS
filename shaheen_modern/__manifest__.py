# -*- coding: utf-8 -*-
{
    'name': "shaheen modern ",

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
    'category': 'productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'mrp', 'purchase', 'maintenance', 'sale_management'],

    # always loaded
    'data': [

        'data/seq.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/followup_daily.xml',
        'views/maintenance.xml',
        'views/main_menu.xml',
        'report/report.xml',
        'report/followup.xml',
        'report/receipt_account.xml',
        'report/cash_receipt.xml',
        # 'report/periodic_reports.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,  # edited

}
