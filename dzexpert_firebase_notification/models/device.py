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



class Device(models.Model):
	_name = 'dzexpert.firebase.device' 
	_inherit=['mail.thread']
	_description = "Users's devices"	
	_order = 'user_id asc'
	_rec_name ='user_id'
 
 
	user_id = fields.Many2one("res.users",string="User")
	device_token = fields.Char(string='Device Token', required=True)