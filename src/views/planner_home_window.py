import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk
from constants import static_values as sv

class PlannerHomeWind(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)

    #---------------------------------FRAMES------------------------------------
    
        title_frame = ttk.Frame(self, relief=tk.RIDGE)
        title_frame.pack(side=tk.TOP, expand=True)

        menu_frame = ttk.Frame(self, relief=tk.RIDGE)
        menu_frame.pack(side=tk.BOTTOM, expand=True)
    #--------------------------------LABELS-------------------------------------
        self.title_lbl = ttk.Label(
            title_frame,
            text="Gestor de proyectos",
            font=tkf.Font(family="Helvetica", size=15)
        )
        self.title_lbl.grid(
            row=0,
            column=0,
            sticky=tk.N,
            pady=(0,25),
            padx=0
        )

        user_name = controller.connector.get(
            ("first_name","second_name","f_last_name","m_last_name"),
            controller.logged_user
        )
        
            
        self.user_info_lbl = ttk.Label(
            title_frame,
            text="Usuario:" + ' '.join(user_name),
            font=tkf.Font(family="Helvetica", size=10)
        )
        self.user_info_lbl.grid(
            row=0,
            column=1,
            sticky=tk.NE,
            pady=(0,25),
            padx=(300,0)
        )
    #--------------------------------BUTTONS--------------------------------

        self.new_project_btn = tk.Button(
                menu_frame,
                heigh=4,
                width=12,
                text="Crear Proyecto",
                #command=
        )
        self.new_project_btn.grid(row=1,column=0, sticky=tk.S)