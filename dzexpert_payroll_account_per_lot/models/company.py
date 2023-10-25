# -*- coding: utf-8 -*-

from odoo import fields, models, api
from operator import itemgetter
import logging
_logger = logging.getLogger(__name__) 

class Company(models.Model):
	_inherit = 'res.company'
	
	conf_slips_accounting_lines = fields.Selection([('normal', 'Par employe'),
												('batch', 'Par journal')
									],default = 'normal', required = True,
									string = 'Ecriture comptable de paie' )
	