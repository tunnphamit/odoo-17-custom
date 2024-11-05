
from odoo import models, fields

class AdmissionGroup(models.Model):
    _name = 'admission.group'
    _description = 'Tổ hợp xét tuyển'
    _order = 'sequence'
    _inherit = 'mail.thread'

    # sort
    sequence = fields.Integer(default=10)

    # attributes
    name = fields.Char("Tên tổ hợp", required=True)
    major_ids = fields.Many2many('admission.major', string="Ngành học", tracking=True)
