# -*- coding: utf-8 -*-

{
    'name': 'Product pack',
    'version': '1.0',
    'category': 'Product',
    'sequence': 6,
    'author': 'Webveer',
    'summary': 'Allows you to create pack product in Odoo.',
    'description': "Allows you to create pack product in Odoo.",
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml'
    ],
    'qweb': [
        # 'static/src/xml/pos.xml',
    ],
    'images': [
        'static/description/product.jpg',
    ],
    'installable': True,
    'website': '',
    'auto_install': False,
    'price': 10,
    'currency': 'EUR',
}
