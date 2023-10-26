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
		related_move_ids = self.env['account.move'].search([('payslip_id','in',payslip_ids)])
		
		for move in related_move_ids:		
			move.update({
				'line_ids': [(5,0,0)]
			})
			move.unlink()

		
	def action_confirm(self):	
		self.ensure_one()
		if self.payslip_count_draft!=0:
			raise UserError('le nombre des fiches paie en brouillon doit etre 0')

		payslip_ids = [payslip.id for payslip in  self.slip_ids]
		related_move_ids = self.env['account.move'].search([('payslip_id','in',payslip_ids)])
		if not related_move_ids:
			move = self.env['account.move'].create({
					'journal_id': self.journal_id.id,
					'ref': ' ',
					'company_id':self.company_id.id,
			})
			if self.conf_payslip_accouting == 'batch':
				credit = self.compute_payslips_credit()
				vals = {'move_id':move.id,
					'account_id':self.journal_id.id ,
					'partner_id': self._uid,
					'credit': credit,
					'debit':0,
					'name':'Operation paie ' + str(self.name),
					'company_id':self.company_id.id,
				}
				self.env['account.move.line'].sudo().with_context(check_move_validity=False).create(vals)
				move.sudo().with_context(check_move_validity=False).post()	
				self.update({'account_move_id':move})
			else:
				_logger.debug('call the super method')
				credit = 900
			
			# Under Lot there should be a new TAB, called : Comptabilite with :
			# Link to accounting Entry : account.move
			# Button to confirm and generate the accountry entry for confirmed salary slips
			# Button the cancel the accounting entry with the special access right.
			
		
	@api.model
	def compute_payslips_batches_credit(self):
		return 100