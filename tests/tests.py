# Standard library imports
import unittest

# Third party imports
import pymysql
import pymysql.cursors

database_host = 'localhost'
database_user = 'root'
database_password = 'learn'
database_name = 'classicmodels'

connection = None
class Tests(unittest.TestCase):
    
    def test_connection(self):
        global connection
        try:
            connection = pymysql.connect(
                host=database_host,
                user=database_user,
                password=database_password,
                database=database_name,
                cursorclass=pymysql.cursors.DictCursor
            )
        except Exception:
            pass
        connection_details = f'Connection to datbase failed, are the connection details correct? host={database_host}, user={database_user}, password={database_password}, name={database_name}'
        self.assertTrue(connection is not None, connection_details)

if __name__ == '__main__':
    unittest.main()