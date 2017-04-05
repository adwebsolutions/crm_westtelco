# -*- coding: utf-8 -*-

from datetime import datetime, date, time
from openerp import api, fields, models

class CrmCustomFields(models.Model):

  _inherit = "crm.lead"

  westelco_fecha_demo            = fields.Date('Fecha de DEMO')
  westelco_resellerusr           = fields.Many2one(comodel_name = 'res.partner', string='Reseller')
  westelco_marcas                = fields.Many2one(comodel_name = 'westelco.marca', string ='Marcas')
  westelco_autorizado_finanzas   = fields.Boolean(string="Autorización de Finanzas", help="Autorización de Finanzas")
  westelco_comentarios_finanzas  = fields.Char(string="Comentarios de Finanzas", help="Comentarios de Finanzas")
  westelco_confirmacion_de_pago  = fields.Boolean(string="Confirmación de Pago", help="Confirmación de Pago")
  westelco_fecha_de_pago         = fields.Date('Fecha de Pago')
  westelco_forma_de_pago         = fields.Selection(
                                    (('cheque','Cheque'),
                                    ('tranferencia_bancaria', 'Transferencia Bancaria'),
                                    ('efectivo', 'Efectivo')), 'Forma de Pago')
  westelco_hay_demo              = fields.Boolean(string="DEMO", help="DEMO")
  westelco_fecha_proximo_cierre  = fields.Date('Fecha de Proximo Cierre')
  westelco_requiere_apoyo_ti     = fields.Boolean(string="Se requiere apoyo de TI", help="Se requiere apoyo de TI")
  westelco_asesor_de_ti          = fields.Many2one(comodel_name = 'res.partner', string='Asesor de TI')


class WestelcoMarcas(models.Model):
  _name = 'westelco.marca'
  name  = fields.Char('Marca', required=True)


#crm_custom_fields()
