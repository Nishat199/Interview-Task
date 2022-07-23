import pyodbc
class task1_insert:
def __init__(self, users.csv,DESKTOP-PKUTUC9,barikoi,usertask1):
# Connect to the database, perform the insert, and update the log table.
conn = self.connect_db(DESKTOP-PKUTUC9,barikoi)
        self.insert_data(conn,users.csv,usertask1)
        conn.close
def connect_db(self, DESKTOP-PKUTUC9,barikoi):
# Connect to the server and database with Windows authentication.
conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + DESKTOP-PKUTUC9 + ';DATABASE=' + barikoi+ ';Trusted_Connection=yes;'
        conn = pyodbc.connect(conn_string)
return conn
def insert_data(self, conn, users.csv, usertask1):
# Insert the data from the CSV file into the database table.

qry = "query = "INSERT INTO usertask1 (name,email,location,...)VALUES (Nishat, nishat@gmail.com, mirpur,...);""
# Execute the query
cursor = conn.cursor()
        success = cursor.execute(qry)
        conn.commit()
        cursor.close
