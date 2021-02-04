import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from constants import static_values as sv
from views.log_in_window import LogInWind as LIWind
from views.sign_up_window import  SignUpWind as SUWind
from views.planner_home_window import PlannerHomeWind as PHWind
from views.warehouse_home_window import WareHomeWind as WHWind
from views.owner_home_window import OwnerHomeWind as OHWind
from services.messenger import Messenger


class Root(tk.Tk):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        #try: 
        # General app configurations.
        self.withdraw()
        self.title("SECOM")
        self.iconphoto(True, tk.PhotoImage(file=sv.APP_MINI_LOGO))
        self.set_wind_param(self, 0, 0)

        # Container setup.
        self.container = ttk.Frame(self)
        self.container.pack(side="top", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.connector = Messenger()
        self.logged_user = None
        self.logged_user_type = None
        self.views = {}
        self.catalog = {
            "LIWind": LIWind,
            "SUWind": SUWind,
            "PHWind": PHWind,
            "WHWind": WHWind,
            "OHWind": OHWind
        }
        

        self.refresh_window("LIWind")
        self.deiconify()
            
        # except:
        #     messagebox.showerror(
        #         "Error de conexion.", 
        #         format("No se pudo establecer la conexion con el servidor.")
        #     )
        #     self.destroy()


    def _create_view(self, view_name):
        """
        INPUT: view object. 
        OUTPUT: None

        Description: creates frame for the view `vire_name` and is added to
                     dict `self.views`.
        """

        # Setup `new_view.`
        new_view = view_name(parent=self.container, controller=self)
        new_view.grid(row=0, column=0, sticky=tk.NSEW)

        # Add `new_view` to catalog of frames.
        self.views[view_name] = new_view


    def refresh_window(self, view_name, top_view=None, delete=None):
        """
        INPUT: one - two strings.
        OUTPUT: None.

        Description: Changes window's size acording to `view_name` specification
                     in static values (sv) as well as recentering window with 
                     respec to the center of the last window postion on the
                     screen, updates view and may delte view if given a second
                     input.
        """

        self.withdraw()
        controller = self if top_view is None else top_view
        self.set_wind_param(
            controller,
            sv.WIND_SIZE[view_name][0],
            sv.WIND_SIZE[view_name][1]
        )

        if top_view is None:
            self.show_view(view_name)
            if delete is not None:
                self._delete_view(delete)

        self.deiconify()
        

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
        """
        INPUT: string.
        OUTPUT: none.

        DESCRIPTION: deletes given view from memory and from dict. `views`.
        """
        self.views[self._conv(view_name)].destroy()
        del self.views[self._conv(view_name)]

    @staticmethod
    def set_wind_param(controller, new_width, new_height):
        """
        INPUT: Tk/popup object, intx2
        OUTPUT: None

        Description: Centers the apps' window or popup window with respect to
                     the last position of the last view.
        """

        x = y = 0
        controller.update()

        if controller.winfo_width() == controller.winfo_height() == 1:
            x = controller.winfo_screenwidth()/2 - new_width/2
            y = controller.winfo_screenheight()/2 - new_height/2
        else:
            x = controller.winfo_rootx() + (controller.winfo_width()/2 - new_width/2)
            y = controller.winfo_rooty() + (controller.winfo_height()/2 - new_height/2)

        controller.geometry("%dx%d+%d+%d" % (new_width, new_height, x, y))

