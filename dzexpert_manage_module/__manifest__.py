# -*- coding: utf-8 -*-
{
    "name": "DZExpert.com Manage Modules",
    "summary": "DZExpert.com Manage Modules",
    "description": """
		DZExpert.com Manage Module
    """,
    "price": 600,
    "currency": "EUR",
    "author": "DZExpert.com",
    "website": "http://www.dzexpert.com",
    "category": "Project",
    "version": "11.0.1.3",
    "depends": [
        "base",
        "account",
    ],
    "data": [
        "security/security.xml",
        "views/task.xml",
        "views/model.xml",
        "views/tutorial.xml",
        "views/menu.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
