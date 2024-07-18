import frappe

@frappe.whitelist()
def send_email_with_invoices(item_code):
    # Fetch the latest 5 sales invoices for the item
    invoices = frappe.get_all('Sales Invoice Item',
        filters={'item_code': item_code},
        fields=['parent', 'creation'],
        order_by='creation desc',
        limit=5
    )

    if not invoices:
        frappe.msgprint('No sales invoices found for this item')
        return

    # Prepare the attachment
    attachments = []
    for invoice in invoices:
        doc = frappe.get_doc('Sales Invoice', invoice['parent'])
        attachments.append(frappe.attach_print('Sales Invoice', doc.name, print_format='Standard'))

    # Prepare the email content
    email_content = f"""
    <h3>Latest 5 Sales Invoices for Item {item_code}</h3>
    <ul>
    {''.join([f"<li>{inv['parent']} - {inv['creation']}</li>" for inv in invoices])}
    </ul>
    """

    # Send the email
    frappe.sendmail(
        recipients=['mohammedanas18025@gmail.com'],
        subject=f'Latest 5 Sales Invoices for Item {item_code}',
        message=email_content,
        attachments=attachments
    )

    frappe.msgprint('Email sent successfully')