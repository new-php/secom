import tkinter as tk
import tkinter.font as tkf
from .root import Root


class SignUpWind(tk.Frame):
    def __init__(self, parent, controller): 
        super().__init__(parent, controller)
        # Setup imge for back button.
        self.img = tk.PhotoImage(file="C:/Users/joshu/Documents/VSC/python/secom/icons/return.png")
        self.img = self.img.subsample(4,4)
        # Create label.
        self.titleLbl = tk.Label(self,
                                 text="Crear cuenta nueva",
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
        self.pswdConfirmLbl = tk.Label(self,
                                 text="Cormirma Contraseña:",
                                 font=tkf.Font(family="Helvetica", size=10, weight="bold"),
                                 bg="#E0E0E0")
        # Creation of entries.
        self.userEty = tk.Entry(self)
        self.pswdEty = tk.Entry(self, show="*")
        self.pswdConfirmEty = tk.Entry(self, show="*")                                 
        # Creation of button.
        self.backBtn = tk.Button(self,
                                 image=self.img,
                                 command=lambda: controller.showFrame(LIWind))
        self.CreateBtn = tk.Button(self,
                                   width=8,
                                   text="Crear",
                                   font=tkf.Font(family="Helvetica", size=10, weight="bold"),
                                   bg="#0080FF",
                                   ############################ ADD COMAND
                                   fg="#fff")


        # Places labels.
        self.titleLbl.grid(row=0, column=0, padx=400 / 2 - 90, sticky=tk.SW)
        self.userLbl.grid(row=1, column=0, padx=parent.width_window / 2 - 60, sticky=tk.W)
        self.pswdLbl.grid(row=3, column=0, padx=parent.width_window / 2 - 60, sticky=tk.W)
        self.pswdConfirmLbl.grid(row=5, column=0, padx=parent.width_window / 2 - 60, sticky=tk.W)
        # Places entries (string inputs).
        self.userEty.grid(row=2, column=0, padx=parent.width_window / 2 - 60, pady=5, sticky=tk.W)
        self.pswdEty.grid(row=4, column=0, padx=parent.width_window / 2 - 60, pady=5, sticky=tk.W)
        self.pswdConfirmEty.grid(row=6, column=0, padx=parent.width_window / 2 - 60, pady=5, sticky=tk.W)
        # Places buttons
        self.backBtn.grid(row=0, column=0,sticky=tk.W)
        self.CreateBtn.grid(row=7, column=0, padx=100,sticky=tk.N)