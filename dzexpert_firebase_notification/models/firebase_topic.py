# -*- coding: utf-8 -*-
from odoo import SUPERUSER_ID
from num2words import num2words
from odoo import api, models,fields
from odoo.exceptions import UserError 
from odoo import exceptions
from pyfcm import FCMNotification
from datetime import datetime
import math
import random,string
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, float_compare
import logging
import subprocess
import sys
_logger = logging.getLogger(__name__)



	
	
class Topic(models.Model):
	_name = 'dzexpert.firebase.topic' 
	_description = "Firebase Topic"	
	_order = 'name asc'


	name = fields.Char(string="Nom",required = True)
	user_topic_ids = fields.Many2many("res.users", string="Abonnés")
	
