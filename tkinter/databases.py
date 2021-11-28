from tkinter import *
import sqlite3

root = Tk()
root.title('Databases')

#Create a db or connect one
conn = sqlite3.connect('clubs_list.db')

#Create cursor
c = conn.cursor()

#Create table
c.execute("""CREATE TABLE clubs(
    name text,
    city text,
    value float,
    year integer)""")

#Commit Changes
conn.commit()

#Close connection
conn.close()

root.mainloop()