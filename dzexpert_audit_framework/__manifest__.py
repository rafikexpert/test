# -*- coding: utf-8 -*-
{
    'name': "DZExpert.com Audit framework",
    'summary': "DZExpert.com Audit framework",
    'description': "DZExpert.com Audit framework description", 
    'price':600,
    'currency':'EUR' ,
    'author': "DZExpert.com",
    'website': "http://www.google.com",
    'category': 'Project', 
    'version': '1.0.0',   
    'depends': [
		'account',
	],
    'data': [
        'security/security.xml',
		'views/session.xml',
        'views/verification.xml',
        'views/category.xml',
        'views/rule.xml',
		'views/menu.xml', 
        'data/seq.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,   
    'auto_install': False,
}