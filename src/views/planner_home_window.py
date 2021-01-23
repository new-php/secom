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
            sticky=tk.S
        )


    #--------------------------------BUTTONS--------------------------------



        self.new_project_btn = ttk.Button(
                self,
                width=15,
                text="Crear Proyecto",
                #command=
        )
        self.new_project_btn.grid(row=1,column=0, sticky=tk.S)