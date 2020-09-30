import tkinter as tk
import tkinter.font as tkf
from .log_in_window import LogInWind as LIWind


class LogInWind(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        # Creation of labels.
        self.titleLbl = tk.Label(self,
                                 text="Iniciar Secion",
                                 font=tkf.Font(family="Helvetica", size=15, weight="bold"),
                                 bg="#E0E0E0")
        self.userLbl = tk.Label(self,
                                text="Usuario:",
                                font=tkf.Font(family="Helvetica", size=10, weight="bold"),
                                bg="#E0E0E0")
        self.pswdLbl = tk.Label(self,
                                text="Contraseña:",
                                font=tkf.Font(family="Helvetica", size=10, weight="bold"),
                                bg="#E0E0E0")
        # Creation of entries.
        self.userEty = tk.Entry(self)   
        self.pswdEty = tk.Entry(self, show="*")
        # Creation of buttons.
        self.logInBtn = tk.Button(self,
                                  width=15,
                                  text="Iniciar Sesion",
                                  font=tkf.Font(family="Helvetica", size=10, weight="bold"),
                                  bg="#0080FF",
                                  ################################### ADD COMMAND
                                  fg="#fff")
        self.signUpBtn  = tk.Button(self,
                                    width=15,
                                    text="Crear cuenta",
                                    font=tkf.Font(family="Helvetica", size=10, weight="bold"),
                                    bg="#0080FF",
                                    command=lambda: controller.showFrame(SUWind),
                                    fg="#fff")

        # Places labels.
        self.titleLbl.grid(row=0,
                           column=0,
                           padx=400 / 2 - 60,
                           pady=10,sticky=tk.SW)
        self.userLbl.grid(row=1,
                          column=0,
                          padx=parent.width_window / 2 - 60,
                          sticky=tk.SW)
        self.pswdLbl.grid(row=3,
                          column=0,
                          padx=parent.width_window / 2 - 60,
                          sticky=tk.W)
        # Places entries (string inputs).
        self.userEty.grid(row=2,
                          column=0,
                          padx=parent.width_window / 2 - 60,
                          pady=5)
        self.pswdEty.grid(row=4,
                          column=0,
                          padx=parent.width_window / 2 - 60,
                          pady=5)
        # # Places buttons
        self.logInBtn.grid(row=5,column=0, sticky=tk.N)
        self.signUpBtn.grid(row=6, column=0, sticky=tk.S, pady=10)