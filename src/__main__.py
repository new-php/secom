import os
from views.root import Root


if __name__ == '__main__':
    root = Root()

    root.views[root._conv("LIWind")].user_ety.insert(0, "josh-hdz")
    root.views[root._conv("LIWind")].pswd_ety.insert(0, os.environ.get("DB_PSWD"))
    root.views[root._conv("LIWind")].logIn_btn.invoke()

    
    root.mainloop()
