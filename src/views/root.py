import tkinter as tk
from .log_in_window import LogInWind as LIWind
from .sign_up_window import SignUpWind as SuWind
from services.messenger import Messenger


class Root(tk.Tk):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        
        # General variables.
        self.frames = {}
        self.width_window
        self.height_window
        self.container = tk.Frame(self,relief="groove")

        # General app configurations.
        self.title("SECOM")
        self.iconbitmap("C:/Users/joshu/Documents/VSC/python/secom/icons/icon.ico")
        self.configure(bg="#E0E0E0")
        
        # Container setup.
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)


    def createFrame(self, page_name):
        """
        INPUT: view object. 
        OUTPUT: None

        Description: creates frame for the view `page_name`.
        """
        # Setup `newFrame.`
        newFrame = page_name(parent=self.container, controller=self)
        newFrame.configure(bg="#E0E0E0")
        newFrame.grid(row=0, column=0, sticky=tk.NSEW)

        # Add `newFrame` to catalog of frames.
        self.__frames[page_name] = newFrame
        

    def showFrame(self, page_name):
        """
        INPUT: view object.
        OUTPUT: None.

        Calls the view `page_name` up front for display.
        """

        try:
            # Bings requested view to the front.
            self.frames[page_name].tkraise()
        except KeyError:
            # Creates view and displays it.
            self.createFrame(page_name)
            self.frames[page_name].tkraise()


    def setLocation(self):
        """
        INPUT: None
        OUTPUT: None

        Description: Sets window in the middle of the screen.
        """
        self.widthWindow = 400
        self.heightWindow = 225
        widthScreen = self.winfo_screenwidth()
        hightScreen = self.winfo_screenheight()
        x = (widthScreen / 2) - (self.widthWindow / 2)
        y = (hightScreen / 2) - (self.heightWindow / 2)

        self.geometry("%dx%d+%d+%d" % (self.widthWindow, self.heightWindow, x, y))