import string
import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk
from constants import static_values as sv
from services import validate
from tools.su_entry import SUEntry 


class SignUpWind(ttk.Frame):
    def __init__(self, parent, controller): 
        super().__init__(parent)

        controller.set_wind_size(
            width=sv.SUWIND_WIDTH,
            height=sv.SUWIND_HEIGHT,
        )
        controller.set_wind_param()
        frame_pad = 150

        # -------------------------------FRAMES---------------------------------
        title_frm = ttk.Frame(self)
        title_frm.grid(row=0, column=1, pady=(0, 20))

        self.peron_error_frm = ttk.Frame(self)

        self.person_info_frm = ttk.LabelFrame(self,
                                              text="Informacion Personal",
                                              padding="2m",
                                              relief=tk.RIDGE)
        self.person_info_frm.grid(row=1,
                                 column=1,
                                 padx=(frame_pad / 3, 0),
                                 pady=(10, 20), 
                                 sticky=tk.NW)

        self.access_info_frm = ttk.LabelFrame(self,
                                              text="Informacion de accesso",
                                              padding="2m",
                                              relief=tk.RIDGE)
        self.access_info_frm.grid(row=1,
                                  column=1,
                                  padx=(0, frame_pad / 3),
                                  pady=(10,20),
                                  sticky=tk.NE)

        self.warnings_frm = ttk.Frame(self)
        self.warnings_frm.grid(
            row=1,
            column=2,
            sticky=tk.NS
        )


        # -------------------------------LABELS---------------------------------
        title_lbl = ttk.Label(title_frm,
                              text="Crear cuenta nueva",
                              font=tkf.Font(family="Helvetica", size=15))
        title_lbl.grid(row=0, column=0, padx=frame_pad, sticky=tk.NS)

        self.first_name_lbl = ttk.Label(self.person_info_frm,
                                   text="Nombre:",
                                   font=tkf.Font(family="Helvetica", size=10))
        self.first_name_lbl.grid(row=0, column=0, sticky=tk.W)

        self.second_name_lbl = ttk.Label(self.person_info_frm,
                                    text="Segundo nombre:",
                                    font=tkf.Font(family="Helvetica", size=10))
        self.second_name_lbl.grid(row=3, column=0, pady=(15, 0), sticky=tk.W)

        self.f_last_name_lbl = ttk.Label(self.person_info_frm,
                                    text="Apellido paterno:",
                                    font=tkf.Font(family="Helvetica", size=10))
        self.f_last_name_lbl.grid(row=6, column=0, pady=(15, 0), sticky=tk.W)

        self.m_last_name_lbl = ttk.Label(self.person_info_frm,
                                    text="Apellido materno:",
                                    font=tkf.Font(family="Helvetica", size=10))
        self.m_last_name_lbl.grid(row=9, column=0, pady=(15, 0), sticky=tk.W)

        self.user_lbl = ttk.Label(self.access_info_frm,
                             text="Usuario:",
                             font=tkf.Font(family="Helvetica", size=10))
        self.user_lbl.grid(row=0, column=0, sticky=tk.W)

        self.pswd_lbl = ttk.Label(self.access_info_frm,
                             text="Contraseña:",
                             font=tkf.Font(family="Helvetica", size=10))
        self.pswd_lbl.grid(row=3, column=0, pady=(15, 0), sticky=tk.W)

        self.pswd_confirm_lbl = ttk.Label(self.access_info_frm,
                                     text="Confirme contraseña:",
                                     font=tkf.Font(family="Helvetica", size=10))
        self.pswd_confirm_lbl.grid(row=6, column=0, pady=(15, 0), sticky=tk.W)

        self.hint_lbl = ttk.Label(self.access_info_frm,
                                text="Palabra salvavidas:",
                                font=tkf.Font(family="Helvetica", size=10))
        self.hint_lbl.grid(row=9, column=0, pady=(15, 0), sticky=tk.W)

        acc_type_lbl = ttk.Label(self.access_info_frm,
                                 text="Tipo de cuenta:",
                                 font=tkf.Font(family="Helvetica", size=10))
        acc_type_lbl.grid(row=12, column=0, pady=(15, 0), sticky=tk.W)

        self.warning_lbl = tk.Label(self.warnings_frm,
                                text="La contraseña debera satisfacer lo siguiente:\n"\
                                     "- Minimo 8 caracteres.                           \n"\
                                     "- Minimo 1 mayuscula.                          \n"\
                                     "- Minimo 1 minuscula.                           \n"\
                                     "- Minimo 1 caracter especial.                 \n"\
                                     "- Minimo 1 digito.                                  \n"\
                                     "- Coinsidir con la contraseña confirmada.",
                                font=tkf.Font(family="Helvetica", size=10))
        self.warning_lbl.grid(row=0, column=0, pady=90, sticky=tk.W)


        # -----------------------------ENTRIES----------------------------------
        self.first_name_ety = SUEntry(
            parent=self.person_info_frm,
            constraints=('ltrs')
        )
        self.first_name_ety.grid(row=1,column=0, sticky=tk.W)

        self.second_name_ety = SUEntry(
            self.person_info_frm,
            constraints=('ltrs')
        )
        self.second_name_ety.grid(row=4,column=0, sticky=tk.W)

        self.f_last_name_ety = SUEntry(
            self.person_info_frm,
            constraints=('ltrs')
        )
        self.f_last_name_ety.grid(row=7,column=0, sticky=tk.W)

        self.m_last_name_ety = SUEntry(
            self.person_info_frm,
            constraints=('ltrs')
        )
        self.m_last_name_ety.grid(row=10,column=0, sticky=tk.W)

        self.user_ety = SUEntry(
            parent=self.access_info_frm,
            constraints=('ltrs', 'dgts', 'spchars')
        )
        self.user_ety.grid(row=1,column=0, sticky=tk.W)

        self.pswd_ety = SUEntry(
            parent=self.access_info_frm,
            constraints=('ltrs', 'dgts', 'spchars'),
            char="•"
        )
        self.pswd_ety.grid(row=4,column=0, sticky=tk.W)

        self.pswd_confirm_ety = SUEntry(
            parent=self.access_info_frm,
            constraints=('ltrs', 'dgts', 'spchars'),
            char="•"
        )
        self.pswd_confirm_ety.grid(row=7,column=0, sticky=tk.W)

        self.hint_ety = SUEntry(
            parent=self.access_info_frm,
            constraints=('ltrs', 'space')
        )
        self.hint_ety.grid(row=10,column=0, sticky=tk.W)


        # ----------------------------COMBOBOX----------------------------------
        self.acc_type_value = tk.StringVar()
        acc_type_cbx = ttk.Combobox(self.access_info_frm,
                                    state="readonly",
                                    textvariable=self.acc_type_value)
        acc_type_cbx['values'] = ("Planeacion", "Almacen")
        acc_type_cbx.grid(row=13, column=0, sticky=tk.E)
        acc_type_cbx.current(0)


        # -----------------------------BUTTONS----------------------------------
        create_btn = ttk.Button(self,
                                    width=20,
                                    text="Crear",
                                    command=lambda: self.send_info(controller))
        create_btn.grid(row=2, column=1, pady=(0, 10), sticky=tk.NS)

        back_btn = ttk.Button(self,
                              width=20,
                              text="Cancelar",
                              command=lambda: controller.refresh_window(
                                 view_name="LIWind",
                                 width=sv.LIWIND_WIDTH,
                                 height=sv.LIWIND_HEIGHT
                              )
        )
        back_btn.grid(row=3, column=1, sticky=tk.NS)
    

    def send_info(self, controller):
        """
        INPUT: root object.
        OUTPUT: None.

        Description: obtains user iputs and validatres entries.
        """
        info = [
            self.user_ety.get(),
            self.pswd_ety.get(),
            self.hint_ety.get(),
            controller.account_types[self.acc_type_value.get()],
            self.first_name_ety.get(),
            self.second_name_ety.get(),
            self.f_last_name_ety.get(),
            self.m_last_name_ety.get(),
        ]

        self.pswd_lbl.config(
                foreground="#000000",
                font=tkf.Font(family="Helvetica", size=10)
        )
        self.pswd_confirm_lbl.config(
            foreground="#000000",
            font=tkf.Font(family="Helvetica", size=10)            
        )
        

        if validate.password(self.pswd_ety.get(), self.pswd_confirm_ety.get()) and validate.all_filled(info):
            controller.connector.create_user(info)
            controller.delete_view('SUWind')
            controller.show_view('LIWind')

        else:
            self.pswd_lbl.config(
                foreground="#DB1B0D",
                font=tkf.Font(family="Helvetica", size=10, weight='bold')
            )
            self.pswd_confirm_lbl.config(
                foreground="#DB1B0D",
                font=tkf.Font(family="Helvetica", size=10, weight='bold')
            )
            