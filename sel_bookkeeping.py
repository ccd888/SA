import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = "student365admin",
                                  password = "Pa55w0rd",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "student365db")

    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from expense.bookkeeping"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from expense.bookkeeping table using cursor.fetchall")
    mobile_records = cursor.fetchall() 
   
    print("Print each row and it's columns values")
    for row in mobile_records:
       print("Id = ", row[0], )
       print("Financial Year = ", row[1])
       print("Name  = ", row[2], "\n")

except (Exception, psycopg2.Error) as error :
     print ("Error while fetching data from PostgreSQL", error)

finally:
     #closing database connection.
     if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
