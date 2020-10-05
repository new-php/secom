import tkinter as tk
import tkinter.font as tkf
import string
from tkinter import ttk
from services.filter import parse_info


class SignUpWind(ttk.Frame):
    def __init__(self, parent, controller): 
        super().__init__(parent)

        controller.set_wind_size(500, 500)
        controller.set_wind_param()
        frame_pad = 150

    # ----------------------------------------FRAMES--------------------------------------------------
        title_frm = ttk.Frame(self)
        title_frm.grid(row=0, column=0, pady=(0, 20))
        person_info_frm = ttk.LabelFrame(self,
                                         text="Informacion Personal",
                                         padding="2m",
                                         relief=tk.GROOVE)
        person_info_frm.grid(row=1, column=0, padx=(frame_pad / 3, 0), pady=(10, 20), sticky=tk.NW)
        access_info_frm = ttk.LabelFrame(self,
                                         text="Informacion de accesso",
                                         padding="2m",
                                         relief=tk.GROOVE)
        access_info_frm.grid(row=1, column=0, padx=(0, frame_pad / 3), pady=(10,20), sticky=tk.NE)


    # -----------------------------------------LABELS--------------------------------------------------
        title_lbl = ttk.Label(title_frm,
                              text="Crear cuenta nueva",
                              font=tkf.Font(family="Helvetica", size=15))
        title_lbl.grid(row=0, column=0, padx=frame_pad, sticky=tk.NS)

        first_name_lbl = ttk.Label(person_info_frm,
                                   text="Nombre:",
                                   font=tkf.Font(family="Helvetica", size=10))
        first_name_lbl.grid(row=0, column=0, sticky=tk.W)

        second_name_lbl = ttk.Label(person_info_frm,
                                    text="Segundo nombre:",
                                    font=tkf.Font(family="Helvetica", size=10))
        second_name_lbl.grid(row=3, column=0, pady=(15, 0), sticky=tk.W)

        f_last_name_lbl = ttk.Label(person_info_frm,
                                    text="Apellido paterno:",
                                    font=tkf.Font(family="Helvetica", size=10))
        f_last_name_lbl.grid(row=6, column=0, pady=(15, 0), sticky=tk.W)

        m_last_name_lbl = ttk.Label(person_info_frm,
                                    text="Apellido materno:",
                                    font=tkf.Font(family="Helvetica", size=10))
        m_last_name_lbl.grid(row=9, column=0, pady=(15, 0), sticky=tk.W)

        user_lbl = ttk.Label(access_info_frm,
                             text="Usuario:",
                             font=tkf.Font(family="Helvetica", size=10))
        user_lbl.grid(row=0, column=0, sticky=tk.W)

        pswd_lbl = ttk.Label(access_info_frm,
                             text="Contraseña:",
                             font=tkf.Font(family="Helvetica", size=10))
        pswd_lbl.grid(row=3, column=0, pady=(15, 0), sticky=tk.W)

        pswd_confirm_lbl = ttk.Label(access_info_frm,
                                     text="Confirme contraseña:",
                                     font=tkf.Font(family="Helvetica", size=10))
        pswd_confirm_lbl.grid(row=6, column=0, pady=(15, 0), sticky=tk.W)

        hint_lbl = ttk.Label(access_info_frm,
                                text="Palabra salvavidas:",
                                font=tkf.Font(family="Helvetica", size=10))
        hint_lbl.grid(row=9, column=0, pady=(15, 0), sticky=tk.W)

        acc_type_lbl = ttk.Label(access_info_frm,
                                 text="Tipo de cuenta:",
                                 font=tkf.Font(family="Helvetica", size=10))
        acc_type_lbl.grid(row=12, column=0, pady=(15, 0), sticky=tk.W)


    # -----------------------------------------ENTRIES----------------------------------------------------
        self.first_name_ety = ttk.Entry(person_info_frm)
        self.first_name_ety.grid(row=1,column=0, sticky=tk.W)

        self.second_name_ety = ttk.Entry(person_info_frm)
        self.second_name_ety.grid(row=4,column=0, sticky=tk.W)

        self.f_last_name_ety = ttk.Entry(person_info_frm)
        self.f_last_name_ety.grid(row=7,column=0, sticky=tk.W)

        self.m_last_name_ety = ttk.Entry(person_info_frm)
        self.m_last_name_ety.grid(row=10,column=0, sticky=tk.W)

        self.user_ety = ttk.Entry(access_info_frm)
        self.user_ety.grid(row=1,column=0, sticky=tk.E)

        self.pswd_ety = ttk.Entry(access_info_frm, show="*")
        self.pswd_ety.grid(row=4,column=0, sticky=tk.E)

        self.pswd_confirm_ety = ttk.Entry(access_info_frm, show="*")
        self.pswd_confirm_ety.grid(row=7,column=0, sticky=tk.E)

        self.hint_ety = ttk.Entry(access_info_frm)
        self.hint_ety.grid(row=10,column=0, sticky=tk.E)


    # -----------------------------------------COMBOBOX----------------------------------------------------
        self.acc_type_value = tk.StringVar()
        acc_type_cbx = ttk.Combobox(access_info_frm,
                                    state="readonly",
                                    textvariable=self.acc_type_value)
        acc_type_cbx['values'] = ("Planeacion", "Almlacen")
        acc_type_cbx.grid(row=13, column=0, sticky=tk.E)
        acc_type_cbx.current(0)


    # -----------------------------------------BUTTONS------------------------------------------------------        
        create_btn = ttk.Button(self,
                                    width=20,
                                    text="Crear",
                                    command=lambda: self.send_info())
        create_btn.grid(row=2, column=0, pady=(0, 10), sticky=tk.NS)

        back_btn = ttk.Button(self,
                              width=20,
                              text="Cancelar",
                              command=lambda: controller.show_view("LIWind"))
        back_btn.grid(row=3, column=0, sticky=tk.NS)


    def send_info(self):
        """
        INPUTS: None
        OUTPUT: None

        Description: Creates dict with keys as entry names which
        each has anothe dict with keys 'value' and 'input type'.
        Filters info and sends it to database thorugh
        `Messenger`.

        Entry names: 
        - first name.          - User           - Father last name.
        - Secod name.          - Hint           - Mother last name.
        - Password                              - Confirm Password.

        Value: 
        Entry box inputs. All managed as strings.

        Input type:
        - L -----> Letters.
        - N -----> Numbers.
        - S -----> Special characters (!, @, #, $, %, ^, &, *, <, >, ?).
        ***USE TOGETHER ADD SUCH CHARACTER TYPE TO ACCEPTABLE FOR 
           THE INPUT***
        Ex. LNS mean letter and Numbers and special characters.

        """
        
        entries = {
            'first name': {
                'value': self.first_name_ety.get(),
                'input type': 'L',
                'label': 0
            },
            'second name': {
                'value': self.second_name_ety.get(),
                'input type': 'L'
            },
            'father last name': {
                'value': self.f_last_name_ety.get(),
                'input type': 'L'
            },
            'mother last name': {
                'value': self.m_last_name_ety.get(),
                'input type': 'L'
            },
            'user': {
                'value':self.user_ety.get(),
                'input type': "LNS"
            },
            'hint': {
                'value': self.hint_ety.get(),
                'input type': 'L'
            },
            'password': {
                'value': self.pswd_ety.get(),
                'input type': "LNS"
            },
            'confirm password': {
                'value': self.pswd_confirm_ety.get(),
                'input type': "LNS"
            }
        }

        parse_info(entries)

        self.wrong_inp_message(entries)




    def wrong_inp_message(self, entries):
        """
        INPUT:
        - dict (check send_info() description for more specifications)
        Output:
          None

        Description: Displays invalid argument labels for invalid 
        inputs.
        """
        pass
        # for info in entries:
        #     for flag in entries[info]['erorr']:
        #         if flag:
