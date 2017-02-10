# -*- coding: utf-8 -*-

from datetime import datetime, date, time
from openerp import api, fields, models 

class CrmCustomFields(models.Model):

  _inherit = "crm.lead"

  westelco_fecha_demo = fields.Date('Fecha de DEMO') 
  westelco_medio      = fields.Selection(
                          (('adwords','Adwords'),
                            ('reseller','Reseller'),
                            ('cliente_recurrente','Cliente Recurrente'),
                            ('recomendacion','Recomendación'),
                            ('eventos','Eventos'),
                            ('bluemarketing','Campaña BlueMarketing')), 'Medio', required=True)
  westelco_resellerusr   =  fields.Many2one(comodel_name = 'res.partner', string='Reseller')
  westelco_marca      =  fields.Many2one(comodel_name = 'westelco.marcas', string ='Marcas')


class WestelcoMarcas(models.Model):
  _name = 'westelco.marcas'
  marca_name  = fields.Char('Marca', required=True)


#crm_custom_fields()