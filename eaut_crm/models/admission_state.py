
from odoo import models, fields

class AdmissionState(models.Model):
    _name = "admission.state"
    _description = "Trạng thái của hồ sơ xét tuyển"

    sequence = fields.Integer("Thứ tự", default=10)
    name = fields.Char("Tên trạng thái", required=True)
    step = fields.Integer("Thứ tự của trạng thái", default=1)

    # Trường này cho chọn: Trạng thái chờ duyệt và Trạng thái đã duyệt
    step_type = fields.Selection(
        [
            ('pending', 'Đang chờ duyệt'),
            ('approved', 'Đã duyệt'),
        ],
        string="Loại trạng thái",
        default='pending'
    )