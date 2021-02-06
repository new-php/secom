import tkinter as tk
from tkinter import  messagebox, ttk
from tkinter.font import Font
from constants import static_values as sv
from services import validate
from tkinter.messagebox import showerror

class SignUpWind(ttk.Frame):
    def __init__(self, parent, controller): 
        super().__init__(parent)
        person_count = 0
        access_count = 0
        self.invalid_inps = set()
        self.acc_type_value = tk.StringVar()

        self.wdgts = {
            'frm':{
                'title': ttk.Frame(self),
                'person_info':  ttk.LabelFrame(
                    self,
                    text="Informacion Personal",
                    padding="2m",
                    relief=tk.RIDGE
                ),
                'access_info': ttk.LabelFrame(
                    self,
                    text="Informacion de cuenta",
                    padding="2m",
                    relief=tk.RIDGE
                )
            }
        }
        self.wdgts['lbl'] = {
            'title': ttk.Label(
                self.wdgts['frm']['title'],
                text="Crear cuenta nueva",
                font=Font(family="Helvetica", size=15)
            ),
            'first_name': ttk.Label(
                self.wdgts['frm']['person_info'],
                text="Nombre:",
                font=Font(family="Helvetica", size=10)
            ),
            'second_name': ttk.Label(
                self.wdgts['frm']['person_info'],
                text="Segundo nombre:",
                font=Font(family="Helvetica", size=10)
            ),
            'f_last_name': ttk.Label(
                self.wdgts['frm']['person_info'],
                text="Apellido paterno:",
                font=Font(family="Helvetica", size=10)
            ),
            'm_last_name': ttk.Label(
                self.wdgts['frm']['person_info'],
                text="Apellido materno:",
                font=Font(family="Helvetica", size=10)
            ),
            'user_name': ttk.Label(
                self.wdgts['frm']['access_info'],
                text="Usuario:",
                font=Font(family="Helvetica", size=10)
            ),
            'pswd': ttk.Label(
                self.wdgts['frm']['access_info'],
                text="Contraseña:",
                font=Font(family="Helvetica", size=10)
            ),
            'pswd_confirm': ttk.Label(
                self.wdgts['frm']['access_info'],
                text="Confirme contraseña:",
                font=Font(family="Helvetica", size=10)
            ),
            'hint': ttk.Label(
                self.wdgts['frm']['access_info'],
                text="Palabra salvavidas:",
                font=Font(family="Helvetica", size=10)
            ),
            'user_type': ttk.Label(
                self.wdgts['frm']['access_info'],
                text="Tipo de cuenta:",
                font=Font(family="Helvetica", size=10)
            )
        }
        self.wdgts['ety'] = {
            'first_name': ttk.Entry(
                self.wdgts['frm']['person_info'],
                validate='key',
                validatecommand=(
                    self.register(validate.contains_char),
                    '%P',
                    'ltrs'
                )
            ),
            'second_name': ttk.Entry(
                self.wdgts['frm']['person_info'],
                validate='key',
                validatecommand=(
                    self.register(validate.contains_char),
                    '%P',
                    'ltrs'
                )
            ),
            'f_last_name': ttk.Entry(
                self.wdgts['frm']['person_info'],
                validate='key',
                validatecommand=(
                    self.register(validate.contains_char),
                    '%P',
                    'ltrs'
                )
            ),
            'm_last_name': ttk.Entry(
                self.wdgts['frm']['person_info'],
                validate='key',
                validatecommand=(
                    self.register(validate.contains_char),
                    '%P',
                    'ltrs'
                )
            ),
            'user_name': ttk.Entry(
                self.wdgts['frm']['access_info'],
                validate='key',
                validatecommand=(
                    self.register(validate.contains_char),
                    '%P',
                    'ltrs',
                    'dgts',
                    'spchars'
                )
            ),
            'pswd': ttk.Entry(
                self.wdgts['frm']['access_info'],
                show='•',
                validate='key',
                validatecommand=(
                    self.register(validate.contains_char),
                    '%P',
                    'ltrs',
                    'dgts',
                    'spchars'
                )
            ),
            'pswd_confirm': ttk.Entry(
                self.wdgts['frm']['access_info'],
                show='•',
                validate='key',
                validatecommand=(
                    self.register(validate.contains_char),
                    '%P',
                    'ltrs',
                    'dgts',
                    'spchars'
                )
            ),
            'hint': ttk.Entry(
                self.wdgts['frm']['access_info'],
                validate='key',
                validatecommand=(
                    self.register(validate.contains_char),
                    '%P',
                    'ltrs',
                    'space'
                )
            ) 
        }
        self.wdgts['cbx'] = {
            'user_type': ttk.Combobox(
                self.wdgts['frm']['access_info'],
                foreground=sv.WHITE,
                state="readonly",
                textvariable=self.acc_type_value
            )
        }
        self.wdgts['btn'] = {
            'create': ttk.Button(
                self,
                width=20,
                text="Crear",
                command=lambda: self.create_user(controller)
            ),
            'back': ttk.Button(
                self,
                width=20,
                text="Cancelar",
                command=lambda: controller.refresh_window("LIWind")
            )
        }

        # -------------------------------Frames---------------------------------
        self.wdgts['frm']['title'].grid(row=0, column=0, pady=(0, 20))
        self.wdgts['frm']['person_info'].grid(
            row=1,
            column=0,
            padx=(150 / 3, 0),
            pady=(10, 20), 
            sticky=tk.NW
        )
        self.wdgts['frm']['access_info'].grid(
            row=1,
            column=0,
            padx=(0, 150 / 3),
            pady=(10,20),
            sticky=tk.NE
        )


        # -------------------------------LABELS---------------------------------
        for name  in self.wdgts['lbl']:
            if self.wdgts['lbl'][name].master == self.wdgts['frm']['person_info']:
                self.wdgts['lbl'][name].grid(
                    row=person_count,
                    column=0,
                    pady=(15, 0),
                    sticky=tk.W
                )
                person_count += 2 
            elif self.wdgts['lbl'][name].master == self.wdgts['frm']['access_info']:
                self.wdgts['lbl'][name].grid(
                    row=access_count,
                    column=0,
                    pady=(15, 0),
                    sticky=tk.W
                )
                access_count += 2
            else:
                self.wdgts['lbl'][name].grid(
                    row=0,
                    column=0,
                    padx=150,
                    sticky=tk.W
                )

        person_count = 1
        access_count = 1


        # -----------------------------ENTRIES----------------------------------
        for name  in self.wdgts['ety']:
            if self.wdgts['ety'][name].master == self.wdgts['frm']['person_info']:
                self.wdgts['ety'][name].grid(
                    row=person_count,
                    column=0,
                    sticky=tk.W
                )
                person_count += 2 
            else:
                self.wdgts['ety'][name].grid(
                    row=access_count,
                    column=0,
                    sticky=tk.W
                )
                access_count += 2


        # ------------------------------Combobox----------------------------------
        self.wdgts['cbx']['user_type']['values'] = [option for option in sv.ACC_TYPE]
        self.wdgts['cbx']['user_type'].grid(row=13, column=0, sticky=tk.E)
        self.wdgts['cbx']['user_type'].current(0)


        # -----------------------------BUTTONS----------------------------------
        self.wdgts['btn']['create'].grid(row=2, column=0, pady=(0, 10), sticky=tk.NS)
        self.wdgts['btn']['back'].grid(row=3, column=0, sticky=tk.NS)

    

    def create_user(self, controller):
        """
        INPUT: root object.
        OUTPUT: None.

        Description: obtains user iputs and validatres entries.

        EXEPTIONS HANDLED FROM: messemger.py '_prepare_args' 
        """

        for name in self.wdgts['ety']:
            if self.wdgts['lbl'][name] in self.invalid_inps:
                if validate.is_filled(self.wdgts['ety'][name].get()):
                    self.wdgts['lbl'][name].config(foreground=sv.WHITE)
                    self.invalid_inps.discard(self.wdgts['lbl'][name])
            else:
                if not validate.is_filled(self.wdgts['ety'][name].get()):
                    self.invalid_inps.add(self.wdgts['lbl'][name])

        if sv.ACC_TYPE[self.acc_type_value.get()] == 0:
            self.invalid_inps.add(self.wdgts['lbl']['user_type'])
        else:
            self.invalid_inps.discard(self.wdgts['lbl']['user_type'])
            self.wdgts['lbl']['user_type'].config(foreground=sv.WHITE)
            

        if not validate.eight_chars(self.wdgts['ety']['pswd'].get()):
            self.invalid_inps.add(self.wdgts['lbl']['pswd'])
        else:
            self.invalid_inps.discard(self.wdgts['lbl']['pswd'])
            self.wdgts['lbl']['pswd'].config(foreground=sv.WHITE)


        if not validate.match_password(self.wdgts['ety']['pswd'].get(), self.wdgts['ety']['pswd'].get()):
            self.invalid_inps.add(self.wdgts['lbl']['pswd_confirm'])
        else:
            self.invalid_inps.discard(self.wdgts['lbl']['pswd_confirm'])
            self.wdgts['lbl']['pswd_confirm'].config(foreground=sv.WHITE)

        if not self.invalid_inps:
            try:
                controller.connector.insert_into(
                    'user',
                    self.wdgts['ety']['user_name'].get(),
                    self.wdgts['ety']['pswd'].get(),
                    self.wdgts['ety']['hint'].get(),
                    sv.ACC_TYPE[self.acc_type_value.get()],
                    self.wdgts['ety']['first_name'].get(),
                    self.wdgts['ety']['second_name'].get(),
                    self.wdgts['ety']['f_last_name'].get(),
                    self.wdgts['ety']['m_last_name'].get()
                )
                controller.refresh_window('LIWind', delete='SUWind')
            except ValueError as err:
                self.wdgts['ety']['user_name'].delete(0, 'end')
                self.wdgts['lbl']['user_name'].config(foreground=sv.RED)
                messagebox.showerror('Error', '{}'.format(err))
 
        else:
            for widget in self.invalid_inps:
                widget.config(foreground=sv.RED)
            if self.wdgts['lbl']['pswd'] in self.invalid_inps:
                messagebox.showerror(
                    "Error",
                    "Campos Invalidos.\n\n"\
                    "La contraseña debe de tener:\n"\
                        "- Minimo 8 caracteres.\n"\
                        "- Minimo 1 mayuscula.\n"\
                        "- Minimo 1 minuscula.\n"\
                        "- Minimo 1 caracter especial.\n"\
                        "- Minimo 1 digito.\n"\
                        "- Coincidir con la contraseña confirmada."
                )
            else: messagebox.showerror('Error', 'Valores invalidos')
