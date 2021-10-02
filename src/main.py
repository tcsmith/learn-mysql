import pymysql
import pymysql.cursors

def main():
    print('Hello MySQL World')

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='learn',
        database='classicmodels',
        cursorclass=pymysql.cursors.DictCursor
    )

    with connection:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM employees'
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)



if __name__ == '__main__':
    main()
