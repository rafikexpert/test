# -*- coding: utf-8 -*-
{
    'name': "DZExpert.com payroll account per lot",
    'summary': "DZExpert.com payroll account per lot",
    'description': """
      DZExpert.com payroll account per lot
    """, 
    'price':600,
    'currency':'EUR' ,
    'author': "DZExpert.com",
    'website': "http://www.dzexpert.com",
    'category': 'Project', 
    'version': '11.0.1.3',   
    'depends': [
    'erpish_dz_hr_salary',
    'base',
		'account',

	],
    'data': [
		# 'security/security.xml',
    'views/sliprun.xml',
    'views/company.xml',
		# 'security/ir.model.access.csv',   
    ],
    'installable': True,
    'application': True,   
    'auto_install': False,
}