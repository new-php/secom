import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk


class SignUpWind(tk.Frame):
    def __init__(self, parent, controller): 
        super().__init__(parent)

        controller.set_wind_size(400, 300)

        # Setup imge for back button.
        self.img = tk.PhotoImage(file="C:/Users/joshu/Documents/VSC/python/secom/src/assets/icons/return.png")
        self.img = self.img.subsample(4,4)
        # Create label.
        self.title_lbl = ttk.Label(self,
                                  text="Crear cuenta nueva",
                                  font=tkf.Font(family="Helvetica", size=15))
        self.user_lbl = ttk.Label(self,
                                 text="Usuario:",
                                 font=tkf.Font(family="Helvetica", size=10))
        self.pswd_lbl = ttk.Label(self,
                                 text="Contraseña:",
                                 font=tkf.Font(family="Helvetica", size=10))
        self.pswdConfirm_lbl = ttk.Label(self,
                                        text="Confirme contraseña:",
                                        font=tkf.Font(family="Helvetica", size=10))
        self.safewrd_lbl = ttk.Label(self,
                                    text="Palabra salvavidas:",
                                    font=tkf.Font(family="Helvetica", size=10))
        # Creation of entries.
        self.user_ety = ttk.Entry(self)
        self.pswd_ety = ttk.Entry(self, show="*")
        self.pswdConfirm_ety = ttk.Entry(self, show="*")
        self.safewrd_ety = ttk.Entry(self)                                
        # Creation of button.
        self.back_btn = ttk.Button(self,
                                 image=self.img,
                                 command=lambda: controller.show_frame("LIWind"))
        self.Create_btn = ttk.Button(self,
                                   width=8,
                                   text="Crear")


        # Places labels.
        self.title_lbl.grid(row=0,
                           column=0, padx=400 / 2 - 90,
                           sticky=tk.SW)
        self.user_lbl.grid(row=1,
                          column=0,
                          padx=controller.get_width_window() / 2 - 60,
                          sticky=tk.W)
        self.pswd_lbl.grid(row=3,
                          column=0,
                          padx=controller.get_width_window() / 2 - 60,
                          sticky=tk.W)
        self.pswdConfirm_lbl.grid(row=5,
                                 column=0,
                                 padx=controller.get_width_window() / 2 - 60,
                                 sticky=tk.W)
        self.safewrd_lbl.grid(row=7,
                             column=0,
                             padx=controller.get_width_window() / 2 - 60,
                             sticky=tk.W)
        # Places entries (string inputs).
        self.user_ety.grid(row=2,
                          column=0,
                          padx=controller.get_width_window() / 2 - 60,
                          pady=5,
                          sticky=tk.W)
        self.pswd_ety.grid(row=4,
                          column=0,
                          padx=controller.get_width_window() / 2 - 60,
                          pady=5,
                          sticky=tk.W)
        self.pswdConfirm_ety.grid(row=6,
                                 column=0,
                                 padx=controller.get_width_window() / 2 - 60,
                                 pady=5,
                                 sticky=tk.W)
        self.safewrd_ety.grid(row=8,
                             column=0,
                             padx=controller.get_width_window() / 2 - 60,
                             pady=5,
                             sticky=tk.W)
        # Places buttons
        self.back_btn.grid(row=0, column=0,sticky=tk.W)
        self.Create_btn.grid(row=9, column=0, padx=100,sticky=tk.N)