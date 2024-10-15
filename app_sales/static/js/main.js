// odoo.define('app_sales.category_form_toggle', function (require) {
//     "use strict";

//     console.log("Test js odoo");

//     var FormController = require('web.FormController');

//     FormController.include({
//         renderButtons: function ($node) {
//             this._super.apply(this, arguments);
//             var self = this;

//             // Hàm để ẩn/hiện trường parent_id
//             function toggleParentField() {
//                 var $isParent = self.$el.find("#is_parent_div input[type='checkbox']");
//                 var $parentId = self.$el.find("#parent_id_div").closest('.o_field_widget');
//                 if ($isParent.prop('checked')) {
//                     $parentId.show();
//                 } else {
//                     $parentId.hide();
//                 }
//             }

//             toggleParentField(); // Gọi ban đầu để đặt trạng thái chính xác

//             // Lắng nghe sự kiện thay đổi của checkbox is_parent
//             self.$el.find("#is_parent_div input[type='checkbox']").on('change', function(){
//                 toggleParentField();
//             });
//         },
//     });
// });
