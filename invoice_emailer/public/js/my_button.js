frappe.ui.form.on('Item', {
  refresh: function(frm) {
      if (!frm.doc.__islocal) {
          frm.add_custom_button(__('Send Email'), function() {
              frappe.call({
                  method: 'invoice_emailer.public.python.email_invocing.send_email_with_invoices',
                  args: {
                      item_code: frm.doc.item_code
                  },
                  callback: function(r) {
                      if (!r.exc) {
                          frappe.msgprint(__('Email sent successfully'));
                      }
                  }
              });
          }, __('Actions'));
      }
  }
});