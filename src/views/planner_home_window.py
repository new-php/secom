import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk
from constants import static_values as sv

class PlannerHomeWind(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)

    #--------------------------------LABELS---------------------------------    
        self.title_lbl = ttk.Label(
            self,
            text="Gestor de proyectos",
            font=tkf.Font(family="Helvetica", size=15)
        )
        self.title_lbl.grid(
            row=0,
            column=0,
            sticky=tk.N,
            pady=(5,25)
        )

        user_name = controller.connector.get("first_name",controller.logged_user)
        # user_name += " " + controller.connector.get("second_name",controller.logged_user)
        # user_name += " " + controller.connector.get("f_last_name",controller.logged_user)
        # user_name += " " + controller.connector.get("m_last_name",controller.logged_user)

        self.user_info_lbl = ttk.Label(
            self,
            text=user_name,
            font=tkf.Font(family="Helvetica", size=15)
        )
        self.user_info_lbl.grid(
            row=0,
            column=1,
            sticky=tk.N,
            pady=(5,25)
        )
    #--------------------------------BUTTONS--------------------------------

        self.new_project_btn = ttk.Button(
                self,
                width=15,
                text="Crear Proyecto",
                #command=
        )
        self.new_project_btn.grid(row=1,column=0, sticky=tk.S)