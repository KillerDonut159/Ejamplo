from sqlite3 import connect, Row
from os import system
import json

def display_test():
    open("test3.db", "w")
    db = connect("test3.db")
    c = db.cursor()
    c.execute("create table display1 (description text, number int)")
    c.execute("insert into display1 values('huge description', 11)")
    db.commit()
    db.close()

def display_test2():
    db = connect("/Users/federation/Downloads/github_repos/Ejamplo/test3.db")
    c = db.cursor()
    c.execute("select * from display1;")
    result = list(c.fetchall())
    db.close()
    return result

display_test()
#display_test2()

print(display_test2())