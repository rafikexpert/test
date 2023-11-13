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

class Category(models.Model):
  _name= 'dzexpert.audit.category' # the name of the model
  _description = 'audit category Description' # model description
  _inherit=['mail.thread']

  name = fields.Char(string='Nom', required=True)  
  sequence = fields.Integer(string='Sequence', index=True, required=True, default=1, help='Used to display digest tip in email template base on order')
  rule_ids = fields.One2many( comodel_name='dzexpert.audit.rule', inverse_name ="category_id", string="Rule", required=True)
