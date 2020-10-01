import tkinter as tk
from .log_in_window import LogInWind as LIWind
from .sign_up_window import  SignUpWind as SUWind
from services.messenger import Messenger


class Root(tk.Tk):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.container = tk.Frame(self,relief="groove")
        self.__width_window = 400
        self.__height_window = 225
        self.frames = {}
        self.catalog = {
            "LIWind": LIWind,
            "SUWind": SUWind
        }
        
        # Container setup.
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # General app configurations.
        self.title("SECOM")
        self.iconbitmap("C:/Users/joshu/Documents/VSC/python/secom/src/assets/icons/icon.ico")
        self.set_wind_param()


    def _create_frame(self, view_name):
        """
        INPUT: view object. 
        OUTPUT: None

        Description: creates frame for the view `vire_name`.
        """

        # Setup `newFrame.`
        new_frame = view_name(parent=self.container, controller=self)
        new_frame.grid(row=0, column=0, sticky=tk.NSEW)

        # Add `newFrame` to catalog of frames.
        self.frames[view_name] = new_frame
        

    def show_frame(self, view_name):
        """
        INPUT: string
        OUTPUT: None.

        Calls the view `view_name` up front for display.
        """

        try:
            # Convert str to view object.
            view_name = self.conv(view_name)
            # Bings requested view to the front.
            self.frames[view_name].tkraise()
        except KeyError:
            # Creates view and displays it.
            self._create_frame(view_name)
            self.frames[view_name].tkraise()


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
        x = (width_screen / 2) - (self.__width_window / 2)
        y = (hight_screen / 2) - (self.__height_window / 2)

        self.geometry("%dx%d+%d+%d" % (self.__width_window, self.__height_window, x, y))


    def get_width_window(self):
        return self.__width_window

    def set_wind_size(self, width, height):
        """
        INPUT: int x2
        OUTPUT: None

        Description: Changes main window's height and width.
        """
        self.__width_window = width
        self.__height_window = height

        self.geometry("%dx%d" % (self.__width_window, self.__height_window))

