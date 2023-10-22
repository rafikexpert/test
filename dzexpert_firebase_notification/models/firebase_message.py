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



	
	
class Message(models.Model):
	_name = 'dzexpert.firebase.message' 
	_inherit=['mail.thread']
	_description = "Firebase Message"	
	_order = 'reference asc'
	_rec_name ='reference'
 
 
	reference = fields.Char(string='Réference', required=False, copy=False, readonly=True, index=True, default=lambda self: 'New',track_visibility='onchange')
	content = fields.Text(string="Content",required = False)
	config_id = fields.Many2one("dzexpert.firebase.configuration",string="Configuration")
	type = fields.Selection(related="config_id.type",string="Type")
	user_dest_ids = fields.Many2many("res.users", string="Utilisateurs de destination")
	topic_ids=fields.Many2many("dzexpert.firebase.topic", string="Thème de destination")
	state = fields.Selection([("draft","Draft"),("tosend","toSend"),("sent","Sent")],required=True, copy=False,tracking=True, default='draft')
	origin = fields.Char(string="Origine")
		
	def action_confirm(self):
        # installing pyfcm package
		
		command = 'pip install pyfcm'
		cammand=command.split(' ')
		subprocess.run([sys.executable, "-m", cammand[0], cammand[1], cammand[2]], capture_output=True,text=True)
		

		for rec in self:
			if rec.reference =='New':
				tmp = self.env['ir.sequence'].next_by_code('dzexpert.firebase.message.sequence')
				rec.update({'reference':tmp,'state':'tosend'})
	
	@api.model
	def cron_send(self):
		messages=self.search([('state','=','tosend')])
		messages.action_send()
  
	def action_send(self):
		for rec in self:
			if rec.state == 'tosend':
				if rec.type == 'user':
					# Initialize the FCM client with your Firebase server key
					push_service = FCMNotification(rec.config_id.key)
					# Prepare the message payload
					message_title = rec.reference
					message_body = rec.content
					data_message = {
					"body": rec.content,
					"reference": rec.reference,
					"origin_user": rec.origin
					# Add more data fields as needed
					}

					for user in rec.user_dest_ids:
						# Get the Firebase device token for each user (you need to store this information)
						firebase_device_token = user.firebase_device_token

						# Send the message to the user's device
						result = push_service.notify_single_device(
							registration_id = firebase_device_token,
							message_title = message_title,
							message_body = message_body,
							data_message = data_message
						)
						if result["success"]==1:
							rec.state = 'sent'

				elif rec.type == "topic":
					# Initialize the FCM client with your Firebase server key
					push_service = FCMNotification(rec.config_id.key)

					# Prepare the message payload
					message_title = rec.reference
					message_body = rec.content
					data_message = {
						"body": rec.content,
						"reference": rec.reference,
						"origin_user": rec.origin
						# Add more data fields as needed
					}
					for tp in rec.topic_ids:
					# Send the message to the specified topic
						topic_name=tp.name
						result = push_service.notify_topic_subscribers(
							topic_name = topic_name,
							message_title = message_title,
							message_body = message_body,
							data_message = data_message
					)	
						if result["success"]==1:
								rec.state = 'sent'
