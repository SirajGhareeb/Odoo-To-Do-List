# -*- coding: utf-8 -*-
{
    'name': "Siraj Todo Task",
    'summary': "Task Manager for easier life",
    'description': "Create and edit tasks, assign tasks to users, and make life easier for you and harder for assigned users.",
    'author': "PotatoFocus",
    'category': '',
    'version': '1.0',
    'depends': ['base', 'todo_users'], 
    'data': [
        'security/ir.model.access.csv',
        'views/todo_task_view.xml',
        'views/todo_user_task_inherited_views.xml',
    ],
    'application': True
}

