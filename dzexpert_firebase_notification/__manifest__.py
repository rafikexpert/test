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
    'base',
		'stock',
		'account',
	],
    'data': [
		'security/security.xml',
    'views/firebase_topic.xml',
		'views/firebase_configuration.xml',
		'views/firebase_message.xml',  
    'views/device.xml',
    'views/menu.xml', 
		'security/ir.model.access.csv',  
    'data/cron.xml', 
    'data/sequence.xml',
    ],
    'installable': True,
    'application': True,   
    'auto_install': False,
}
