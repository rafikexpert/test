from odoo import models, fields, api

class task(models.Model):
    _name= 'task.nom' # the name of the model
    _description = 'Task Description' # model description
    _category = 'task category'
    _order = 'name desc, id desc' # criteria to order the model records

    name = fields.Char("Task nom", required=True,index=True)  
    description = fields.Char("Task description", required=True,index=True, delegate=True)  
    category = fields.Many2one('todo.category', string='category', required=True , ondelete='cascade' )
 #   category_id = fields.Many2one('todo.category', ondelete='set null', required=True, string='category')

    def action_hello():
        return    
