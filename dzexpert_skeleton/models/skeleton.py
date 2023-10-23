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



	
	
class Consolidation(models.Model):
	_name = 'dzexpert.skeleton'
	_inherit=['mail.thread']
	_description = "Skeleton"	
	_order = 'name asc'

	
	active = fields.Boolean('Active', default=True)
	state=fields.Selection([
		('draft','Draft'),
		('done','Done')],string='State',default='draft')
	name = fields.Char(string='Nom', required=True,track_visibility='onchange')	
	image_small = fields.Binary("Image", attachment=True)	
	description=fields.Html(string='Description')
	company_id = fields.Many2one('res.company', 'Entreprise Locale')
		
	attachment_number = fields.Integer(compute='_compute_attachment_number', string='P.J.')	
		
	
	def action_done(self):
		self.state='done'
		
	def cron_update(self):
		f=1
		
	def _compute_attachment_number(self):
		attachment_data = self.env['ir.attachment'].read_group([('res_model', '=', 'erpish.achat.demande'), ('res_id', 'in', self.ids)], ['res_id'], ['res_id'])
		attachment = dict((data['res_id'], data['res_id_count']) for data in attachment_data)
		for expense in self:
			expense.attachment_number = attachment.get(expense.id, 0)
			
			
 
	def action_get_attachment_view(self):
		self.ensure_one()
		res = self.env.ref('base.action_attachment').sudo().read()[0]
		res['domain'] = [('res_model', '=', 'erpish.achat.demande'), ('res_id', 'in', self.ids)]
		res['context'] = {'create':True,'delete':True,'default_res_model': 'erpish.achat.demande', 'default_res_id': self.id}
		return res

	##Must be called on an object
	def api_mark_skeleton_done(self):
		for rec in self:
			if rec.state=='draft':
				rec.state='done'

	##Belongs to the class 
	@api.model
	def api_get_skeleton_documents(self):
		docs=self.env['dzexpert.skeleton'].search([('state','=','draft')])
		ret={'state':200,'data':[],'message':''}
		for doc in docs:
			ret.append({
				'id':doc.id,
				'name':doc.name,
				'content':doc.description,
			})
		return json.dumps(ret)
