from views.root import Root
from views.log_in_window import LogInWind as LIWind


if __name__ == '__main__':
    root = Root()

    root.showFrame("LIWind")
    
    root.mainloop()