
from odoo import models, fields, api

class AttachedDocument(models.Model):
    _name = 'admission.attached_document'
    _description = 'Document for Admission application'

    name = fields.Char('Tên tài liệu', required=True)
    file = fields.Binary('File', required=True)
    application_id = fields.Many2one('admission.application', string="Hồ sơ xét tuyển")