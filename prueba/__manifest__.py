# -*- coding: utf-8 -*-
{
    'name': "Prueba",

    'summary': """
        Módulo para hacer pruebas""",

    'description': """
        Este apartado tiene como finalidad facilitar la creación de pruebas o exámenes para estudiantes
    """,

    'author': "Ángel Álvarez",
    'website': "http://www.google.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
