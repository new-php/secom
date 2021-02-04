import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk
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

        #--------------------------------Frames---------------------------------
        title_frm = ttk.Frame(popup, width=20, height=20)
        title_frm.pack(side='top', expand=True)
        # title_frm.grid(row=0,column=0)

        info_frm = ttk.Frame(popup)
        info_frm.pack(side='top', expand=True)

        #--------------------------------Lables---------------------------------
        title_lbl = ttk.Label(
            title_frm,
            text='Crear proyecto nuevo',
            font=tkf.Font(family=sv.FONT, size=sv.TITLE_FONT_SIZE)
        )
        title_lbl.grid(row=0,column=0, sticky=tk.N)
        
        prj_name_lbl = ttk.Label(
            info_frm,
            text='Nombre:',
            font=tkf.Font(family=sv.FONT, size=sv.NORMAL_FONT_SIZE)
        )
        prj_name_lbl.grid(row=0, column=0, sticky=tk.W)

        recipient_lbl = ttk.Label(
            info_frm,
            text='Cliente:',
            font=tkf.Font(family=sv.FONT, size=sv.NORMAL_FONT_SIZE)
        )
        recipient_lbl.grid(row=2, column=0, sticky=tk.W)

        start_date_lbl = ttk.Label(
            info_frm,
            text='Fecha inicio:',
            font=tkf.Font(family=sv.FONT, size=sv.NORMAL_FONT_SIZE)
        )
        start_date_lbl.grid(row=4, column=0, sticky=tk.W)

        end_date_lbl = ttk.Label(
            info_frm,
            text='Fecha cierre:',
            font=tkf.Font(family=sv.FONT, size=sv.NORMAL_FONT_SIZE)
        )
        end_date_lbl.grid(row=6, column=0, sticky=tk.W)

        addr_lbl = ttk.Label(
            info_frm,
            text='Direccion:',
            font=tkf.Font(family=sv.FONT, size=sv.NORMAL_FONT_SIZE)
        )
        addr_lbl.grid(row=8, column=0, sticky=tk.W)

        #-----------------------------Entry-------------------------------------
        prj_name_ety = ttk.Entry(
            info_frm,
            validate='key',
            validatecommand=(
                popup.register(validate.contains_char),
                '%P',
                'ltrs',
                'space'
            )
        )
        prj_name_ety.grid(row=1, column=0, pady=(0, 13))

        recipient_ety = ttk.Entry(
            info_frm,
            validate='key',
            validatecommand=(
                popup.register(validate.contains_char),
                '%P',
                'ltrs',
                'space'
            )
        )
        recipient_ety.grid(row=3, column=0, pady=(0, 13))

        start_date_ety = ttk.Entry(
            info_frm,
            validate='key',
            validatecommand=(
                popup.register(validate.contains_char),
                '%P',
                'dgts',
            )
        )
        start_date_ety.grid(row=5, column=0, pady=(0, 13))

        end_date_ety = ttk.Entry(
            info_frm,
            validate='key',
            validatecommand=(
                popup.register(validate.contains_char),
                '%P',
                'dgts',
                'frd slash'
            )
        )
        end_date_ety.grid(row=7, column=0, pady=(0, 13))
        
        addr_ety = ttk.Entry(
            info_frm,
            validate='key',
            validatecommand=(
                popup.register(validate.contains_char),
                '%P',
                'dgts',
            )
        )
        addr_ety.grid(row=9,column=0)

        #-------------------------------------Button----------------------------
        state = tk.StringVar()
        state_cbx = ttk.Combobox(
            info_frm,
            foreground=sv.WHITE,
            state="readonly",
            textvariable=state
        )
        state_cbx['values'] = [
            'Seleccione una opcion',
            'Planeacion',
            'Construccion'
        ]
        state_cbx.grid(row=10, column=0, sticky=tk.E, pady=(9, 0))
        state_cbx.current(0)

        #-------------------------------------Button----------------------------
        create_btn = ttk.Button(info_frm,
            text='Crear',
            command=lambda: controller.connector.insert_into(
                'project',
                prj_name_ety.get(),
                recipient_ety.get(),
                start_date_ety.get(),
                end_date_ety.get(),
                state.get(),
                addr_ety.get()

            )
        )
        create_btn.grid(row=11,column=0, pady=(20, 0))


        popup.deiconify()