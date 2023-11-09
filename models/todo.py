from odoo import  models, fields, api

class todo(models.Model):
    _name= 'todo.category' # the name of the model
    _description = 'Todo Category' # model description
    _order = 'name asc, id desc' # criteria to order the model records
    _task = 'Todo Task'
 

    name = fields.Char("Category name", required=True,index=True)  
    description = fields.Char("Category description", required=True,index=True)  
    task = fields.One2many( comodel_name='task.nom', inverse_name ="name", string="Tasks")

    def action_hello():
        return
