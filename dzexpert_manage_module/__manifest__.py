# -*- coding: utf-8 -*-
{
    'name': "DZExpert.com Manage Module",
    'summary': "DZExpert.com Manage Module",
    'description': """
		DZExpert.com Manage Module
    """, 
    'price':600,
    'currency':'EUR' ,
    'author': "DZExpert.com",
    'website': "http://www.dzexpert.com",
    'category': 'Project', 
    'version': '11.0.1.3',   
    'depends': [
		'stock',
		'account',
	],
    'data': [ 
		'security/security.xml',
		'views/task.xml',
		'views/menu.xml', 
		'data/cron.xml', 
		'security/ir.model.access.csv',   
    ],
    'installable': True,
    'application': True,   
    'auto_install': False,
}
