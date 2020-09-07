# -*- coding: utf-8 -*-
{
    'name': " TPCO Project",
    'category': 'TPCO',
    'version': '1.0.1',
    'author': "",
    'website': 'http://www.tpco.cl',
    "support": "",
    'summary': """
         TPCO Project""",
    'description': """
        Valida empresa y flujo cotizacion  
    """,
    "images": [],
    "depends": [
        "website_sale","sh_request_quote_multiple"
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/as_template.xml',
        'views/assets.xml',
    ],
    'qweb': [
    ],
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'installable': True,
    'auto_install': False,
    
}
