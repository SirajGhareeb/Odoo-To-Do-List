from odoo import models, fields

class ToDoUser(models.Model):
    _name = 'todo.user'
    _description = 'To-Do User'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone')
    active = fields.Boolean(string='Active', default=True)
    task_ids = fields.One2many('todo.task', 'user_id', string='Tasks')