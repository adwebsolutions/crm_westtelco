# -*- coding: utf-8 -*-
from openerp import api, fields, models
# Aqui se importan los paquetes que necesites, en orden alfabético
#
# El nombre de la clase en notación CamelCase.
# La clases que se usan para extender los modelos, son modelos en sí mismos, por tanto heredan de models.Model
# En la version anterior de la API se usaba osv.osv.
#

class PartnerCustomFields(models.Model):

  # Aqui se especifica de qué modelo estamos herando.
  # res.partner es el nombre de la clase clientes.
  _inherit = "res.partner"

  # _name es el nombre que tiene la clase en el modelo. El nombre que tendrá la tabla en la base de datos. Y el que se usa para relaciones
  # En esta clase no lo tenemos porque solo estamos añadiendo algunos campos a un modelo que ya existe (res.partner)
  # En otras clases que pongo de ejemplo aquí si verán el _name

  # En la API vieja, los campos a la clase se espeficaban en un diccionario _columns
  # otra diferencia era que los tipos de datos tenían la forma fields.char, en minúsculas. En la nueva API esto cambia a fields.Char, en mayúsculas
  # A continuación, un ejemplo:

  #_columns = {
  #  'proseso_partner_rfc': fields.char('RFC'),
  #  'proseso_partner_modulos': fields.many2many('modulos', 'relation_table_partner_modulo', 'modulos_id', 'partner_id'),
  #}

  # A continuación un ejemplo de todos los atributos que puede tener un field

#          name = fields.Char(
#              string="Name",                   # Opcional, es el label del campo que aparecerá en la vista. Defaul es el mismo nombre del campo, en mayúsculas
#              compute="_compute_name_custom",  # Función que se usa para calcular el valor del campo para los campos calcuados.
#                                               # Por ejemplo, si el campo es edad, aqui se pone una funcion que calcule edad a partir de la fecha de nacimiento
#              store=True,                      # Si el campo es calculado, y este atributo es true, se guarda en la BD cada que se calcula. Ineficiente
#              select=True,                     # Force index on field
#              readonly=True,                   # El campo es de solo lectura
#              inverse="_write_name"            # Una funcion que se ejecuta cuando el campo se actualiza
#              required=True,                   # El campo es obligatorio
#              translate=True,                  # Disponible para traduccion
#              help='blabla',                   # Tooltip que aparecerá en la vista en el mouseover
#              company_dependent=True,          # Transforma la columna de un Campo normal a una property
#              search='_search_function'        # Custom search function mainly used with compute
#          )

  # A continuación los campos adicionales para los partners (usuarios)
  # El nombre de las variales debe ser en notacion snake_case

  westelco_puesto_trabajo    = fields.Char(string="Puesto de Trabajo", help="Puesto de trabajo del cliente")
  westelco_tiene_credito     = fields.Boolean(string="¿Tiene Crédito?", help="¿Tiene crédito?")
  westelco_dias_de_credito   = fields.Selection(string="Días de crédito", help="Días de crédito que tiene el cliente", selection=[(30, 30), (45, 45), (60, 60)])
  westelco_domicilio_fiscal  = fields.Char(string="Domicilio Fiscal", help="Domicilio Fiscal de la empresa")
  westelco_rfc               = fields.Char(string="RFC", help="RFC de la empresa")
  westelco_razon_social      = fields.Char(string="Razón Social", help="Razón Social de la empresa")
  westelco_reseller          = fields.Boolean(string="¿Es RESELLER?", help="¿Es un reseller?")
  westelco_certificaciones   = fields.Boolean(string="¿Tiene certificaciones?", help="¿Tiene certificaciones?")
  westelco_equipo_demo       = fields.Boolean(string="¿Tiene equipo para DEMO?", help="¿Tiene equipo para DEMO?")


#
#   En ocasiones es necesario crear campos que se comporten como catálogos abiertos, que el usuario puede crear nuevos items al hacer la asociación
#   Por ejemplo, en la oportunidad al seleccionar el cliente, aparece un Select y puedes seleccionar uno o crear uno nuevo.
#   Para hacer esto hay que tener un campo que sea una relacion Many2one, con el modelo relacionado.
#   Por ejemplo, si quisiera añadir un campo Industria, y que el usario pudiera crear nuevos si el que desea no está, debo hacer esto:


#   westelco_industria    = fields.Many2one('westelco.industria')

#   Luego, se debe crear el nuevo modelo, en este caso Industria
#   En el mismo archivo puede ser, aunque lo ideal es qeu sea en otro .py,
#   Notese aquí que la clase se llama WestelcoIndustrias pero el name es westelco.industrias... en la relacion uso westelco.industrias.

#          class WestelcoIndustrias(models.Model):
#            _name = 'westelco.industrias'
#            industria_name  = fields.Char('Industria', required=True)



#   =====================================================

#
# En la API vieja, había que hacer una llamada a la clase al final del archivo, para que se registrara.
# En módulos hechos con la API vieja, lo verás. Ya esto no hace falta
#
#PartnerCustomFields()
