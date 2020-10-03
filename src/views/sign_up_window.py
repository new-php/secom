import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk


class SignUpWind(ttk.Frame):
    def __init__(self, parent, controller): 
        super().__init__(parent)

        controller.set_wind_size(400, 400)

        # Create label.
        title_lbl = ttk.Label(self,
                                  text="Crear cuenta nueva",
                                  font=tkf.Font(family="Helvetica", size=15))
        first_name_lbl = ttk.Label(self,
                                    text="Nombre:",
                                    font=tkf.Font(family="Helvetica", size=10))
        second_name_lbl = ttk.Label(self,
                                    text="Segundo nombre:",
                                    font=tkf.Font(family="Helvetica", size=10))
        f_last_name_lbl = ttk.Label(self,
                                    text="Apellido paterno:",
                                    font=tkf.Font(family="Helvetica", size=10))
        m_last_name_lbl = ttk.Label(self,
                                    text="Apellido materno:",
                                    font=tkf.Font(family="Helvetica", size=10))
        user_lbl = ttk.Label(self,
                                 text="Usuario:",
                                 font=tkf.Font(family="Helvetica", size=10))
        pswd_lbl = ttk.Label(self,
                                 text="Contraseña:",
                                 font=tkf.Font(family="Helvetica", size=10))
        pswd_confirm_lbl = ttk.Label(self,
                                        text="Confirme contraseña:",
                                        font=tkf.Font(family="Helvetica", size=10))
        safewrd_lbl = ttk.Label(self,
                                    text="Palabra salvavidas:",
                                    font=tkf.Font(family="Helvetica", size=10))
        acc_type_lbl = ttk.Label(self,
                                 text="Tipo de cuenta:",
                                 font=tkf.Font(family="Helvetica", size=10))
        # Creation of entries.
        self.first_name_ety = ttk.Entry(self)
        self.second_name_ety = ttk.Entry(self)
        self.f_last_name_ety = ttk.Entry(self)
        self.m_last_name_ety = ttk.Entry(self)
        self.user_ety = ttk.Entry(self)
        self.pswd_ety = ttk.Entry(self, show="*")
        self.pswd_confirm_ety = ttk.Entry(self, show="*")
        self.hint_ety = ttk.Entry(self)
        #Creation of cobobox.
        self.acc_type_value = tk.StringVar()
        acc_type_cbx = ttk.Combobox(self,
                                         textvariable=self.acc_type_value)
        acc_type_cbx['values'] = ("Planeacion", "Almlacen")
        # Creation of button.
        back_btn = ttk.Button(self,
                              width=15,  
                              text="Cancelar",
                              command=lambda: controller.show_view("LIWind"))
        create_btn = ttk.Button(self,
                                width=15,
                                text="Crear",
                                command=self.send_info)


        # Places labels.
        title_lbl.grid(row=0,
                           column=1,
                           padx=120,
                           pady=10,
                           sticky=tk.NSEW)
        first_name_lbl.grid(row=1,
                            column=1,
                            padx=70,
                            sticky=tk.W)
        second_name_lbl.grid(row=3,
                            column=1,
                            padx=70,
                            sticky=tk.W)
        f_last_name_lbl.grid(row=5,
                            column=1,
                            padx=71,
                            sticky=tk.W)
        m_last_name_lbl.grid(row=7,
                            column=1,
                            padx=71,
                            sticky=tk.W)
        user_lbl.grid(row=1,
                          column=1,
                          padx=145,
                          sticky=tk.E)
        pswd_lbl.grid(row=3,
                          column=1,
                          padx=120,
                          sticky=tk.E)
        pswd_confirm_lbl.grid(row=5,
                                 column=1,
                                 padx=70,
                                 sticky=tk.E)
        safewrd_lbl.grid(row=7,
                             column=1,
                             padx=80,
                             sticky=tk.E)
        acc_type_lbl.grid(row=9,
                          column=1,
                          pady=5,
                          sticky=tk.NS)
        # Places entries (string inputs).
        self.first_name_ety.grid(row=2,
                          column=1,
                          padx=70,
                          pady=5,
                          sticky=tk.W)
        self.second_name_ety.grid(row=4,
                          column=1,
                          padx=70,
                          pady=5,
                          sticky=tk.W)
        self.f_last_name_ety.grid(row=6,
                          column=1,
                          padx=70,
                          pady=5,
                          sticky=tk.W)
        self.m_last_name_ety.grid(row=8,
                          column=1,
                          padx=70,
                          pady=5,
                          sticky=tk.W)
        self.user_ety.grid(row=2,
                          column=1,
                          padx=70,
                          pady=5,
                          sticky=tk.E)
        self.pswd_ety.grid(row=4,
                          column=1,
                          padx=70,
                          pady=5,
                          sticky=tk.E)
        self.pswd_confirm_ety.grid(row=6,
                                 column=1,
                                 padx=70,
                                 pady=5,
                                 sticky=tk.E)
        self.hint_ety.grid(row=8,
                             column=1,
                             padx=70,
                             pady=5,
                             sticky=tk.E)
        # Palcing combobox.
        acc_type_cbx.grid(row=10,
                          column=1,
                          pady=5,
                          sticky=tk.NS)
        acc_type_cbx.current(0)
        # Places buttons
        back_btn.grid(row=12, 
                           column=1,
                           padx=40,
                           pady=5,
                           sticky=tk.NS)
        create_btn.grid(row=11,
                             column=1,
                             padx=40,
                             pady=5,
                             sticky=tk.NS)


    def send_info(self):
        pass