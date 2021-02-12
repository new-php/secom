import tkinter as tk
from tkinter.constants import NSEW
import tkinter.font as tkf
from tkinter import Widget, ttk
from constants import static_values as sv
from services import validate

class PlannerHomeWind(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)

        #---------------------------------FRAMES------------------------------------
    
        title_frame = ttk.Frame(self, relief=tk.RIDGE)
        title_frame.pack(side=tk.TOP, expand=True)

        self.menu_frame = ttk.Frame(self, relief=tk.RIDGE)
        self.menu_frame.pack(side=tk.BOTTOM, expand=True)

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
            controller.logged_user,
            "first_name",
            "second_name",
            "f_last_name",
            "m_last_name"
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

        self.menu_lbl = ttk.Label(
            self.menu_frame,
            text="Proyectos Activos",
            font=tkf.Font(family="Helvetica", size=15)
        )

        self.menu_lbl.grid(
            row=1,
            column=0,
            sticky=tk.N,
            pady=(25,25),
            padx=(0,0)
        )
        
        #--------------------------------BUTTONS--------------------------------

        self.new_project_btn = tk.Button(
                self.menu_frame,
                heigh=3,
                width=12,
                text="Crear Proyecto",
                command=lambda: self._create_project_popup(controller)
        )
        self.new_project_btn.grid(
            row=0,
            column=0, 
            sticky=tk.S,
            pady=(5,5),
            padx=(0,0)
        )

        self.delete_project_btn = tk.Button(
                self.menu_frame,
                heigh=3,
                width=20,
                text="Eliminar(Exportar) Proyecto"
                #command=
        )
        self.delete_project_btn.grid(
            row=0,
            column=2,
            sticky=tk.S,
            pady=(5,5),
            padx=(300,0)
        )

        #-----------------------------Treeview----------------------------------
        self.projects_tree = ttk.Treeview(
            self.menu_frame,
            height=20,
            columns=[column[0] for column in sv.PROYECT_COLUMNS]
        )

        self.projects_tree.column("#0", width=10)
        for column in sv.PROYECT_COLUMNS:
            column_id, column_name = column[0], column[1]

            self.projects_tree.heading(column_id, text=column_name)
            self.projects_tree.column(
                column_id,
                minwidth=5 * len(column_name)
            )
        self._update_project_tree()
        self.projects_tree.grid(row=2,column=0)


    def _update_project_tree(self):
        pass


    @staticmethod
    def _create_project_popup(controller):
        popup = tk.Toplevel()
        popup.withdraw()
        popup.title("SECOM")
        controller.refresh_window('CPPopup', top_view=popup)

        wdgts = {
            'frm': {
                'title': ttk.Frame(popup),
                'info': ttk.Frame(popup)
            }
        }
        wdgts['lbl'] = {
            'title':ttk.Label(
                wdgts['frm']['title'],
                text='Crear Proyecto nuevo',
                font=tkf.Font(family=sv.FONT, size=sv.TITLE_FONT_SIZE)
            ),
            'prj_name': ttk.Label(
                wdgts['frm']['info'],
                text='Nombre:',
                font=tkf.Font(family=sv.FONT, size=sv.NORMAL_FONT_SIZE)
            ),
   
            'recipient': ttk.Label(
                wdgts['frm']['info'],
                text='Cliente:',
                font=tkf.Font(family=sv.FONT, size=sv.NORMAL_FONT_SIZE)
            ),
            'start_date':ttk.Label(
                wdgts['frm']['info'],
                text='Fecha inicio (Opcional):',
                font=tkf.Font(family=sv.FONT, size=sv.NORMAL_FONT_SIZE)
            ),
            'end_date':ttk.Label(
                wdgts['frm']['info'],
                text='Fecha cierre (Opcinal):',
                font=tkf.Font(family=sv.FONT, size=sv.NORMAL_FONT_SIZE)
            ),
            'addr':ttk.Label(
                wdgts['frm']['info'],
                text='Direccion:',
                font=tkf.Font(family=sv.FONT, size=sv.NORMAL_FONT_SIZE)
            ), 
        }
        wdgts['ety'] = {
            'prj_name':ttk.Entry(
                wdgts['frm']['info'],
                validate='key',
                validatecommand=(
                    popup.register(validate.contains_char),
                    '%P',
                    'ltrs',
                    'space'
                )
            ), 
            'recipient':ttk.Entry(
                wdgts['frm']['info'],
                validate='key',
                validatecommand=(
                    popup.register(validate.contains_char),
                    '%P',
                    'ltrs',
                    'space'
                )
            ),
            'start_date':ttk.Entry(
                wdgts['frm']['info'],
                validate='key',
                validatecommand=(
                    popup.register(validate.contains_char),
                    '%P',
                    'dgts',
                )
            ), 
            'end_date':ttk.Entry(
                wdgts['frm']['info'],
                validate='key',
                validatecommand=(
                    popup.register(validate.contains_char),
                    '%P',
                    'dgts',
                    'frd slash'
                )
            ),
            'addr':ttk.Entry(
                wdgts['frm']['info'],
                validate='key',
                validatecommand=(
                    popup.register(validate.contains_char),
                    '%P',
                    'ltr',
                    'dgts',
                    'space',
                )
            ) 
        }
        wdgts['btn'] = {
            'create':ttk.Button(
                wdgts['frm']['info'],
                text='Crear',
                width=10,
                command=lambda: controller.connector.insert_into(
                    'project',
                    wdgts['ety']['prj_name'].get(),
                    wdgts['ety']['recipient'].get(),
                    wdgts['ety']['start_date'].get(),
                    wdgts['ety']['end_date'].get(),
                    wdgts['ety']['addr'].get()

                )
            )
        }

        #--------------------------------Frames---------------------------------
        wdgts['frm']['title'].grid(row=0, column=0, padx=(12,0), pady=(15,20))
        wdgts['frm']['info'].grid(row=1, column=0, padx=(15, 0))

        #--------------------------------Lables---------------------------------
        placer = 0
        for widget in wdgts['lbl'].values():
            if widget.master == wdgts['frm']['info']:
                widget.grid(row=placer, column=0, sticky=tk.W)
                placer += 2
            else:
               widget.grid(row=0,column=0, sticky=tk.NSEW)

     
        #-----------------------------Entry-------------------------------------
        placer = 1
        popup.update_idletasks()
        for name, widget in wdgts['ety'].items():
            widget.grid(row=placer, column=0, pady=(0, 13))
            placer += 2
            
        
        #-------------------------------------Button----------------------------
        wdgts['btn']['create'].grid(row=placer,column=0, sticky=tk.NSEW)


        popup.deiconify()