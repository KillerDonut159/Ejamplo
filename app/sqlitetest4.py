from sqlite3 import connect, Row
from os import system
import json

def display_test():
    open("test4.db", "w")
    db = connect("test4.db")
    c = db.cursor()
    c.execute("create table display1 (description text, number int)")
    c.execute("insert into display1 values('huge html description', 100)")
    db.commit()
    db.close()
    return 4

def display_test2():
    db = connect("/Users/federation/Downloads/github_repos/Ejamplo/test4.db")
    c = db.cursor()
    c.execute("select * from display1;")
    result = list(c.fetchall())
    db.close()
    return 1

def display_test3():
    db = connect("/Users/federation/Downloads/github_repos/Ejamplo/test4.db")
    c = db.cursor()
    c.execute("select * from display1;")
    result = list(c.fetchall())
    db.close()
    return result

display_test()
#display_test2()

python = display_test3()
print(python)

print('Conversion moment?')

convert = json.dumps(python)
print(convert)