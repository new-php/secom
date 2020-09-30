import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk


class LogInWind(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        # Creation of labels.
        self.titleLbl = ttk.Label(self,
                                 text="Iniciar Secion",
                                 font=tkf.Font(family="Helvetica", size=15))
        self.userLbl = ttk.Label(self,
                                text="Usuario:",
                                font=tkf.Font(family="Helvetica", size=10))
        self.pswdLbl = ttk.Label(self,
                                text="Contraseña:",
                                font=tkf.Font(family="Helvetica", size=10))
        # Creation of entries.
        self.userEty = ttk.Entry(self)   
        self.pswdEty = ttk.Entry(self, show="*")
        # Creation of buttons.
        self.logInBtn = ttk.Button(self,
                                  width=15,
                                  text="Iniciar Sesion")
        self.signUpBtn = ttk.Button(self,
                                    width=15,
                                    text="Crear cuenta",
                                    command=lambda: controller.showFrame(page_name="SUWind"))
        controller.setWindParam()

        # Places labels.
        self.titleLbl.grid(row=0,
                           column=0,
                           padx=400 / 2 - 60,
                           pady=10,sticky=tk.SW)
        self.userLbl.grid(row=1,
                          column=0,
                          padx=controller.widthWindow / 2 - 60,
                          sticky=tk.SW)
        self.pswdLbl.grid(row=3,
                          column=0,
                          padx=controller.widthWindow / 2 - 60,
                          sticky=tk.W)
        # Places entries (string inputs).
        self.userEty.grid(row=2,
                          column=0,
                          padx=controller.widthWindow / 2 - 60,
                          pady=5)
        self.pswdEty.grid(row=4,
                          column=0,
                          padx=controller.widthWindow / 2 - 60,
                          pady=5)
        # # Places buttons
        self.logInBtn.grid(row=5,column=0, pady=5, sticky=tk.N)
        self.signUpBtn.grid(row=6, column=0, pady=5 ,sticky=tk.S)