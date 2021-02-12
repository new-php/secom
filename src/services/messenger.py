import os
import bcrypt
import mysql.connector as mysql

from datetime import datetime
class Messenger:
    def __init__(self):
        self.DB = mysql.connect(
            host = os.environ.get('DB_HOST'),
            user = os.environ.get('DB_USER'),
            passwd = os.environ.get('DB_PSWD'),
            database = os.environ.get('DB')
        )

    def _prepare_args(f):
        def wrapper(self, table, *args):
            args = list(args)

            if table == 'user':
                if args[0] in self.get_all_users():
                    raise ValueError('El Usuario ya existe, intente otro.')
                args[1] = bcrypt.hashpw(args[1].encode('utf-8'), bcrypt.gensalt())
            elif table == 'project':
               pass 
            args = tuple(args)
            return f(self, table, *args)
        return wrapper

    @_prepare_args
    def insert_into(self, table, *args):
        """
        """
        cursor = self.DB.cursor(buffered=True)
        
        query = 'INSERT INTO '+\
            table+\
            ' ('+\
            ', '.join(self._describe(table))+\
            ')'+\
            ' VALUES ('+\
            ', '.join(['%s' for i in range(len(args))])+\
            ')'

        
        cursor.execute(
            query, 
            args
        )

        self.DB.commit()
        cursor.close()


    def get_all_users(self):
        cursor = self.DB.cursor(buffered=True)
        
        cursor.execute('SELECT user_name FROM user')

        result = tuple(row[0] for row in cursor)
        cursor.close()
        return result 


    def _describe(self, table):
       """
       """
       
       cursor = self.DB.cursor(buffered=True)
       cursor.execute('DESCRIBE ' + table )

       return (row[0] for row in cursor.fetchall()[1:])


    def check_credentials(self, user_name, ety_pswd):
        """
        INPUT: stringx2
        OUTPUT: string

        DESCRIPTION: checks for matching passwords returns user type
                     raises exeption otherwisde.

        EXEPTION RAISED: handdled in log_in_window.py 'login'.
        """
        password = self.get(user_name, 'pswd')
        if not bcrypt.checkpw(ety_pswd.encode('utf8'),password.encode('utf8')):
            raise ValueError('Usuario o contraseña incorrecta.')
        else:
            return self.get(user_name, 'user_type')


    def get(self, user_name, *args):
        """
        INPUT: tuple
        OUTPUT: tuple or EXEPTION VALUE ERROR

        DESCRIPTION: queries all requiered values in tuple input from given
                     `user_name'.

        EXEPTION RAISED: handdled in log_in_window.py 'login'.
        """
        cursor = self.DB.cursor(buffered=True)

        query = "SELECT " + ", ".join(args) + " FROM user WHERE user_name=%s"

        cursor.execute(
            query,
            (user_name, )
        )

        results = cursor.fetchall()
        cursor.close()

        if results:
            if len(args) == 1:
                if len(results) == 1: return results[0][0]
                else: return tuple(result[0] for result in results)
            else:
                if len(results) == 1: return results[0]
                else: return tuple(result for result in results)
        else:
            raise ValueError('Usiario o contraseña incorrecta.')

    def kardex_transaction(self, trans_type, quantity):
        print ("Checking function... (delete later)")

        cursor = self.DB.cursor(buffered=True)

        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        query = ("INSERT INTO kardex "
                "VALUES(%s,%s,%s,%s,%s,%s)")
        

        data = (1,1,1,100,formatted_date,3)


        cursor.execute(query,data)

        print("done...")
        return 1
