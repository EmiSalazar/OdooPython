import Product_Template
import Purchase_Order
import Stock_Picking


db = 'soluciones-test'
username = 'soluciones@bbinco.com'
password = 'Bbinco1.0'
url = 'http://soluciones-test.odoo.com'

while 1:
    print("Que deseas modificar: \n1 - Inventario\n2 - Orden De Compra\n3 - Producto")
    x = input()
    if x == "1" or x == "2" or x == "3":
        if x == "1":
            Stock_Picking.modify(db, username, password, url)
            break
        if x == "2":
            Purchase_Order.modify(db, username, password, url)
            break
        if x == "3":
            Product_Template.modify(db, username, password, url)
            break
    else:
        print(x, " no es una opcion valida")