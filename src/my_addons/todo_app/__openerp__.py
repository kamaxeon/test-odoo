# -*- coding: utf-8 -*-
{
    'name': "To-Do Application",

    'summary': """
        Manage your personal Tasks with this module
        """,

    'description': """
        Manage your personal Tasks with this module
    """,

    'author': "Israel Santana",
    'website': "https://github.com/kamaxeon/test-odoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'application': True,
}