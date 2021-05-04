import xmlrpc.client

def modify(db, username, password, url):
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    print("Ingrese el nombre del documento a editar:")
    busqueda = input()

    ids = models.execute_kw(db, uid, password, 'purchase.order', 'search', [[['name', '=', busqueda]]])

    document = models.execute_kw(db, uid, password, 'purchase.order', 'read', [ids], {'fields': ['id']})

    document = document[-1]

    print(document)

    while 1:
        print(
            "Ingresa el nuevo estado: \n(1 = Borrador)\n(2 = En Espera)\n(3 = Preparado)\n(4 = Hecho)\n(5 = Cancelado)")

        state = input()

        if state == '1' or state == '2' or state == '3' or state == '4' or state == '5':
            if state == '1':
                update = models.execute_kw(db, uid, password, 'purchase.order', 'write',
                                           [[int(document['id'])], {'state': 'draft'}])
                print("Cambio realzado")
                break
            if state == '2':
                update = models.execute_kw(db, uid, password, 'purchase.order', 'write',
                                           [[int(document['id'])], {'state': 'confirmed'}])
                print("Cambio realzado")
                break
            if state == '3':
                update = models.execute_kw(db, uid, password, 'purchase.order', 'write',
                                           [[int(document['id'])], {'state': 'assigned'}])
                print("Cambio realzado")
                break
            if state == '4':
                update = models.execute_kw(db, uid, password, 'purchase.order', 'write',
                                           [[int(document['id'])], {'state': 'done'}])
                print("Cambio realzado")
                break
            if state == '5':
                update = models.execute_kw(db, uid, password, 'purchase.order', 'write',
                                           [[int(document['id'])], {'state': 'cancel'}])
                print("Cambio realzado")
                break
        else:
            print(state, " no es una opcion valida")
