import env as databaseLink

#installation of cursor object
curobj = databaseLink.con.cursor()

#database creation
databaseName = "create database pythoncrud"
# curobj.execute(databaseName)

#use database
useDatabase = "use pythoncrud"
curobj.execute(useDatabase)

#table creation
userTable = """create table users(
    user_id integer(11) AUTO_INCREMENT PRIMARY KEY,
    firstname varchar(100),
    lastname varchar(100),
    email varchar(100),
    created_at timestamp default current_timestamp)"""
# curobj.execute(userTable)

#insert operation
insertUser = "Insert into users (firstname, lastname, email, created_at) values (%s, %s, %s, %s)"
userVal1 = ('Ranveer', 'Yadav', 'yadavranveerp@gmail.com', '2022-07-08')
userVal2 = ('Ram', 'Yadav', 'yadavramp@gmail.com', '2022-07-08')
userVal3 = ('Raj', 'Yadav', 'yadavrajp@gmail.com', '2022-07-08')
# curobj.execute(insertUser, userVal1)
# curobj.execute(insertUser, userVal2)
# curobj.execute(insertUser, userVal3)
# databaseLink.con.commit()

#insert multiple entries in single query
insertUser = "Insert into users (firstname, lastname, email) values (%s, %s, %s)"
singleInsert = [
    ('Yellow', 'Colour', 'yellowcolour@gmail.com'),
    ('Green', 'Colour', 'greencolour@gmail.com'),
    ('Blue', 'Colour', 'bluecolour@gmail.com')
]
# curobj.executemany(insertUser, singleInsert)
# databaseLink.con.commit()

#select operation
userSelect = "Select * from users where created_at like '%2022%'"
curobj.execute(userSelect)
userResult = curobj.fetchall()
for user in userResult:
    print(user)

#update operation
userUpdate = 'Update users set firstname = "Green" where firstname = "Blue"'
curobj.execute(userUpdate)
databaseLink.con.commit()

#select operation after update
userSelectAfterUpdate = "Select * from users where firstname = 'Green'"
curobj.execute(userSelectAfterUpdate)
userUpdateResult = curobj.fetchall()
for userUpdate in userUpdateResult:
    print(userUpdate)

#delete operation
userDelete = 'Delete from users where firstname = "Green"'
curobj.execute(userDelete)
databaseLink.con.commit()