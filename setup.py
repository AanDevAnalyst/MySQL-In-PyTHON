import mysql.connector
from database import cursor
from mysql.connector import errorcode


DB_NAME = sql_store
TABLES = {}

def create_database():
    cursor.execute (
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    
    print("Database {} Created !".format(DB_NAME))
    
def create_tables():
    cursor.execute("USE {}".format(DB_NAME))
    for table_name in TABLES:
        table_description = TABLES[table_name]
        
        try:
            print("Created table({})".format(table_name), end="")
            cursor.execute(table_description)
            
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXIST_ERROR:
                print("Table Already Exists")
                
            else:
                print(err.msg)
    
TABLES ['logs'] = (
    "CREATE TABLE 'logs' ("
    "'id' int(11) NOT NULL AUTO_INCREMENT",
    "'text' varchar(250) NOT NULL",
    "'user' varchar(250) NOT NULL",
    "'created' datetime NOT NULL DEFAULT CURRENT_TIMESTAMP",
    "PRIMARY KEY ('id')"
    ") ENGINE = InnoDB"
) 

TABLES ['customers'] = (
    "CREATE TABLE 'customers'("
    "'customer_id' int(11) NOT NULL AUTO_INCREMENT",
    "'first_name' varchar(50) NOT NULL",
    "'last_name' varchar(50) NOT NULL",
    "'birth_date' date NOT NULL",
    "'state'",
    "PRIMARY KEY ('id')"
    ") ENGINE = InnoDB"    
) 
    
create_database()
create_tables()