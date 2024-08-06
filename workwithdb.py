import sqlite3

def newuser(username,name,rost,weight):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username,name, rost, weight) VALUES (?, ?, ?, ?)', (f'{username}', f'{name}',rost,weight))
    connection.commit()
    connection.close()
def find_userinfo(username,parametr):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Users WHERE username LIKE '{username}' ")
    records = cursor.fetchall()
    try:
        spisok = records[0]
    except Exception as ex:
        print("Error")
        spisok = ["","","","",""]
    print(spisok)
    if parametr==0:
        return spisok[0]
    elif parametr == 1:
        return spisok[1]
    elif parametr == 2:
        return spisok[2]
    elif parametr == 3:
        return spisok[3]
    elif parametr == 4:
        return  spisok[4]
    connection.commit()
    connection.close()
