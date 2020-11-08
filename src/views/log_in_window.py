import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk
from constants import static_values


class LogInWind(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        parent.config(relief="groove")
        controller.set_wind_size(
            width=static_values.LIWIND_WIDTH,
            height=static_values.LIWIND_HEIGHT
        )
        controller.set_wind_param()
        
        # Creation of labels.
        self.title_lbl = ttk.Label(self,
                                 text="Iniciar Secion",
                                 font=tkf.Font(family="Helvetica", size=15))
        self.user_lbl = ttk.Label(self,
                                text="Usuario:",
                                font=tkf.Font(family="Helvetica", size=10))
        self.pswd_lbl = ttk.Label(self,
                                text="Contraseña:",
                                font=tkf.Font(family="Helvetica", size=10))
        # Creation of entries.
        self.user_ety = ttk.Entry(self)   
        self.pswd_ety = ttk.Entry(self, show="*")
        # Creation of buttons.
        self.logIn_btn = ttk.Button(self,
                                  width=15,
                                  text="Iniciar Sesion")
        self.signUp_btn = ttk.Button(self,
                                    width=15,
                                    text="Crear cuenta",
                                    command=lambda: controller._show_view("SUWind"))
        

        # Places labels.
        self.title_lbl.grid(row=0,
                           column=0,
                           padx=400 / 2 - 60,
                           pady=10,
                           sticky=tk.SW)
        self.user_lbl.grid(row=1,
                          column=0,
                          padx=controller.get_width_window() / 2 - 60,
                          sticky=tk.SW)
        self.pswd_lbl.grid(row=3,
                          column=0,
                          padx=controller.get_width_window() / 2 - 60,
                          sticky=tk.W)
        # Places entries (string inputs).
        self.user_ety.grid(row=2,
                          column=0,
                          padx=controller.get_width_window() / 2 - 60,
                          pady=5)
        self.pswd_ety.grid(row=4,
                          column=0,
                          padx=controller.get_width_window() / 2 - 60,
                          pady=5)
        # # Places buttons
        self.logIn_btn.grid(row=5,column=0, pady=5, sticky=tk.N)
        self.signUp_btn.grid(row=6, column=0, pady=5 ,sticky=tk.S)