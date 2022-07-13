#connection setup
# mysql.connector to install, run pip install mysql-connector
import mysql.connector as databaseConnector

con = databaseConnector.connect(
    host = 'localhost',
    user = 'root',
    password = '310889',
    database = 'pythoncrud'
)

try:
    print(con.connection_id)
except:
    print('Connection establishment failed')