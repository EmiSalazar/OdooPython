import xmlrpc.client
import json

db = 'soluciones-test'
username = 'soluciones@bbinco.com'
password = 'Bbinco1.0'
url = 'http://soluciones-test.odoo.com'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

#print(models)

print("Ingrese el nombre del documento a editar:")
busqueda = input()

ids = models.execute_kw(db, uid, password, 'stock.picking', 'search', [[['name', '=', busqueda]]])

#document = models.execute_kw(db, uid, password, 'stock.picking', 'read', [ids], {'fields': ['id']})

document = models.execute_kw(db, uid, password, 'stock.picking', 'read', [ids], {'fields': ['name',
                                                                                            'origin',
                                                                                            'note',
                                                                                            'backorder_id',
                                                                                            'backorder_ids',
                                                                                            'move_type',
                                                                                            'state',
                                                                                            'group_id',
                                                                                            'priority',
                                                                                            'scheduled_date',
                                                                                            'date_deadline',
                                                                                            'has_deadline_issue',
                                                                                            'date',
                                                                                            'date_done',
                                                                                            'delay_alert_date',
                                                                                            'json_popover',
                                                                                            'location_id',
                                                                                            'location_dest_id',
                                                                                            'move_lines',
                                                                                            'move_ids_without_package',
                                                                                            'has_scrap_move',
                                                                                            'picking_type_id',
                                                                                            'picking_type_code',
                                                                                            'picking_type_entire_packs',
                                                                                            'hide_picking_type',
                                                                                            'partner_id',
                                                                                            'company_id',
                                                                                            'user_id',
                                                                                            'move_line_ids',
                                                                                            'move_line_ids_without_package',
                                                                                            'move_line_nosuggest_ids',
                                                                                            'move_line_exist',
                                                                                            'has_packages',
                                                                                            'show_check_availability',
                                                                                            'show_mark_as_todo',
                                                                                            'show_validate',
                                                                                            'use_create_lots',
                                                                                            'owner_id',
                                                                                            'printed',
                                                                                            'signature',
                                                                                            'is_locked',
                                                                                            'product_id',
                                                                                            'show_operations',
                                                                                            'show_reserved',
                                                                                            'show_lots_text',
                                                                                            'has_tracking',
                                                                                            'immediate_transfer',
                                                                                            'package_level_ids',
                                                                                            'package_level_ids_details',
                                                                                            'products_availability',
                                                                                            'products_availability_state',
                                                                                            'purchase_id',
                                                                                            'sale_id',
                                                                                            'activity_ids',
                                                                                            'activity_state',
                                                                                            'activity_date_deadline',
                                                                                            'activity_exception_decoration',
                                                                                            'activity_exception_icon',
                                                                                            'activity_user_id',
                                                                                            'activity_type_id',
                                                                                            'activity_type_icon',
                                                                                            'activity_summary',
                                                                                            'message_is_follower',
                                                                                            'message_follower_ids',
                                                                                            'message_partner_ids',
                                                                                            'message_channel_ids',
                                                                                            'message_ids',
                                                                                            'message_unread',
                                                                                            'message_unread_counter',
                                                                                            'message_needaction',
                                                                                            'message_needaction_counter',
                                                                                            'message_has_error',
                                                                                            'message_has_error_counter',
                                                                                            'message_attachment_count',
                                                                                            'message_main_attachment_id',
                                                                                            'website_message_ids',
                                                                                            'message_has_sms_error',
                                                                                            'id',
                                                                                            'display_name',
                                                                                            'create_uid',
                                                                                            'create_date',
                                                                                            'write_uid',
                                                                                            'write_date',
                                                                                            '__last_update',
                                                                                            'x_studio_referencia_interna',
                                                                                            'x_studio_referencia_del_cliente',
                                                                                            'x_studio_lista_1',
                                                                                            'x_studio_entrega_de_material',
                                                                                            'x_studio_lista',
                                                                                            'x_studio_responsable',
                                                                                            'x_studio_cliente',
                                                                                            'x_studio_direccin',
                                                                                            'x_studio_related_field_qLMOV',
                                                                                            'x_studio_ciudad']
                                                                                            })

document = document[-1]
#print(jsonToPython['id'])

#document = document[1:]


print(document)

while 1:
    print("Ingresa el nuevo estado: \n(1 = Borrador)\n(2 = En Espera)\n(3 = Preparado)\n(4 = Hecho)\n(5 = Cancelado)")

    state = input()

    if state == '1' or state == '2' or state == '3' or state == '4' or state == '5':
        if state == '1':
            update = models.execute_kw(db, uid, password, 'stock.picking', 'write', [[int(document['id'])], {'state': 'draft'}])
            print("Cambio realzado")
            break
        if state == '2':
            update = models.execute_kw(db, uid, password, 'stock.picking', 'write', [[int(document['id'])], {'state': 'confirmed'}])
            print("Cambio realzado")
            break
        if state == '3':
            update = models.execute_kw(db, uid, password, 'stock.picking', 'write', [[int(document['id'])], {'state': 'assigned'}])
            print("Cambio realzado")
            break
        if state == '4':
            update = models.execute_kw(db, uid, password, 'stock.picking', 'write', [[int(document['id'])], {'state': 'done'}])
            print("Cambio realzado")
            break
        if state == '5':
            update = models.execute_kw(db, uid, password, 'stock.picking', 'write', [[int(document['id'])], {'state': 'cancel'}])
            print("Cambio realzado")
            break
    else:
        print(state, " no es una opcion valida")
