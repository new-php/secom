import mysql.connector as mysql

class Messenger:
    def __inti__(self, user_name, pswd):
        self.DB = mysql.connect(
            host = "localhost",
            user = user_name,
            passwd = pswd,
            database="secom"
        )
        self.cursor = self.DB.cursor()

    # def log_in(self, userName, pswd):
    #     a = 1

    def create_user(self, nick_name, first_name, f_last_name, m_last_name, pswd, typ, safe_word):
        self.cursor.execute(
            "INSERT INTO users(nickname, first_name, f_last_name, m_last_name, pswrd, type, safeword) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (nick_name, first_name, f_last_name, m_last_name, pswd, typ, safe_word)
        )

        self.DB.commit()
