# -*- coding: utf-8 -*-
{
    'name': "disable_apps",

    'summary': """
         admin privilage configuration for ERP deployment""",

    'description': """
        Configures menu visibility for customer and admin
    """,



    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customs/Disable menus',
    'version': '15.0.1.0.0',
    'license': 'AGPL-3',
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/Security_for_admin_rights_control.xml',
        'security/ir.model.access.csv',
        'views/disable_apps_menu_record.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
