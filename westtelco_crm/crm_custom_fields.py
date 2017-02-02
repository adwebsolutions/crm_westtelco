from openerp.osv import fields, osv

class crm_custom_fields(osv.osv):

  _inherit = "crm.lead"

  _columns = {
    'westtelco_crm_fecha_cita': fields.date('Fecha Cita de Ventas'),
    'westtelco_crm_no_promo': fields.boolean('No enviar promos'),
    'westtelco_crm_motivo': fields.char('Motivo de Contrato o Cancelación'),
    'westtelco_crm_tipo_empresa': fields.selection((('emprendedor','Emprendedor'),
    											('profesionista','Profesionista'), 
    											('gobierno','Gobierno'), 
    											('fundacion','Fundación'), 
    											('pyme','PyME'), 
    											('corporativo','Corporativo')), 
    											'Tipo de Empresa', required=True),	 
    'westtelco_crm_servicio': fields.selection((('avanzado','Avanzado'),
    											('tienda','Tienda Virtual'),
    											('tienda_plantilla','Tienda Virtual Plantilla'),
    											('catalogo','Catálogo'),
    											('catalogo_plantilla','Catálogo Plantilla'),
    											('avanzado_plantilla','Avanzado Plantilla'),
    											('estandar','Estándar'),
    											('desarrollo','Desarrollo a la Medida'),
    											('intranet_crm','Intranet/CRM'),
    											('identidad','Identidad Visual'),
    											('mantenimiento','Mantenimiento'),
    											('basico','Básico'),
    											('emarketing','eMarketing'), 
    											('hosting','Hosting')), 
    											'Servicio', required=True),
												
    'westtelco_crm_web': fields.char('¿Cuál es su página Web actual?'),
    'westtelco_crm_giro': fields.text('¿A qué se dedica la empresa?'),
    'westtelco_crm_competencia': fields.text('Mencione algunas empresas competencia'),
    'westtelco_crm_detalles_proyecto': fields.text('Describe de forma general el Proyecto'),
    'westtelco_crm_objetivo_proyecto': fields.text('¿Cuál es el objetivo del proyecto?'),
    'westtelco_crm_paginas_referencia': fields.text('Páginas de Referencia'),
    'westtelco_crm_cantidad_paginas': fields.char('¿Cuántas páginas tendrá el sitio?'),
    'westtelco_crm_cms': fields.boolean('¿Requiere Administrador de Contenidos?'),
    'westtelco_crm_catalogo': fields.boolean('¿Necesitan un catálogo de productos?'),
    'westtelco_crm_venta': fields.char('¿Quieren pedidos o venta en línea?'),
    'westtelco_crm_especiales': fields.text('Menciona algún otro requerimiento especial'),
    'westtelco_crm_oficina': fields.selection([('matriz','Matriz'),
    																					('providencia','Providencia'),
    																					('chapultepec','Chapultepec'),
    																					('cursos','Cursos')], 
    																					'Oficina', required=True, default="matriz"),

  }

crm_custom_fields()
