from tkinter import ttk
from services import validate

class SUEntry(ttk.Entry):
    def __init__(self,parent, constraints, char='', *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.config(
            show=char,
            validate='key',
            validatecommand=(
                self.register(validate.contains_char),
                '%P',
                constraints
            )
        )
