{
    'name': 'WESTTELCO CRM campos adicionales',
    'category': 'Tools',
    'summary': 'Incluir campos adicionales en el crm',
    'website': 'https://www.adweb.mx',
    'version': '1.0',
    'description': """
Modulo de ADWEB para WESTELCO - CRM
===================================
    Este módulo incluye un grupo de campos nuevos a los modelos res.parters, crm.lead y sale.order, para cumplir los requerimientos de WESTTELCO


        """,
    'author': 'ADWEB',
    'depends': ['crm','sale'],
    'external_dependencies': {},
    'data': ['views/crm_custom_fields.xml','views/partner_custom_fields.xml','views/sales_custom_fields.xml'],
    'installable': True,
    'auto_install':False,
    'active':False,
}
