import pyodbc

def get_driver(db_type):
    drivers = [x for x in pyodbc.drivers() if db_type in x]
    if not drivers:
        return None
    return "{"+drivers[-1]+"}"

def check_opt(options_original):   #boş bilgileri atıyor
    options_used = options_original.copy()
    for element in options_original:
        if options_used[element] == "":
            options_used.pop(element)
    return options_used

def compose_conn_string(driver,options_used):
    string = ["DRIVER="+driver]
    for key in options_used:
        line.append(key+"="+options_used[key])
    return ";".join(string)+";"

# option_dict = {"SERVER":"localhost","DATABASE":"db","Trusted_Connection":"yes"}
# conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=db;Trusted_Connection=yes;'

def read(conn):
    cursor = conn.cursor()
    cursor.execute("select * from dbo.MainTable")
    for row in cursor:
        print(f"row={row}")
        print()

# MS SQL SERVER
# conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=test;DATABASE=test;UID=user;PWD=password'

# MYSQL
# connection_string = (
#     'DRIVER=MySQL ODBC 8.0 ANSI Driver;'
#     'SERVER=localhost;'
#     'DATABASE=mydb;'
#     'UID=root;'
#     'PWD=mypassword;'
#     'charset=utf8mb4;'
# )

# SQLite
# cnxn = pyodbc.connect("Driver=SQLite3 ODBC Driver;Database=sqlite.db")

# Excel
# conn_str = (
#     r'DRIVER={Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)};'
#     r'DBQ=C:\path\to\myspreadsheet.xls;'
#     )

# option_dict = {"SERVER":"","DATABASE":"","UID":"","PWD":"","DBQ":"","Trusted_Connection":"","CHARSET":""}


# conn = pyodbc.connect(conn_string)
# conn_string = ";".join(["Driver="+driver_string,"Server="+server,"Database="+database,"Trusted_Connection=yes;"])
# conn = pyodbc.connect(
#     "DRIVER={ODBC Driver 17 for SQL Server};Server=.\SQLEXPRESS;Database=LogDB;Trusted_Connection=yes;"
# )


db_type = "SQL Server"
option_dictioary = {"SERVER":".\SQLEXPRESS","DATABASE":"LogDB","UID":"","PWD":"","DBQ":"","Trusted_Connection":"yes","CHARSET":""}
driver = get_driver(db_type)
options_necessary = check_opt(option_dictioary)
conn_string = compose_conn_string(driver,options_necessary)
conn=pyodbc.connect(conn_string)
read(conn)
