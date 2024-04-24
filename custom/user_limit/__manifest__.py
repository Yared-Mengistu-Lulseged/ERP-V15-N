# -*- coding: utf-8 -*-
{
    'name': "user_limit",

    'summary': """
        Zergaw's number of user limit app""",

    'description': """
        Limit customer users based on available resources
    """,

    'author': "Zergaw",
    'website': "https://zergaw.com/",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Zergaw Customs/Limit User',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'installable': True,
    'application': False,
    # always loaded
    'data': [
        'security/AccessRight_for_Limit_User.xml',
        'security/ir.model.access.csv',
        'views/View_for_UL_Zergaw.xml',
        'views/Menu_Item_for_UL_Zergaw.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
