from odoo import fields, models, api

class Product(models.Model):
    _name = "app_sales.product"
    _description = "Product for App Sales"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description")
    thumbnail = fields.Binary(string="Product image")
    sales_price = fields.Float(string="Sales price", required=True)
    purchase_price = fields.Float(string="Purchase price", required=True)
    category_id = fields.Many2one("app_sales.product.category", string="Category")
    gift_ids = fields.Many2many("app_sales.product", 'product_gift_rel', 'product_id', 'gift_id', string="Gifts")
