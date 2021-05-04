import xmlrpc.client
from tkinter import *
from tkinter import messagebox

db = 'soluciones-test'
username = 'soluciones@bbinco.com'
password = 'Bbinco1.0'
url = 'http://soluciones-test.odoo.com'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

document = ""

class Editor(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.createWidgets()

    def Pruduct_Template(self):
        global document
        selected = StringVar()

        self.rad1 = Radiobutton(self, text='Consumible', value="consu", variable=selected)
        self.rad2 = Radiobutton(self, text='Servicio', value="service", variable=selected)
        self.rad3 = Radiobutton(self, text='Almacenable', value="product", variable=selected)

        self.rad1.grid(column=2, row=1)
        self.rad2.grid(column=2, row=2)
        self.rad3.grid(column=2, row=3)

        self.busqueda = Entry(self, width=10)
        self.busqueda.grid(column=2, row=0)

        self.busquedaButton = Button(self, font=("Arial", 12), fg='black', text="Buscar", highlightbackground='black',
                               command=lambda: self.Search_Product(self, self.busqueda.get()))
        self.busquedaButton.grid(row=0, column=3, sticky="nsew")


        self.saveButton = Button(self, font=("Arial", 12), fg='black', text="Guardar", highlightbackground='black',
                                command=lambda: models.execute_kw(db, uid, password, 'product.template', 'write',
                                                [[int(document['id'])], {'type': selected}]))
        self.saveButton.grid(row=7, column=2, sticky="nsew")


    def Search_Product(self, busqueda):
        global document
        ids = models.execute_kw(db, uid, password, 'product.template', 'search', [[['name', '=', busqueda]]])

        document = models.execute_kw(db, uid, password, 'product.template', 'read', [ids], {'fields': ['id']})

        document = document[-1]
        print(document)

    def Purchase_Order(self):
        global document
        selected = StringVar()

        self.rad1 = Radiobutton(self, text='Borrador', value="draft", variable=selected)
        self.rad2 = Radiobutton(self, text='En Espera', value="confirmed", variable=selected)
        self.rad3 = Radiobutton(self, text='Preparado', value="assigned", variable=selected)
        self.rad4 = Radiobutton(self, text='Hecho', value="done", variable=selected)
        self.rad5 = Radiobutton(self, text='Cancelado', value="cancel", variable=selected)

        self.rad1.grid(column=2, row=1)
        self.rad2.grid(column=2, row=2)
        self.rad3.grid(column=2, row=3)
        self.rad4.grid(column=2, row=4)
        self.rad5.grid(column=2, row=5)

        self.busqueda = Entry(self, width=10)
        self.busqueda.grid(column=2, row=0)

        self.busquedaButton = Button(self, font=("Arial", 12), fg='black', text="Buscar", highlightbackground='black',
                                    command=lambda: self.Search_Purchase_Order(self.busqueda.get()))
        self.busquedaButton.grid(row=0, column=3, sticky="nsew")

        self.saveButton = Button(self, font=("Arial", 12), fg='black', text="Guardar", highlightbackground='black',
                                command=lambda: models.execute_kw(db, uid, password, 'purchase.order', 'write',
                                                [[int(document['id'])], {'state': selected}]))
        self.saveButton.grid(row=7, column=2, sticky="nsew")

        document = ""

    def Search_Purchase_Order(self, busqueda):
        global document
        ids = models.execute_kw(db, uid, password, 'purchase.order', 'search', [[['name', '=', busqueda]]])

        document = models.execute_kw(db, uid, password, 'purchase.order', 'read', [ids], {'fields': ['id']})
        print(document)
        document = document[-1]


    def Stock_Picking(self):

        global document

        selected = StringVar()

        self.rad1 = Radiobutton(self, text='Borrador', value="draft", variable=selected)
        self.rad2 = Radiobutton(self, text='En Espera', value="confirmed", variable=selected)
        self.rad3 = Radiobutton(self, text='Preparado', value="assigned", variable=selected)
        self.rad4 = Radiobutton(self, text='Hecho', value="done", variable=selected)
        self.rad5 = Radiobutton(self, text='Cancelado', value="cancel", variable=selected)

        self.rad1.grid(column=2, row=1)
        self.rad2.grid(column=2, row=2)
        self.rad3.grid(column=2, row=3)
        self.rad4.grid(column=2, row=4)
        self.rad5.grid(column=2, row=5)

        self.busqueda = Entry(self, width=10)
        self.busqueda.grid(column=2, row=0)

        self.busquedaButton = Button(self, font=("Arial", 12), fg='black', text="Buscar", highlightbackground='black',
                                     command=lambda: self.Search_Stock_Picking(self.busqueda.get()))
        self.busquedaButton.grid(row=0, column=3, sticky="nsew")

        self.saveButton = Button(self, font=("Arial", 12), fg='black', text="Guardar", highlightbackground='black',
                                 command=self.saveStock(self))
        self.saveButton.grid(row=7, column=2, sticky="nsew")

    def saveStock(self, selected):

        global document

        models.execute_kw(db, uid, password, 'stock.picking', 'write',
                          [[int(document['id'])], {'state': selected}])

    def Search_Stock_Picking(self, busqueda):

        global document

        ids = models.execute_kw(db, uid, password, 'stock.picking', 'search', [[['name', '=', busqueda]]])

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
        print(document)

    def createWidgets(self):

        self.label = Label(self, font=("Arial", 24), relief=RAISED, justify=CENTER, bg='white', fg='black', borderwidth=0, text="Editar:")
        self.label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.stockButton = Button(self, font=("Arial", 12), fg='black', text="Inventario", highlightbackground='black', command=lambda: self.Stock_Picking())
        self.stockButton.grid(row=1, column=0, sticky="nsew")

        self.purchaseButton = Button(self, font=("Arial", 12), fg='black', text="Orden de Compra", highlightbackground='black', command=lambda: self.Purchase_Order())
        self.purchaseButton.grid(row=2, column=0, sticky="nsew")

        self.productButton = Button(self, font=("Arial", 12), fg='black', text="Productos", highlightbackground='black', command=lambda: self.Pruduct_Template())
        self.productButton.grid(row=3, column=0, sticky="nsew")



Edit = Tk()
Edit.title("Editor De ODOO")
Edit.resizable(True, True)
root = Editor(Edit).grid()
Edit.mainloop()
