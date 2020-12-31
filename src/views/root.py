import tkinter as tk
from tkinter import ttk
from constants import static_values as sv
from views.log_in_window import LogInWind as LIWind
from views.sign_up_window import  SignUpWind as SUWind
from services.messenger import Messenger


class Root(tk.Tk):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.container = ttk.Frame(self)
        self._width_window = 0
        self._height_window = 0
        self.connector = Messenger()
        self.views = {}
        self.account_types = sv.acc_types
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
        self.iconphoto(True, tk.PhotoImage(file=sv.app_mini_logo))

        self.refresh_window(
            view_name="LIWind",
            width=sv.LIWIND_WIDTH,
            height=sv.LIWIND_HEIGHT
        )


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


    def refresh_window(self, view_name, width, height):
        self.set_wind_size(width, height)
        self.show_view(view_name)

        

    def show_view(self, view_name):
        """
        INPUT: string
        OUTPUT: None.

        Calls the view `view_name` up front for display.
        """

        try:
            # Convert str to view object.
            view_name = self._conv(view_name)
            # Bings requested view to the front.
            self.views[view_name].tkraise()
        except KeyError:
            # Creates view and displays it.
            self._create_view(view_name)
            # Bings requested view to the front.
            self.views[view_name].tkraise()
       

    def _conv(self, view_name):
        """
        INPUT: string
        OUTPUT: view object

        Converts string to an existant view object
        """
        return self.catalog[view_name]


    def delete_view(self, view_name):
        del self.views[self.catalog[view_name]]


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

    def set_wind_size(self, width, height):
        """
        INPUT: int x2
        OUTPUT: None

        Description: Changes main window's height and width.
        """
        self._width_window = width
        self._height_window = height

        self.geometry("%dx%d" % (self._width_window, self._height_window))
