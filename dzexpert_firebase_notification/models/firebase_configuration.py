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
_logger = logging.getLogger(__name__)



	
	
class Configuration(models.Model):
	_name = 'dzexpert.firebase.configuration' 
	_description = "Firebase Configuration"	
	_order = 'name asc'

	
	active = fields.Boolean('Active', default=True)
	
	name = fields.Char(string='Nom', required=True,track_visibility='onchange')	
	description=fields.Html(string='Description')
	type = fields.Selection([('topic','Topic'),('user','User')], string='Type',required=True)
	key = fields.Text(string='Token', required=True)	
