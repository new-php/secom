import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk


class SignUpWind(tk.Frame):
    def __init__(self, parent, controller): 
        super().__init__(parent)

        controller.set_wind_size(400, 300)

        # Create label.
        self.title_lbl = ttk.Label(self,
                                  text="Crear cuenta nueva",
                                  font=tkf.Font(family="Helvetica", size=15))
        self.first_name_lbl = ttk.Label(self,
                                    text="Nombre:",
                                    font=tkf.Font(family="Helvetica", size=10))
        self.second_name_lbl = ttk.Label(self,
                                    text="Segundo nombre:",
                                    font=tkf.Font(family="Helvetica", size=10))
        self.f_last_name_lbl = ttk.Label(self,
                                    text="Apellido paterno:",
                                    font=tkf.Font(family="Helvetica", size=10))
        self.m_last_name_lbl = ttk.Label(self,
                                    text="Apellido materno:",
                                    font=tkf.Font(family="Helvetica", size=10))
        self.user_lbl = ttk.Label(self,
                                 text="Usuario:",
                                 font=tkf.Font(family="Helvetica", size=10))
        self.pswd_lbl = ttk.Label(self,
                                 text="Contraseña:",
                                 font=tkf.Font(family="Helvetica", size=10))
        self.pswd_confirm_lbl = ttk.Label(self,
                                        text="Confirme contraseña:",
                                        font=tkf.Font(family="Helvetica", size=10))
        self.safewrd_lbl = ttk.Label(self,
                                    text="Palabra salvavidas:",
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
        # Creation of button.
        self.back_btn = ttk.Button(self,
                                 text="Regresar",
                                 command=lambda: controller.show_frame("LIWind"))
        self.create_btn = ttk.Button(self,
                                     width=8,
                                     text="Crear",
                                     command=self.send_info)


        # Places labels.
        self.title_lbl.grid(row=0,
                           column=1,
                           padx=40,
                           sticky=tk.NSEW)
        self.first_name_lbl.grid(row=1,
                            column=1,
                            #padx=90,
                            sticky=tk.W)
        self.second_name_lbl.grid(row=3,
                            column=1,
                            #padx=70,
                            sticky=tk.W)
        self.f_last_name_lbl.grid(row=5,
                            column=1,
                            #padx=70,
                            sticky=tk.W)
        self.m_last_name_lbl.grid(row=7,
                            column=1,
                            #padx=70,
                            sticky=tk.W)
        self.user_lbl.grid(row=1,
                          column=1,
                          padx=75,
                          sticky=tk.E)
        self.pswd_lbl.grid(row=3,
                          column=1,
                          padx=55,
                          sticky=tk.E)
        self.pswd_confirm_lbl.grid(row=5,
                                 column=1,
                                 padx=2,
                                 sticky=tk.E)
        self.safewrd_lbl.grid(row=7,
                             column=1,
                             padx=13,
                             sticky=tk.E)
        # Places entries (string inputs).
        self.first_name_ety.grid(row=2,
                          column=1,
                          #padx=50,
                          pady=5,
                          sticky=tk.W)
        self.second_name_ety.grid(row=4,
                          column=1,
                          #padx=50,
                          pady=5,
                          sticky=tk.W)
        self.f_last_name_ety.grid(row=6,
                          column=1,
                          #padx=50,
                          pady=5,
                          sticky=tk.W)
        self.m_last_name_ety.grid(row=8,
                          column=1,
                          #padx=50,
                          pady=5,
                          sticky=tk.W)
        self.user_ety.grid(row=2,
                          column=1,
                          #padx=controller.get_width_window() / 2 - 60,
                          pady=5,
                          sticky=tk.E)
        self.pswd_ety.grid(row=4,
                          column=1,
                          #padx=controller.get_width_window() / 2 - 60,
                          pady=5,
                          sticky=tk.E)
        self.pswd_confirm_ety.grid(row=6,
                                 column=1,
                                 #padx=controller.get_width_window() / 2 - 60,
                                 pady=5,
                                 sticky=tk.E)
        self.hint_ety.grid(row=8,
                             column=1,
                             #padx=controller.get_width_window() / 2 - 60,
                             pady=5,
                             sticky=tk.E)
        # Places buttons
        self.back_btn.grid(row=10, column=1, padx=40, pady=5,sticky=tk.NSEW)
        self.create_btn.grid(row=9, column=1, padx=40, pady=5, sticky=tk.NSEW)


    def send_info(self):
        pass