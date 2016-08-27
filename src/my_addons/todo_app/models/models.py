# -*- coding: utf-8 -*-

from openerp import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'

    name = fields.Char(string="Description", required=True, )
    is_done = fields.Boolean(string="Done?",  )
    active = fields.Boolean(string="Active?", default=True )
# class todo_app(models.Model):
#     _name = 'todo_app.todo_app'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100