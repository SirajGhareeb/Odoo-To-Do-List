# -*- coding: utf-8 -*-
{
    'name': "Siraj Todo user",
    'summary': "users to assign task for so that they can work harder",
    'description': "assing tasks to users so they can work without worrying about losing track of what they have to do",

    'author': "PotatoFocus",
    'website': "https://github.com/SirajGhareeb",
    'license': 'OPL-1',

    'category': '',
    'version': '1.0',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/todo_user_views.xml',
        # 'views/example_view.xml',``
    ],
    'application' : True,
}

