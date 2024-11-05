
from odoo import models, fields

class AdmissionMajor(models.Model):
    _name = 'admission.major'
    _description = 'Ngành xét tuyển'
    _order = 'sequence'
    _inherit = 'mail.thread'

    # sort
    sequence = fields.Integer(default=10)

    # attributes
    name = fields.Char("Tên ngành", required=True)
    major_code = fields.Char("Mã ngành", required=True)
    admission_group_ids = fields.Many2many('admission.group', string="Tổ hợp xét tuyển", tracking=True)

