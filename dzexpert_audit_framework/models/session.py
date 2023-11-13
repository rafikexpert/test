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

class Session(models.Model):
  _name= 'dzexpert.audit.session'
  _description = 'audit session Description'
  _order = 'date desc'
  _inherit=['mail.thread']

  name = fields.Char(string='Nom',  required=False, copy=False, readonly=True, index=True, default=lambda self: 'New',track_visibility='onchange')
  date = fields.Date(string="Date", required=True)
  notes = fields.Text(string='Notes')
  state=fields.Selection([
      ('draft','Draft'),
      ('en préparation','En préparation'),
      ('done','Done'),
      ('cancel','Cancel')],string='Status',default='draft')
  line_ids = fields.One2many( comodel_name='dzexpert.audit.verification', inverse_name ="session_id", string="Verification")
  category_id = fields.Many2one("dzexpert.audit.category", string = "Categorie", required=True)
  rules = fields.Many2many("dzexpert.audit.rule", string="rules", required=True )

  def action_progress(self):
    for rec in self:
      if rec.name =='New':
        tmp = self.env['ir.sequence'].next_by_code('dzexpert.audit.session.sequence')
        rec.name=tmp	
      rec.state='en préparation'

  def action_done(self):
      for rec in self:
        rec.state='done'

  def action_cancel(self):
      for rec in self:      
        rec.state='cancel'
