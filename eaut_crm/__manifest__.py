{
    'name': 'EAUT CRM',
    'version': '1.0',
    'description': 'Quản lý hồ sơ xét tuyển & CRM',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',

        # views
        'views/admission_application.xml',
        'views/admission_state.xml',
        'views/admission_major.xml',
        'views/admission_group.xml',
        'views/crm_plugin_switchboard.xml',

        # menus
        'views/eaut_crm_menus.xml',
    ],
    "application": True,
    'icon': '/eaut_crm/static/description/icon.png',
    "license": "OEEL-1",
}