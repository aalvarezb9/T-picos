# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class prueba(models.Model):
#     _name = 'prueba.prueba'
#     _description = 'prueba.prueba'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
# access_prueba_prueba,prueba_prueba,model_prueba_prueba,base_group_user,,1,1,1,1
class pregunta(models.Model):
	_name = 'prueba.pregunta'
	_description = 'Permite crear una pregunta'

	name = fields.Char('Pregunta', required=True)
	tipo = fields.Selection(string='Tipo', selection=[
			('s', 'Selección'), ('r', 'Respuesta breve')
		], default='s')
	puntaje = fields.Float('Puntaje', (2, 2))
	respuesta_id = fields.Many2one('prueba.respuesta', 'pregunta_id', string='Respuestas')

class respuesta(models.Model):
	_name = 'prueba.respuesta'
	_description = 'Posible respuesta de una pregunta'

	name = fields.Char('Respuesta')
	correcta = fields.Boolean('Correcta', default=False)

	pregunta_id = fields.One2many('prueba.pregunta', string='Pregunta')
