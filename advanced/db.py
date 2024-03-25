import pymssql

# Replace placeholders with your actual connection details
server_address = 'DESKTOP-7H7GACC\\SQLSERVER'
username = 'martin'
password = 'iii'
database_name = 'testing_db'

# Connect to the SQL Server
conn = pymssql.connect(
    server=server_address,
    user=username,
    password=password,
    database=database_name,
    as_dict=True
)

mycursor=conn.cursor()

mycursor.execute("select id,name,age from staffdet")

for x in mycursor:
    print(x)


# Execute queries or perform other database operations
# ...

# Close the connection when done
# conn.close()
