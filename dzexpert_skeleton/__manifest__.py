# -*- coding: utf-8 -*-
{
    'name': "DZExpert.com Skeleton",
    'summary': "DZExpert.com Skeleton",
    'description': """
		DZExpert.com Skeleton
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
		'views/skeleton.xml',
		'views/menu.xml', 
		'data/cron.xml', 
		'security/ir.model.access.csv',   
    ],
    'installable': True,
    'application': True,   
    'auto_install': False,
}
