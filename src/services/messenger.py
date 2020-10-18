import mysql.connector as mysql

class Messenger:
    def __init__(self, USER_DB, PSWD_DB):
        self.DB = mysql.connect(
            host = "localhost",
            user = USER_DB,
            passwd = PSWD_DB,
            database="secom"
        )
        self.cursor = self.DB.cursor()
        print("connected")

    def create_user(self, info):
        self.cursor.execute(
            "INSERT INTO users (user_name, "\
                        "pswd, "\
                        "hint, "\
                        "user_type, "\
                        "first_name, "\
                        "second_name, "\
                        "f_last_name, "\
                        "m_last_name) "\
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (info[0], info[1] ,info[2], info[3],
             info[4], info[5], info[6], info[7])
        )

        self.DB.commit()
