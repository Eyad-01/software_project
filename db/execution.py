import mysql.connector
from db.DBConnector import DBConnector

def execute(query):
    try:
        connector = DBConnector()
        mydb = connector.connect_database()
        if mydb.is_connected():
            my_cursor = mydb.cursor(dictionary=True)
            my_cursor.execute(query)

            if "SELECT" in query:
                result = my_cursor.fetchall()
                return result
            else:
                mydb.commit()
    except mysql.connector.Error as err:
        return f"Something went wrong: {err}"
    finally:
        if mydb.is_connected():
            my_cursor.close()
            mydb.close()
