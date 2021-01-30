import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk
from constants import static_values as sv
from datetime import datetime

class WareHomeWind(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
         #---------------------------------FRAMES------------------------------------
    
        title_frame = ttk.Frame(self, relief=tk.RIDGE)
        title_frame.pack(side=tk.TOP, expand=True)

        menu_frame = ttk.Frame(self, relief=tk.RIDGE)
        menu_frame.pack(side=tk.BOTTOM, expand=True)

        #--------------------------------LABELS-------------------------------------
        self.title_lbl = ttk.Label(
            title_frame,
            text="Control de materiales",
            font=tkf.Font(family="Helvetica", size=15)
        )
        self.title_lbl.grid(
            row=0,
            column=0,
            sticky=tk.N,
            pady=(0,25),
            padx=0
        )

        user_name = controller.connector.get(
            ("first_name","second_name","f_last_name","m_last_name"),
            controller.logged_user
        )

        self.user_info_lbl = ttk.Label(
            title_frame,
            text="Usuario:" + ' '.join(user_name),
            font=tkf.Font(family="Helvetica", size=10)
        )
        self.user_info_lbl.grid(
            row=0,
            column=1,
            sticky=tk.NE,
            pady=(0,25),
            padx=(300,0)
        )

        self.material_lbl = ttk.Label(
            menu_frame,
            text="Material: ",
            font=tkf.Font(family="Helvetica", size=15)
        )
        self.material_lbl.grid(
            row=1,
            column=0,
            sticky=tk.N,
            pady=(0,10),
            padx=0
        )

        self.quantity_lbl = ttk.Label(
            menu_frame,
            text="Unidades: ",
            font=tkf.Font(family="Helvetica", size=15)
        )
        self.quantity_lbl.grid(
            row=2,
            column=0,
            sticky=tk.N,
            pady=(0,10),
            padx=0
        )
        
        #Get time in order to register when the transaction takes place

        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        print(formatted_date)

        #--------------------------------COMBOBOX   --------------------------------
        self.material_value = tk.StringVar()
        material_value_cbx = ttk.Combobox(
            menu_frame,
            foreground=sv.WHITE,
            state="readonly",
            textvariable=self.material_value
        )
        
        material_value_cbx['values'] = [option for option in sv.MATERIALS]
        material_value_cbx.grid(row=1, column=1, sticky=tk.N)
        material_value_cbx.current(0)

        #--------------------------------BUTTONS--------------------------------

        self.add_material_btn = tk.Button(
                menu_frame,
                heigh=4,
                width=20,
                text="Ingreso de material",
                #command=
        )
        self.add_material_btn.grid(
            row=3,
            column=0, 
            sticky=tk.S,
            pady=(5,5),
            padx=(0,0)
        )

        self.delete_material_btn = tk.Button(
                menu_frame,
                heigh=4,
                width=20,
                text="Egreso de material"
                #command=
        )
        self.delete_material_btn.grid(
            row=3,
            column=2,
            sticky=tk.S,
            pady=(5,5),
            padx=(250,0)
        )

    #def materal_transaction(self,controller):

