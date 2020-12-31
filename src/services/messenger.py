import os
import bcrypt
import mysql.connector as mysql


class Messenger:
    def __init__(self):
        self.DB = mysql.connect(
            host = os.environ.get('DB_HOST'),
            user = os.environ.get('DB_USER'),
            passwd = os.environ.get('DB_PSWD'),
            database = os.environ.get('DB')
        )
        self.cursor = self.DB.cursor()

    def create_user(self, info):
        self.cursor.execute(
            "INSERT INTO users ( "\
                "user_name, "\
                "pswd, "\
                "hint, "\
                "user_type, "\
                "first_name, "\
                "second_name, "\
                "f_last_name, "\
                "m_last_name) "\
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (info[0],   # user_name. 
            bcrypt.hashpw(info[1], bcrypt.gensalt()),   #Hashing the password.
            info[2],    # hint.
            info[3],    # user_type.
            info[4],    # first_name.
            info[5],    # second_name.
            info[6],    # f_last_name.
            info[7])    # m_last_name.
        )

        self.DB.commit()

    def check_credentials(self, username,pswd):
        password = self.get_hashed_pswd(username)
        print(bcrypt.checkpw(pswd,password))

    def get_hashed_pswd(self, username):
        self.cursor.execute(
            "SELECT pswd FROM users WHERE user_name = 'test'"
        )

        return self.cursor.fetchone()[0]
        
        #test
        #Test001!