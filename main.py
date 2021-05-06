import tkinter
import xmlrpc.client
from tkinter import *
from tkinter import messagebox

db = 'soluciones-dev'
username = 'soluciones@bbinco.com'
password = 'Bbinco1.0'
url = 'https://soluciones-dev.odoo.com'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))


class Editor(Frame):
    document = ""
    stock = False
    product = False
    purchase = False

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.label = Label(self, font=("Arial", 24), relief=RAISED, justify=CENTER, bg='white', fg='black', borderwidth=0, text="      ")
        self.stockButton = Button(self, font=("Arial", 12), fg='black', text="Inventario", highlightbackground='black',
                                  command=lambda: self.Stock_Picking())
        self.purchaseButton = Button(self, font=("Arial", 12), fg='black', text="Orden de Compra",
                                     highlightbackground='black', command=lambda: self.Purchase_Order())
        self.productButton = Button(self, font=("Arial", 12), fg='black', text="Productos", highlightbackground='black',
                                    command=lambda: self.Pruduct_Template())
        self.parent = master
        self.grid()
        self.createWidgets()

    def Pruduct_Template(self):
        self.product = True
        selected = StringVar()
        self.productButton['state'] = tkinter.DISABLED

        if self.purchase == True:
            self.Purchase_Order_Rad1.grid_remove()
            self.Purchase_Order_Rad2.grid_remove()
            self.Purchase_Order_Rad3.grid_remove()
            self.Purchase_Order_Rad4.grid_remove()
            self.Purchase_Order_Rad5.grid_remove()
            self.Purchase_Order_Search_Box.grid_remove()
            self.Purchase_Order_Search_Button.grid_remove()
            self.Purchase_Order_Save_Button.grid_remove()
            self.Purchase_Order_Rad6.grid_remove()
            self.purchase = False
            self.purchaseButton['state'] = tkinter.NORMAL

        if self.stock == True:
            self.Stock_Picking_Rad1.grid_remove()
            self.Stock_Picking_Rad2.grid_remove()
            self.Stock_Picking_Rad3.grid_remove()
            self.Stock_Picking_Rad4.grid_remove()
            self.Stock_Picking_Rad5.grid_remove()
            self.Stock_Picking_Search_Box.grid_remove()
            self.Stock_Picking_Search_Button.grid_remove()
            self.Stock_Picking_Save_Button.grid_remove()
            self.stock = False
            self.stockButton['state'] = tkinter.NORMAL

        self.Pruduct_Template_Rad1 = Radiobutton(self, state=DISABLED, text='Consumible', value="consu", variable=selected)
        self.Pruduct_Template_Rad2 = Radiobutton(self, state=DISABLED, text='Servicio', value="service", variable=selected)
        self.Pruduct_Template_Rad3 = Radiobutton(self, state=DISABLED, text='Almacenable', value="product", variable=selected)

        self.Pruduct_Template_Rad1.grid(column=2, row=1)
        self.Pruduct_Template_Rad2.grid(column=2, row=2)
        self.Pruduct_Template_Rad3.grid(column=2, row=3)

        self.Pruduct_Template_Search_Box = Entry(self, width=25)
        self.Pruduct_Template_Search_Box.grid(column=2, row=0)

        self.Pruduct_Template_Search_Button = Button(self, font=("Arial", 12), fg='black', text="Buscar",
                                                     highlightbackground='black',
                                                     command=lambda: self.Search_Product(
                                                         self.Pruduct_Template_Search_Box.get()))
        self.Pruduct_Template_Search_Button.grid(row=0, column=3, sticky="nsew")

        self.Pruduct_Template_Save_Button = Button(self, state=DISABLED, font=("Arial", 12), fg='black', text="Guardar",
                                                   highlightbackground='black',
                                                   command=lambda: models.execute_kw(db, uid, password,
                                                                                     'product.template', 'write',
                                                                                     [[int(self.document['id'])],
                                                                                      {'type': selected.get()}]))
        self.Pruduct_Template_Save_Button.grid(row=7, column=2, sticky="nsew")

    def Search_Product(self, busqueda):
        ids = models.execute_kw(db, uid, password, 'product.template', 'search', [[['name', '=', busqueda]]])

        self.document = models.execute_kw(db, uid, password, 'product.template', 'read', [ids], {'fields': ['id']})

        self.document = self.document[-1]
        print(self.document)
        if self.document['id'] != "":
            self.Pruduct_Template_Rad1['state'] = tkinter.NORMAL
            self.Pruduct_Template_Rad2['state'] = tkinter.NORMAL
            self.Pruduct_Template_Rad3['state'] = tkinter.NORMAL
            self.Pruduct_Template_Save_Button['state'] = tkinter.NORMAL

    def Purchase_Order(self):
        selected = StringVar()

        self.purchase = True

        self.purchaseButton['state'] = tkinter.DISABLED

        if self.stock == True:
            self.Stock_Picking_Rad1.grid_remove()
            self.Stock_Picking_Rad2.grid_remove()
            self.Stock_Picking_Rad3.grid_remove()
            self.Stock_Picking_Rad4.grid_remove()
            self.Stock_Picking_Rad5.grid_remove()
            self.Stock_Picking_Search_Box.grid_remove()
            self.Stock_Picking_Search_Button.grid_remove()
            self.Stock_Picking_Save_Button.grid_remove()
            self.stock = False
            self.stockButton['state'] = tkinter.NORMAL

        if self.product == True:
            self.Pruduct_Template_Rad1.grid_remove()
            self.Pruduct_Template_Rad2.grid_remove()
            self.Pruduct_Template_Rad3.grid_remove()
            self.Pruduct_Template_Search_Box.grid_remove()
            self.Pruduct_Template_Search_Button.grid_remove()
            self.Pruduct_Template_Save_Button.grid_remove()
            self.product = False
            self.productButton['state'] = tkinter.NORMAL

        self.Purchase_Order_Rad1 = Radiobutton(self, state=DISABLED, text='Borrador', value="draft", variable=selected)
        self.Purchase_Order_Rad2 = Radiobutton(self, state=DISABLED, text='Solicitud de ppto.', value="sent", variable=selected)
        self.Purchase_Order_Rad3 = Radiobutton(self, state=DISABLED, text='Para aprobar', value="to approve", variable=selected)
        self.Purchase_Order_Rad4 = Radiobutton(self, state=DISABLED, text='Pedido de compra', value="purchase", variable=selected)
        self.Purchase_Order_Rad5 = Radiobutton(self, state=DISABLED, text='Bloqueado', value="done", variable=selected)
        self.Purchase_Order_Rad6 = Radiobutton(self, state=DISABLED, text='Cancelado', value="cancel", variable=selected)

        self.Purchase_Order_Rad1.grid(column=2, row=1)
        self.Purchase_Order_Rad2.grid(column=2, row=2)
        self.Purchase_Order_Rad3.grid(column=2, row=3)
        self.Purchase_Order_Rad4.grid(column=2, row=4)
        self.Purchase_Order_Rad5.grid(column=2, row=5)
        self.Purchase_Order_Rad5.grid(column=2, row=6)

        self.Purchase_Order_Search_Box = Entry(self, width=25)
        self.Purchase_Order_Search_Box.grid(column=2, row=0)

        self.Purchase_Order_Search_Button = Button(self, font=("Arial", 12), fg='black', text="Buscar",
                                                   highlightbackground='black',
                                                   command=lambda: self.Search_Purchase_Order(self.Purchase_Order_Search_Box.get()))
        self.Purchase_Order_Search_Button.grid(row=0, column=3, sticky="nsew")

        self.Purchase_Order_Save_Button = Button(self, state=DISABLED, font=("Arial", 12), fg='black', text="Guardar",
                                                 highlightbackground='black',
                                                 command=lambda: models.execute_kw(db, uid, password, 'purchase.order', 'write', [[int(self.document['id'])], {'state': selected.get()}]))
        self.Purchase_Order_Save_Button.grid(row=7, column=2, sticky="nsew")

    def Search_Purchase_Order(self, busqueda):
        ids = models.execute_kw(db, uid, password, 'purchase.order', 'search', [[['name', '=', busqueda]]])

        self.document = models.execute_kw(db, uid, password, 'purchase.order', 'read', [ids], {'fields': ['id']})
        print(self.document)
        self.document = self.document[-1]
        if self.document['id'] != "":
            self.Purchase_Order_Rad1['state'] = tkinter.NORMAL
            self.Purchase_Order_Rad2['state'] = tkinter.NORMAL
            self.Purchase_Order_Rad3['state'] = tkinter.NORMAL
            self.Purchase_Order_Rad4['state'] = tkinter.NORMAL
            self.Purchase_Order_Rad5['state'] = tkinter.NORMAL
            self.Purchase_Order_Rad6['state'] = tkinter.NORMAL
            self.Purchase_Order_Save_Button['state'] = tkinter.NORMAL

    def Stock_Picking(self):
        selected = StringVar()

        self.stock = True

        self.stockButton['state'] = tkinter.DISABLED

        if self.purchase == True:
            self.Purchase_Order_Rad1.grid_remove()
            self.Purchase_Order_Rad2.grid_remove()
            self.Purchase_Order_Rad3.grid_remove()
            self.Purchase_Order_Rad4.grid_remove()
            self.Purchase_Order_Rad5.grid_remove()
            self.Purchase_Order_Rad6.grid_remove()
            self.Purchase_Order_Search_Box.grid_remove()
            self.Purchase_Order_Search_Button.grid_remove()
            self.Purchase_Order_Save_Button.grid_remove()
            self.purchase = False
            self.purchaseButton['state'] = tkinter.NORMAL
        if self.product == True:
            self.Pruduct_Template_Rad1.grid_remove()
            self.Pruduct_Template_Rad2.grid_remove()
            self.Pruduct_Template_Rad3.grid_remove()
            self.Pruduct_Template_Search_Box.grid_remove()
            self.Pruduct_Template_Search_Button.grid_remove()
            self.Pruduct_Template_Save_Button.grid_remove()
            self.product = False
            self.productButton['state'] = tkinter.NORMAL

        self.Stock_Picking_Rad1 = Radiobutton(self, state=DISABLED, text='Borrador', value="draft", variable=selected)
        self.Stock_Picking_Rad2 = Radiobutton(self, state=DISABLED, text='En Espera', value="confirmed", variable=selected)
        self.Stock_Picking_Rad3 = Radiobutton(self, state=DISABLED, text='Preparado', value="assigned", variable=selected)
        self.Stock_Picking_Rad4 = Radiobutton(self, state=DISABLED, text='Hecho', value="done", variable=selected)
        self.Stock_Picking_Rad5 = Radiobutton(self, state=DISABLED, text='Cancelado', value="cancel", variable=selected)

        self.Stock_Picking_Rad1.grid(column=2, row=1)
        self.Stock_Picking_Rad2.grid(column=2, row=2)
        self.Stock_Picking_Rad3.grid(column=2, row=3)
        self.Stock_Picking_Rad4.grid(column=2, row=4)
        self.Stock_Picking_Rad5.grid(column=2, row=5)

        self.Stock_Picking_Search_Box = Entry(self, width=25)
        self.Stock_Picking_Search_Box.grid(column=2, row=0)

        self.Stock_Picking_Search_Button = Button(self, font=("Arial", 12), fg='black', text="Buscar",
                                                  highlightbackground='black',
                                                  command=lambda: self.Search_Stock_Picking(self.Stock_Picking_Search_Box.get()))
        self.Stock_Picking_Search_Button.grid(row=0, column=3, sticky="nsew")

        self.Stock_Picking_Save_Button = Button(self, state=DISABLED, font=("Arial", 12), fg='black', text="Guardar", highlightbackground='black',
                            command=lambda: models.execute_kw(db, uid, password, 'stock.picking', 'write',
                                                              [[int(self.document['id'])], {'state': selected.get()}]))
        self.Stock_Picking_Save_Button.grid(row=7, column=2, sticky="nsew")

    def Search_Stock_Picking(self, busqueda):
        ids = models.execute_kw(db, uid, password, 'stock.picking', 'search', [[['name', '=', busqueda]]])

        self.document = models.execute_kw(db, uid, password, 'stock.picking', 'read', [ids], {'fields': ['name',
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

        self.document = self.document[-1]
        print(self.document)

        if self.document['id'] != "":
            self.Stock_Picking_Rad1['state'] = tkinter.NORMAL
            self.Stock_Picking_Rad2['state'] = tkinter.NORMAL
            self.Stock_Picking_Rad3['state'] = tkinter.NORMAL
            self.Stock_Picking_Rad4['state'] = tkinter.NORMAL
            self.Stock_Picking_Rad5['state'] = tkinter.NORMAL
            self.Stock_Picking_Save_Button['state'] = tkinter.NORMAL

    def createWidgets(self):
        self.label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.stockButton.grid(row=1, column=0, sticky="nsew")

        self.purchaseButton.grid(row=2, column=0, sticky="nsew")

        self.productButton.grid(row=3, column=0, sticky="nsew")


Edit = Tk()
Edit.title("Editor De ODOO")
Edit.geometry('360x250')
Edit.resizable(False, False)
root = Editor(Edit).grid()
Edit.mainloop()
