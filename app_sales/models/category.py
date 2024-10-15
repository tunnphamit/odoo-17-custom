from odoo import fields, models, api

class Category(models.Model):
    _name = "app_sales.product.category"
    _description = "Product category"

    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description")
    parent_id = fields.Many2one("app_sales.product.category", string="Parent")
    
    # Properties for smart buttons
    product_ids =fields.One2many("app_sales.product", "category_id")
    product_count = fields.Integer(compute="_compute_product_ids")

    @api.depends("product_ids")
    def _compute_product_ids(self):
        for rec in self:
            rec.product_count = len(rec.product_ids)

    def action_open_product_ids(self):
        return {
            "name": "Related product",
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "res_model": "app_sales.product",
            "target": "current",
            "domain": [("category_id", "=", self.id)],
            "context": {"default_category_id": self.id}, 
        }