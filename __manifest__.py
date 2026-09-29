{
    'name': 'Rental Management',
    'version': '1.0',
    'summary': 'Simple Rental Management System',
    'author': 'Evan Jamaq',
    'category': 'Services',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/rental_views.xml',
    ],
    'installable': True,
    'application': True,
}