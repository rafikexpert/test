# -*- coding: utf-8 -*-
{
    'name': "DZExpert.com Firebase Notification",
    'summary': "DZExpert.com Firebase Notification",
    'description': """
		DZExpert.com Firebase Notification
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
		'views/firebase_notification.xml',
		'views/menu.xml', 

		'security/ir.model.access.csv',   
    ],
    'installable': True,
    'application': True,   
    'auto_install': False,
}
