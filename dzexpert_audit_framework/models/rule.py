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

class Rule(models.Model):
	_name = 'dzexpert.audit.rule'
	_inherit=['mail.thread']
	_description = "Rule"	
	_order = 'name asc'

	name=fields.Char(string='Nom:', required=True)  
	rule_type=fields.Selection([
		('manual','Manual'),
		('code','Code'),
		('auto','Auto')],string='Type de loi:',default='manual')
 
	sequence = fields.Integer(string="Sequence:", required=True)
	category_id = fields.Many2one('dzexpert.audit.category', 'Categorie:', required=True)
