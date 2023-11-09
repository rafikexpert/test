# -*- coding: utf-8 -*-
{
    'name': "Todo app",
    'summary': "Todo app ",
    'description': "Todo app description", 
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
		'security/ir.model.access.csv',
    'views/todo.xml',
    'views/menu.xml',

    ],
    'installable': True,
    'application': True,   
    'auto_install': False,
}

