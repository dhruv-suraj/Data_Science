from imbox import Imbox
import mysql.connector
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

with Imbox('imap.gmail.com',
        username = '',
        password = '',
        ssl=True,
        ssl_context=None,
        starttls=False) as imbox:
        inbox = imbox.messages(sent_from = '')

        for uid,message in inbox:
            message.sent_from
            message.sent_to
            message.subject
            message.headers
            message.message_id
            message.date
            message.body
            message.attachments
            body = message.body

            text = str(body['plain'][0])
            print(text)
            final = text.split()
            invoice_num = str(final[0:20])
            print(invoice_num)
            invoice_date = final[3]
            print(invoice_date)
            product_list = []
            products = " "
            for i in final[9:]:
                if(i == 'Billing'):
                    break
                product_list.append(i)
            for temp in product_list:
                products = products + temp + " "
            for i in range(len(product_list) - 1):
                product_list[i] = product_list[i].replace(',', '')
            address = []
            billing_address = " "
            for i in final[11 + len(product_list):]:
                if(i == '--'):
                    break
                address.append(i)
            for temp in address:
                billing_address  = billing_address + temp + " "
            client_name = final[0]

connection = mysql.connector.connect(host="localhost",user="root",passwd=" ", database = "invoicing")
cursor = connection.cursor()
cursor.callproc('insert_invoice', (invoice_num, client_name, invoice_date, billing_address))
for x in product_list:
    cursor.callproc('insert_products_into_invoiceitems', (x, invoice_num))
connection.commit()
cursor.close()
connection.close()