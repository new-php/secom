import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk, messagebox
from constants import static_values as sv


class LogInWind(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        #General view settings.
        parent.config(relief="groove")
        
        #--------------------------------LABELS---------------------------------
        self.title_lbl = ttk.Label(
            self,
            text="Iniciar Secion",
            font=tkf.Font(family="Helvetica", size=15)
        )
        self.title_lbl.grid(
            row=0,
            column=0,
            sticky=tk.SW
        )

        self.user_lbl = ttk.Label(
            self,
            text="Usuario:",
            font=tkf.Font(family="Helvetica", size=10)
        )
        self.user_lbl.grid(
            row=1,
            column=0,
            sticky=tk.SW
        )

        self.pswd_lbl = ttk.Label(
            self,
            text="Contraseña:",
            font=tkf.Font(family="Helvetica", size=10)
        )
        self.pswd_lbl.grid(
            row=3,
            column=0,
            sticky=tk.SW
        )
        
        #--------------------------------ENTRIES--------------------------------
        self.user_ety = ttk.Entry(self)   
        self.user_ety.grid(
            row=2,
            column=0,
            pady=5
        )

        self.pswd_ety = ttk.Entry(self, show="•")
        self.pswd_ety.grid(
            row=4,
            column=0,
            pady=5
        )

        #--------------------------------BUTTONS--------------------------------
        self.logIn_btn = ttk.Button(
            self,
            width=15,
            text="Iniciar Sesion",
            command=lambda: self.login(controller)
        )
        self.logIn_btn.grid(row=5,column=0, pady=5, sticky=tk.N)
        
        self.signUp_btn = ttk.Button(
            self,
            width=15,
            text="Crear cuenta",
            command=lambda: controller.refresh_window("SUWind")
        )
        self.signUp_btn.grid(row=6, column=0, pady=5 ,sticky=tk.S)

        # Upadte Idle tasks to get widget's width for good placement
        controller.update_idletasks()
        self.title_lbl.grid(
            padx=(sv.WIND_SIZE["LIWind"][0] - self.title_lbl.winfo_width()) / 2,
            pady=(10,20)
        )
        self.user_lbl.grid(
            padx=(sv.WIND_SIZE["LIWind"][0] - self.user_ety.winfo_width()) / 2
        )
        self.pswd_lbl.grid(
            padx=(sv.WIND_SIZE["LIWind"][0] - self.pswd_ety.winfo_width()) / 2
        )
        self.user_ety.grid(
            padx=(sv.WIND_SIZE["LIWind"][0] - self.user_ety.winfo_width()) / 2
        )
        self.pswd_ety.grid(
            padx=(sv.WIND_SIZE["LIWind"][0] - self.pswd_ety.winfo_width()) / 2
        )
        self.logIn_btn.grid(
            padx=(sv.WIND_SIZE["LIWind"][0] - self.logIn_btn.winfo_width()) / 2
        )
        self.signUp_btn.grid(
            padx=(sv.WIND_SIZE["LIWind"][0] - self.signUp_btn.winfo_width()) / 2 
        )

    def login(self, controller):
        """
        INPUT: root object.
        OUTPUT: none.

        DESCRIPTION: Verifies credentials and displays next screen.

        EXEPTIONS HANDLED FROM: messenger.py `get()`
        """

        try:
            if controller.connector.check_credentials(self.user_ety.get(), self.pswd_ety.get()):
                controller.logged_user = self.user_ety.get()

                controller.logged_user_type = controller.connector.get(("user_type"),
                                              controller.logged_user
                                                )
                                                
                controller.refresh_window("PHWind", delete="LIWind")

            else:
                messagebox.showerror(
                    "Credenciales invalidas",
                    "Usuario o contraseña incorrecta"
                )
                
                self.user_ety.delete(0, "end")
                self.pswd_ety.delete(0, "end")
        except ValueError:
            self.user_ety.delete(0, "end")
            self.pswd_ety.delete(0, "end")

            messagebox.showerror(
                    "Credenciales invalidas",
                    "El usuario no existe"
                )