# -*- coding: utf-8 -*-

from datetime import datetime, date, time
from openerp import api, fields, models 

class CrmCustomFields(models.Model):

  _inherit = "crm.lead"

  westelco_fecha_demo     = fields.Date('Fecha de DEMO') 
  westelco_medio          = fields.Selection(
                            (('adwords','Adwords'),
                            ('reseller','Reseller'),
                            ('cliente_recurrente','Cliente Recurrente'),
                            ('recomendacion','Recomendación'),
                            ('eventos','Eventos'),
                            ('bluemarketing','Campaña BlueMarketing')), 'Medio', required=True)
  westelco_resellerusr    = fields.Many2one(comodel_name = 'res.partner', string='Reseller')
  westelco_marcas          = fields.Many2one(comodel_name = 'westelco.marca', string ='Marcas')
  westelco_auth_finanzas  = fields.Boolean('Autorización de Finanzas')
  westelco_observaciones  = fields.Text('Observaciones de Finanzas')
  westelco_confirm_pago   = fields.Boolean('Confirmación de Pago')
  westelco_fecha_pago     = fields.Date('Fecha de Pago')
  westelco_medio_pago     = fields.Selection(
                            (('efectivo','Efectivo'),
                              ('transferencia','Transferencia Bancaraia'),
                              ('deposito','Deposito Bancario'),
                              ('paypal', 'Paypal')), 'Forma de pago')


class WestelcoMarca(models.Model):
  _name = 'westelco.marca'
  name  = fields.Char('Marca')


#crm_custom_fields()