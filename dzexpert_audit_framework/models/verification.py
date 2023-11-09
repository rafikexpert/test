# -*- coding: utf-8 -*-
from odoo import SUPERUSER_ID
from num2words import num2words
from odoo import api, models,fields
from odoo.exceptions import UserError 
from odoo import exceptions
from datetime import datetime
import math
import random,string
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, float_compare
import logging
import json

_logger = logging.getLogger(__name__)

class Verification(models.Model):
	_name = 'dzexpert.audit.verification'
	_inherit=['mail.thread']
	_description = "Verification"	
	_order = 'description asc'
    
	name=fields.Char(string='Nom:', required=True, copy=False)  
	session_id	 = fields.Many2one('dzexpert.audit.session', 'Session:', required=True)
	rule_id	 = fields.Many2one('dzexpert.audit.rule', 'Loi:', required=True)
	description=fields.Text(string='Description:')        
	category_id = fields.Many2one(string="Categorie:", related='session_id.category_id', store=True, required=True)
