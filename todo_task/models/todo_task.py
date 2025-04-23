from odoo import models, fields

class ToDoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-Do Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    assigned_to = fields.Many2one('todo.user', string='Assigned To')
    due_date = fields.Date(string='Due Date')
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], string='Status', default='new')
    