import xmlrpc.client

def modify(db, username, password, url):
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    print("Ingrese el nombre del producto a editar:")
    busqueda = input()

    ids = models.execute_kw(db, uid, password, 'product.template', 'search', [[['name', '=', busqueda]]])

    document = models.execute_kw(db, uid, password, 'product.template', 'read', [ids], {'fields': ['id']})

    document = document[-1]

    print(document)

    while 1:
        print("Ingresa el nuevo tipo: \n(1 = Consumible)\n(2 = Servicio)\n(3 = Almacenable)")

        state = input()

        if state == '1' or state == '2' or state == '3':
            if state == '1':
                update = models.execute_kw(db, uid, password, 'product.template', 'write',
                                           [[int(document['id'])], {'type': 'consu'}])
                print("Cambio realzado")
                break
            if state == '2':
                update = models.execute_kw(db, uid, password, 'product.template', 'write',
                                           [[int(document['id'])], {'type': 'service'}])
                print("Cambio realzado")
                break
            if state == '3':
                update = models.execute_kw(db, uid, password, 'product.template', 'write',
                                           [[int(document['id'])], {'type': 'product'}])
                print("Cambio realzado")
                break
        else:
            print(state, " no es una opcion valida")
