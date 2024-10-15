{
    "name": "App Sales",
    "version": "1.0",
    "category": "sale",
    "depends": [
        "base",
        'mail',
    ],
    "data": [
        "security/ir.model.access.csv",

        "views/product.xml",
        "views/product_category.xml",
        "views/app_sales_menus.xml",
    ],
    "assets": {
        'web.assets_backend': [
            "app_sales/static/scss/custom.scss",
            'app_sales/static/js/main.js',
        ],
        "web.assets_frontend": [
            "app_sales/static/scss/custom.scss",
        ],
    },
    "application": True,
    "license": "OEEL-1",
}