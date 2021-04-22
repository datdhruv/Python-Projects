"""
The general format is as follows:
sqldesc = "DESC TABLE hello"
sqlcmd = "INSERT INTO hello(var1,var2,var3) VALUES (%s, %s, %s)"
# Check out https://stackoverflow.com/questions/20818155/not-all-parameters-were-used-in-the-sql-statement-python-mysql
values = (10, "hello", 12)

mycursor.execute(sqlcmd, values)

# For changes to show up:
mydb.commit()
"""
import mysql.connector as cn
# mysql stuff
mydb = cn.connect(
    host="192.168.1.146",
    port="3306",
    user="root",
    password="dhruv",
    database="lol"
)

mycursor = mydb.cursor()

def insert_generic(tablename, *args):
    # TODO: The values will change according to the insertion table,
    cmd = "INSERT INTO " + tablename + " (var1, var2, var3) VALUES (%s, %s, %s)"
    vals = (args[0], args[1], args[2])
    mycursor.execute(cmd, vals)

def delete_generic(*args):
    # TODO: The values will change according to the deletetion table
    # Ask teachers for a better way to handle that
    pass

def done():
    mydb.commit()