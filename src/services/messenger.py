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

    def create_user(self, info):
        """
        INPUT: tuple.
        OUTPUT: nome.

        DESCRIPTION: Inserts user info to user table in DB. It hashes pswd 
                     before sending.
        """
        cursor = self.DB.cursor(buffered=True)
        
        cursor.execute(
            "INSERT INTO user ( "\
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
            bcrypt.hashpw(info[1].encode('utf-8'), bcrypt.gensalt()),   #Hashing the password.
            info[2],    # hint.
            info[3],    # user_type.
            info[4],    # first_name.
            info[5],    # second_name.
            info[6],    # f_last_name.
            info[7])    # m_last_name.
        )

        self.DB.commit()
        cursor.close()



    def check_credentials(self, user_name, ety_pswd):
        password = self.get("pswd", user_name)
        """
        INPUT: stringx2
        OUTPUT: bool

        DESCRIPTION: returns True if `ety-pswd` matches with retireved pswd from
                     DB, else returns False. 
        """
        password = self.get(("pswd",), user_name)[0]
        return bcrypt.checkpw(ety_pswd.encode('utf8'),password.encode('utf8'))
    


    def get(self, value, user_name):
    def get(self, values, user_name):
        """
        INPUT: tuple
        OUTPUT: tuple or EXEPTION VALUE ERROR

        DESCRIPTION: queries all requiered values in tuple input from given
                     `user_name'.
        """
        cursor = self.DB.cursor(buffered=True)

        cursor.execute(
            ("SELECT " + value + " FROM user WHERE user_name='%s'"),
            (user_name, )
        )



        if cursor.rowcount == 1:
            pswd = cursor.fetchone()[0]
            cursor.close()
            return pswd
        else:
            raise ValueError("User not found.")