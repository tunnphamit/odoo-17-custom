
from odoo import models, fields, api

class AttachedDocument(models.Model):
    _name = 'crm.plugin.switchboard'
    _description = 'Cấu hình tích hợp tổng đài'

    vendor_name = fields.Char('Nhà cung cấp', required=True)