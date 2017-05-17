# -*- coding: utf-8 -*-

from openerp import api, fields, models

class SalesCustomFields(models.Model):

  _inherit = "sale.order"

  adw_sale_servicio = fields.Selection(string="Plantilla", help="Plantilla", selection=[('avanzado', "Avanzado"), ('tienda', 'Tienda'), ('avanzado_plantilla', 'Avanzado Plantilla')])
  westelco_b1 = fields.Boolean(string="Usar plantilla de B1", help="Al seleccionar permite utilizar una plantilla de PDF con los datos de B1.")

#sales_custom_fields()
