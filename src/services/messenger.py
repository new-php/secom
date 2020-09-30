import mysql.connector as mysql

class Messenger:
    def __inti__(self, userName, pswd):
        self.DB = mysql.connect(
            host = "localhost",
            user = userName,
            passwd = pswd,
        )
        self.cursor = self.DB.cursor()

    # def logInToDB(self, userName, pswd):
    #     a = 1

    def createUser(self, nickName, firstName, fLastName, mLastName, pswd, typ, safeWord):
        self.cursor.execute(
            "INSERT INTO users(nickname, first_name, f_last_name, m_last_name, pswrd, type, safeword) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (nickName, firstName, fLastName, mLastName, pswd, typ, safeWord)
        )

        self.DB.commit()
