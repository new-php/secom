import string
import tkinter as tk
import tkinter.font as tkf
from tkinter import ttk
from services import validate


class SignUpWind(ttk.Frame):
    def __init__(self, parent, controller): 
        super().__init__(parent)

        controller.set_wind_size(800, 500)
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
                                  pady=(10,20), sticky=tk.NE)


        # -------------------------------LABELS---------------------------------
        title_lbl = ttk.Label(title_frm,
                              text="Crear cuenta nueva",
                              font=tkf.Font(family="Helvetica", size=15))
        title_lbl.grid(row=0, column=0, padx=frame_pad, sticky=tk.NS)

        first_name_lbl = ttk.Label(self.person_info_frm,
                                   text="Nombre:",
                                   font=tkf.Font(family="Helvetica", size=10))
        first_name_lbl.grid(row=0, column=0, sticky=tk.W)

        second_name_lbl = ttk.Label(self.person_info_frm,
                                    text="Segundo nombre:",
                                    font=tkf.Font(family="Helvetica", size=10))
        second_name_lbl.grid(row=3, column=0, pady=(15, 0), sticky=tk.W)

        f_last_name_lbl = ttk.Label(self.person_info_frm,
                                    text="Apellido paterno:",
                                    font=tkf.Font(family="Helvetica", size=10))
        f_last_name_lbl.grid(row=6, column=0, pady=(15, 0), sticky=tk.W)

        m_last_name_lbl = ttk.Label(self.person_info_frm,
                                    text="Apellido materno:",
                                    font=tkf.Font(family="Helvetica", size=10))
        m_last_name_lbl.grid(row=9, column=0, pady=(15, 0), sticky=tk.W)

        user_lbl = ttk.Label(self.access_info_frm,
                             text="Usuario:",
                             font=tkf.Font(family="Helvetica", size=10))
        user_lbl.grid(row=0, column=0, sticky=tk.W)

        pswd_lbl = ttk.Label(self.access_info_frm,
                             text="Contraseña:",
                             font=tkf.Font(family="Helvetica", size=10))
        pswd_lbl.grid(row=3, column=0, pady=(15, 0), sticky=tk.W)

        pswd_confirm_lbl = ttk.Label(self.access_info_frm,
                                     text="Confirme contraseña:",
                                     font=tkf.Font(family="Helvetica", size=10))
        pswd_confirm_lbl.grid(row=6, column=0, pady=(15, 0), sticky=tk.W)

        hint_lbl = ttk.Label(self.access_info_frm,
                                text="Palabra salvavidas:",
                                font=tkf.Font(family="Helvetica", size=10))
        hint_lbl.grid(row=9, column=0, pady=(15, 0), sticky=tk.W)

        acc_type_lbl = ttk.Label(self.access_info_frm,
                                 text="Tipo de cuenta:",
                                 font=tkf.Font(family="Helvetica", size=10))
        acc_type_lbl.grid(row=12, column=0, pady=(15, 0), sticky=tk.W)


        # ---------------------------VALIDATORS---------------------------------
        validate_letters = (self.register(validate.letters), '%P')
        validate_user = (self.register(validate.letters_numbers), '%P')
        validate_pswd = (self.register(validate.letters_numbers_specials), '%P')


        # -----------------------------ENTRIES----------------------------------
        self.first_name_ety = ttk.Entry(self.person_info_frm,
                                        validate="key",
                                        validatecommand=validate_letters)
        self.first_name_ety.grid(row=1,column=0, sticky=tk.W)

        self.second_name_ety = ttk.Entry(self.person_info_frm,
                                         validate="key",
                                         validatecommand=validate_letters)
        self.second_name_ety.grid(row=4,column=0, sticky=tk.W)

        self.f_last_name_ety = ttk.Entry(self.person_info_frm,
                                         validate="key",
                                         validatecommand=validate_letters)
        self.f_last_name_ety.grid(row=7,column=0, sticky=tk.W)

        self.m_last_name_ety = ttk.Entry(self.person_info_frm,
                                         validate="key",
                                         validatecommand=validate_letters)
        self.m_last_name_ety.grid(row=10,column=0, sticky=tk.W)

        self.user_ety = ttk.Entry(self.access_info_frm,
                                  validate="key",
                                  validatecommand=validate_user)
        self.user_ety.grid(row=1,column=0, sticky=tk.W)


        self.pswd_ety = ttk.Entry(self.access_info_frm,
                                  validate="key",
                                  validatecommand=validate_pswd,
                                  show="*")
        self.pswd_ety.grid(row=4,column=0, sticky=tk.W)

        self.pswd_confirm_ety = ttk.Entry(self.access_info_frm,
                                          show="*",
                                          validate="key",
                                          validatecommand=validate_user)
        self.pswd_confirm_ety.grid(row=7,column=0, sticky=tk.W)

        self.hint_ety = ttk.Entry(self.access_info_frm,
                                  validate="key",
                                  validatecommand=validate_letters)
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
                              command=lambda: controller.show_view("LIWind"))
        back_btn.grid(row=3, column=1, sticky=tk.NS)


    def send_info(self, controller):

        errors = validate.password(self.pswd_ety.get(),
                                   self.pswd_confirm_ety.get()
        )

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

        controller.connector.create_user(info)