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
            (info[0], 
            bcrypt.hashpw(info[1], bcrypt.gensalt()),   #Hashing the password
            info[2],
            info[3], 
            info[4],
            info[5],
            info[6],
            info[7])
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