# -*- coding: utf-8 -*-
{
    'name': "Siraj Todo Task",
    'summary': "Task Manager for easier life",
    'description': "creat and edit tasks assign tasks to users make life easier for you and harder for assigned users.",

    'author': "PotatoFocus",
    'category': '',
    'version': '1.0',

    'depends': ['base','siraj_todo_user'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_task_view.xml',  
    ],
        'application' : True,
}

