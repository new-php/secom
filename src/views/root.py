import tkinter as tk
from .log_in_window import LogInWind as LIWind
from .sign_up_window import  SignUpWind as SUWind
from services.messenger import Messenger


class Root(tk.Tk):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.container = tk.Frame(self,relief="groove")
        self.widthWindow = 400
        self.heightWindow = 225
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


    def _createFrame(self, page_name):
        """
        INPUT: view object. 
        OUTPUT: None

        Description: creates frame for the view `page_name`.
        """

        # Setup `newFrame.`
        newFrame = page_name(parent=self.container, controller=self)
        newFrame.grid(row=0, column=0, sticky=tk.NSEW)

        # Add `newFrame` to catalog of frames.
        self.frames[page_name] = newFrame
        

    def showFrame(self, page_name):
        """
        INPUT: string
        OUTPUT: None.

        Calls the view `page_name` up front for display.
        """

        try:
            # Convert str to view object.
            page_name = self.conv(page_name)
            # Bings requested view to the front.
            self.frames[page_name].tkraise()
        except KeyError:
            # Creates view and displays it.
            self._createFrame(page_name)
            self.frames[page_name].tkraise()


    def setWindParam(self):
        """
        INPUT: None
        OUTPUT: None

        Description: Sets window in the middle of the screen.
        """
        widthScreen = self.winfo_screenwidth()
        hightScreen = self.winfo_screenheight()
        x = (widthScreen / 2) - (self.widthWindow / 2)
        y = (hightScreen / 2) - (self.heightWindow / 2)

        self.geometry("%dx%d+%d+%d" % (self.widthWindow, self.heightWindow, x, y))


    def conv(self, page_name):
        """
        INPUT: string
        OUTPUT: view object

        Converts string to an existant view object
        """
        for view in self.catalog:
            if view == page_name:
                return self.catalog[view]
