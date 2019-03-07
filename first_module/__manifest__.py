# -*- coding: utf-8 -*-
{
    'name': "Primer Modulo",
    'summary': """
        Creacion del primer modulo""",
    'description': """
       Este es el ejemplo de la creacion de un modulo desde 0
    """,
    'author': "Xmarts",
    'website': "www.gtvp.odoo.com",    
    'category': 'Modulo',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'aplication': True,
    'auto_install': False,
}