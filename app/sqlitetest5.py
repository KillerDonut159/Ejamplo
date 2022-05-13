from flask import Flask, render_template, request, redirect, url_for
from sqlite3 import connect, Row
from os import system
import json

def display_test5():
    open("test5.db", "w")
    db = connect("test5.db")
    c = db.cursor()
    c.execute("create table display1 (first text, last text)")
    c.execute("insert into display1 values ('spacea', 'spaceb')")
    db.commit()
    db.close()

def display_test5add(firstn, lastn):
    db = connect("test5.db")
    c = db.cursor()
    c.execute("insert into display1 values (?, ?)", (firstn, lastn))
    db.commit()
    db.close() 

def display_test5check():
    db = connect("/Users/federation/Downloads/github_repos/Ejamplo/test5.db")
    c = db.cursor()
    c.execute("select * from display1;")
    result = list(c.fetchall())
    db.close()
    return result

display_test5()