import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from constants import static_values as sv
from views.log_in_window import LogInWind as LIWind
from views.sign_up_window import  SignUpWind as SUWind
from views.planner_home_window import PlannerHomeWind as PHWind
from services.messenger import Messenger


class Root(tk.Tk):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        try: 
        # General app configurations.
            self.title("SECOM")
            self.iconphoto(True, tk.PhotoImage(file=sv.APP_MINI_LOGO))

            # Container setup.
            self.container = ttk.Frame(self)
            self.container.pack(side="top", expand=True)
            self.container.grid_rowconfigure(0, weight=1)
            self.container.grid_columnconfigure(0, weight=1)

            self.connector = Messenger()
            self.views = {}
            self.catalog = {
                "LIWind": LIWind,
                "SUWind": SUWind,
                "PHWind": PHWind
            }

            self.refresh_window("LIWind")
            
        except:
            messagebox.showerror(
                "Error de conexion.", 
                format("No se pudo establecer la conexion con el servidor.")
            )
            self.destroy()


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


    def refresh_window(self, view_name, delete=None):
        """
        
        """
        self.set_wind_param(
            sv.WIND_SIZE[view_name][0],
            sv.WIND_SIZE[view_name][1]
        )
        self.show_view(view_name)

        if delete is not None:
            self._delete_view(delete)
        

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


    def _delete_view(self, view_name):
        # self.views[self.catalog[view_name]].destroy()
        del self.views[self.catalog[view_name]]


    def set_wind_param(self, new_width, new_height):
        """
        INPUT: intx2
        OUTPUT: None

        Description: Centers the apps' window with respect to the last position 
                     of the last view.
        """

        x = y = 0
        self.update()

        if self.winfo_width() == self.winfo_height() == 1:
            x = self.winfo_screenwidth()/2 - new_width/2
            y = self.winfo_screenheight()/2 - new_height/2
        else:
            x = self.winfo_rootx() + (self.winfo_width()/2 - new_width/2)
            y = self.winfo_rooty() + (self.winfo_height()/2 - new_height/2)

        self.geometry("%dx%d+%d+%d" % (new_width, new_height, x, y))
