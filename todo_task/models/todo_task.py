from odoo import models, fields, api


class TodoTask(models.Model):
    _name = "todo.task"
    _description = "To Do Task"

    name = fields.Char(string="Task Name")
    description = fields.Text(string="Description")
    user_id = fields.Many2one("todo.user", string="Assigned To")
    due_date = fields.Date(string="Due Date")
    state = fields.Selection(
        [("new", "New"), ("in_progress", "In Progress"), ("done", "Done")],
        default="new",
        string="Status",
    )
    state_icon = fields.Html(
        string="State Icon", compute="_compute_state_icon", store=False
    )

    @api.depends("state")
    def _compute_state_icon(self):
        icon_map = {
            "new": '<i class="fa fa-circle text-secondary mx-auto" title="New"/>',
            "in_progress": '<i class="fa fa-spinner text-warning" title="In Progress"/>',
            "done": '<i class="fa fa-check-circle text-success" title="Done"/>',
        }
        for rec in self:
            rec.state_icon = icon_map.get(rec.state, "")

    def action_set_status_new(self):
        """Set status to 'To Do'"""
        self.write({"state": "new"})

    def action_set_status_in_progress(self):
        """Set status to 'In Progress'"""
        self.write({"state": "in_progress"})

    def action_set_status_done(self):
        """Set status to 'Done'"""
        self.write({"state": "done"})


class ToDoUser(models.Model):
    _inherit = "todo.user"

    task_ids = fields.One2many("todo.task", "user_id", string="Tasks")
