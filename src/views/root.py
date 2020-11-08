import tkinter as tk
from tkinter import ttk
from constants import static_values
from views.log_in_window import LogInWind as LIWind
from views.sign_up_window import  SignUpWind as SUWind
from services.messenger import Messenger


class Root(tk.Tk):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.container = ttk.Frame(self)
        self._width_window = 0
        self._height_window = 0
        self.connector = Messenger("root", "trustme")
        self.views = {}
        self.account_types = static_values.acc_types
        self.catalog = {
            "LIWind": LIWind,
            "SUWind": SUWind
        }
        
        # Container setup.
        self.container.pack(side="top", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # General app configurations.
        self.title("SECOM")
        self.iconphoto(True, tk.PhotoImage(file=static_values.app_mini_logo))


    def _create_view(self, view_name):
        """
        INPUT: view object. 
        OUTPUT: None

        Description: creates frame for the view `vire_name`.
        """

        # Setup `new_view.`
        new_view = view_name(parent=self.container, controller=self)
        new_view.grid(row=0, column=0, sticky=tk.NSEW)

        # Add `new_view` to catalog of frames.
        self.views[view_name] = new_view
        

    def _delete_view(self, view):
        del self.views[self.catalog["SUWind"]]


    def _show_view(self, view_name):
        """
        INPUT: string
        OUTPUT: None.

        Calls the view `view_name` up front for display.
        """

        try:
            # Convert str to view object.
            view_name = self.conv(view_name)
            # Bings requested view to the front.
            self.views[view_name].tkraise()
        except KeyError:
            # Creates view and displays it.
            self._create_view(view_name)
            self.views[view_name].tkraise()


    def conv(self, view_name):
        """
        INPUT: string
        OUTPUT: view object

        Converts string to an existant view object
        """
        return self.catalog[view_name]


    def set_wind_param(self):
        """
        INPUT: None
        OUTPUT: None

        Description: Sets window in the middle of the screen.
        """
        width_screen = self.winfo_screenwidth()
        hight_screen = self.winfo_screenheight()
        x = (width_screen / 2) - (self._width_window / 2)
        y = (hight_screen / 2) - (self._height_window / 2)

        self.geometry("%dx%d+%d+%d" % (self._width_window, self._height_window, x, y))


    def get_width_window(self):
        return self._width_window


    def get_height_window(self):
        return self._height_window


    def set_wind_size(self, width, height):
        """
        INPUT: int x2
        OUTPUT: None

        Description: Changes main window's height and width.
        """
        self._width_window = width
        self._height_window = height

        self.geometry("%dx%d" % (self._width_window, self._height_window))

