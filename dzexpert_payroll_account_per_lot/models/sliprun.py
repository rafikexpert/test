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


class MySlipRun(models.Model):
	_inherit = 'hr.payslip.run'
	
	account_move_id = fields.Many2one('account.move', string='Movement')
	conf_payslip_accouting = fields.Selection('res.company',related='company_id.conf_payslip_accouting',readonly=True)

	# active = fields.Boolean('Active', default=True)
	# state=fields.Selection([
	# 	('draft','Draft'),
	# 	('done','Done')],string='State',default='draft')
	# name = fields.Char(string='Nom', required=True,track_visibility='onchange')	
	# image_small = fields.Binary("Image", attachment=True)	
	# description=fields.Html(string='Description')
		
	# attachment_number = fields.Integer(compute='_compute_attachment_number', string='P.J.')
	
	def action_cancel(self):	
		self.ensure_one()
		payslip_ids = [payslip.id for payslip in  self.slip_ids]
		related_move_ids = self.env['account.move'].serach([('payslip_id','in',payslip_ids)])
		
		for move in related_move_ids:
			if move:
				move.update({
					'line_ids': [(5,0,0)]
				})

		
	def action_confirm(self):	
		declassified_value = 0
		self.ensure_one()
		if self.payslip_count_draft!=0:
			raise UserError('le nombre des fiches paie en brouillon doit etre 0')
		# if self.payslip_count_draft==0:
		# 	raise UserError('le nombre des fiches paie en brouillon doit etre 0')
		
		raise UserError('button clicked confirm clicked')
		
		move = self.env['account.move'].create({
					'journal_id': self.journal_id.id,
					'ref': ' ',
					'company_id':self.company_id.id,
			})
		# vals1 = {'move_id':move.id,
		# 		'account_id':self.env.user.company_id.declassify_stock_account_adj.id ,
		# 		'partner_id': self._uid,
		# 		'credit': declassified_value,
		# 		'debit':0,
		# 		'name':'Operations de declassifications',
		# 		'company_id':self.company_id.id,
		# 	}
		# vals2 = {'move_id':move.id,
		# 		'account_id':self.env.user.company_id.declassify_stock_account_adj_minus.id ,
		# 		'partner_id': self._uid,
		# 		'credit': 0,
		# 		'debit':declassified_value,
		# 		'name':'Operations de declassifications',
		# 		'company_id':self.company_id.id,
		# 	}
		# self.env['account.move.line'].sudo().with_context(check_move_validity=False).create(vals1)
		# self.env['account.move.line'].sudo().with_context(check_move_validity=False).create(vals2)
		# move.sudo().with_context(check_move_validity=False).post()