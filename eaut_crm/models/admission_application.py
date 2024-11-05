
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class AdmissionApplication(models.Model):
    _name = 'admission.application'
    _description = 'Quản lý hồ sơ xét tuyển'
    _order = 'sequence'
    _inherit = 'mail.thread'

    # sort
    sequence = fields.Integer(default=10)

    # attributes
    name = fields.Char("Họ và tên", required=True)
    email = fields.Char("Địa chỉ email", required=True)
    phone = fields.Char("Số điện thoại", required=True)
    sales_person = fields.Many2one(
        'res.users', 
        string="Thầy/Cô hỗ trợ", 
        required=True, 
        domain=lambda self: [('groups_id', 'in', self.env.ref('base.group_user').ids)]
    )
    attached_documents = fields.One2many("admission.attached_document", 'application_id', string="Tài liệu đính kèm")
    state = fields.Selection(
        [
            ('pending', 'Đang chờ duyệt'),
            ('accept', 'Đạt'),
            ('denied', 'Không đạt'),
        ],
        string="Loại trạng thái",
        default='pending'
    )
    admission_major_id = fields.Many2one('admission.major', string="Ngành xét tuyển", required=True)
    admission_group_ids = fields.Many2many('admission.group', string="Tổ hợp xét tuyển")

    # Phone validate
    @api.constrains('phone')
    def _phone_validate(self):
        for record in self:
            if not record.phone.isdigit():
                raise ValidationError("Số điện thoại chỉ chứa các ký từ 0-9")
            if len(record.phone) != 10:
                raise ValidationError("Số điện thoại phải bao gồm 10 ký tự")
            if not record.phone.startswith('0'):
                raise ValidationError("Số điện thoại phải bắt đầu từ 0")
    
    @api.constrains('email')
    def _email_validate(self):
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        for record in self:
            if record.email and not re.match(email_regex, record.email):
                raise ValidationError("Email không đúng định dạng")
    
    # Fill admission group when admission major is selected
    @api.onchange('admission_major_id')
    def _fill_admission_group(self):
        if self.admission_major_id:
            # Lấy các tổ hợp liên kết với ngành đã chọn
            self.admission_group_ids = [(6, 0, self.admission_major_id.admission_group_ids.ids)]
        else:
            self.admission_group_ids = [(5, 0, 0)]  # Xóa tất cả nếu không có ngành học

    def test(self):
        return

