import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk


class SignUpWind(tk.Frame):
    def __init__(self, parent, controller): 
        super().__init__(parent)
        # Setup imge for back button.
        self.img = tk.PhotoImage(file="C:/Users/joshu/Documents/VSC/python/secom/src/assets/icons/return.png")
        self.img = self.img.subsample(4,4)
        # Create label.
        self.titleLbl = ttk.Label(self,
                                  text="Crear cuenta nueva",
                                  font=tkf.Font(family="Helvetica", size=15))
        self.userLbl = ttk.Label(self,
                                 text="Usuario:",
                                 font=tkf.Font(family="Helvetica", size=10))
        self.pswdLbl = ttk.Label(self,
                                 text="Contraseña:",
                                 font=tkf.Font(family="Helvetica", size=10))
        self.pswdConfirmLbl = ttk.Label(self,
                                        text="Confirme contraseña:",
                                        font=tkf.Font(family="Helvetica", size=10))
        self.safewrdLbl = ttk.Label(self,
                                    text="Palabra salvavidas:",
                                    font=tkf.Font(family="Helvetica", size=10))
        # Creation of entries.
        self.userEty = ttk.Entry(self)
        self.pswdEty = ttk.Entry(self, show="*")
        self.pswdConfirmEty = ttk.Entry(self, show="*")
        self.safewrdEty = ttk.Entry(self)                                
        # Creation of button.
        self.backBtn = ttk.Button(self,
                                 image=self.img,
                                 command=lambda: controller.showFrame(page_name="LIWind"))
        self.CreateBtn = ttk.Button(self,
                                   width=8,
                                   text="Crear")


        # Places labels.
        self.titleLbl.grid(row=0,
                           column=0, padx=400 / 2 - 90,
                           sticky=tk.SW)
        self.userLbl.grid(row=1,
                          column=0,
                          padx=controller.widthWindow / 2 - 60,
                          sticky=tk.W)
        self.pswdLbl.grid(row=3,
                          column=0,
                          padx=controller.widthWindow / 2 - 60,
                          sticky=tk.W)
        self.pswdConfirmLbl.grid(row=5,
                                 column=0,
                                 padx=controller.widthWindow / 2 - 60,
                                 sticky=tk.W)
        self.safewrdLbl.grid(row=7,
                             column=0,
                             padx=controller.widthWindow / 2 - 60,
                             sticky=tk.W)
        # Places entries (string inputs).
        self.userEty.grid(row=2,
                          column=0,
                          padx=controller.widthWindow / 2 - 60,
                          pady=5,
                          sticky=tk.W)
        self.pswdEty.grid(row=4,
                          column=0,
                          padx=controller.widthWindow / 2 - 60,
                          pady=5,
                          sticky=tk.W)
        self.pswdConfirmEty.grid(row=6,
                                 column=0,
                                 padx=controller.widthWindow / 2 - 60,
                                 pady=5,
                                 sticky=tk.W)
        self.safewrdEty.grid(row=8,
                             column=0,
                             padx=controller.widthWindow / 2 - 60,
                             pady=5,
                             sticky=tk.W)
        # Places buttons
        self.backBtn.grid(row=0, column=0,sticky=tk.W)
        self.CreateBtn.grid(row=9, column=0, padx=100,sticky=tk.N)