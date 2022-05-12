from sqlite3 import connect, Row
from os import system

def access_test():
    open("test2.db", "w")
    db = connect("test2.db")
    c = db.cursor()
    c.execute("CREATE TABLE tbl1 (one text, two int)")
    c.execute("INSERT INTO tbl1 values('this from python','heheheha')")
    db.commit()
    db.close()

def access_test2():
    open("/Users/federation/Downloads/github_repos/Ejamplo/test2.db", "w")
    db = connect("/Users/federation/Downloads/github_repos/Ejamplo/test2.db")
    c = db.cursor()
    c.execute("SELECT * FROM tbl1")
    db.close()

access_test()
access_test2()
