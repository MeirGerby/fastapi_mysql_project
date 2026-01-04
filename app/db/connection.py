import mysql.connector
from mysql.connector import Error

from core.config import setting 

class DBCennection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBCennection, cls).__new__(cls)
            cls._instance._connect()
            return cls._instance
        
    def __init__(self):
        self._connection = None 
        
    def _connect(self): 
        try: 
            self._connection = mysql.connector.connect(
                host=setting.MYSQL_HOST,
                password=setting.MYSQL_PASSWORD,
                user=setting.MYSQL_USER, 
                port=setting.MYSQL_PORT 
            ) 
            if self._connection.is_connected():
                print("successfully connected to db")

        except Error as e:
            print("Error: can't connected to db", e)
            self._connection = None 

    def get_connection(self):
        return self._connection 
    
    def close_connection(self):
        if self._connection and self._connection.is_connected():
            self._connection.close()
            DBCennection._instance = None 
            print("MySQL connection closed")
