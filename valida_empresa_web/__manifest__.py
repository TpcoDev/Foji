# -*- coding: utf-8 -*-
{
    'name': "Ahorasoft TPCO Project",
    'category': 'TPCO',
    'version': '1.0.1',
    'author': "Ahorasoft",
    'website': 'http://www.ahorasoft.com',
    "support": "soporte@ahorasoft.com",
    'summary': """
        Ahorasoft TPCO Project""",
    'description': """
        Ahorasoft TPCO Project
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