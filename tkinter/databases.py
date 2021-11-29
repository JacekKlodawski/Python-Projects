from tkinter import *
import sqlite3

root = Tk()
root.title('Databases')

#Create a db or connect one
conn = sqlite3.connect('clubs_list.db')

#Create cursor
c = conn.cursor()

#Create table
c.execute("""CREATE TABLE clubs (
    name string,
    city string,
    value float,
    year integer)""")

def submit():
    conn = sqlite3.connect('clubs_list.db')
    c = conn.cursor()
#Insert into table
    c.execute("INSERT INTO clubs VALUES (:name, :city, :value, :year)",
    {
        'name': name.get(),
        'city': city.get(),
        'value': value.get(),
        'year': year.get()
    })

    conn.commit()
    conn.close()

    #Clear the text boxes
    name.delete(0,END)
    city.delete(0,END)
    value.delete(0,END)
    year.delete(0,END)

#Create query function
def query():
    conn = sqlite3.connect('clubs_list.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM clubs")
    records = c.fetchall()
    print(records)
    


    conn.commit()
    conn.close()

#create text boxes
name = Entry(root, width=30).grid(row=0, column=1, padx=20)
city = Entry(root, width=30).grid(row=1, column=1, padx=20)
value = Entry(root, width=30).grid(row=2, column=1, padx=20)
year = Entry(root, width=30).grid(row=3, column=1, padx=20)

#Create text box labels
name_label = Label(root, text="name").grid(row=0, column=0, padx=20)
city_label = Label(root, text="city").grid(row=1, column=0, padx=20)
value_label = Label(root, text="value").grid(row=2, column=0, padx=20)
year_label = Label(root, text="year").grid(row=3, column=0, padx=20)

#Create Submit Buttons
submit_btn = Button(root, text="Add record to db", command=submit).grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create query button
query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Commit Changes
conn.commit()

#Close connection
conn.close()

root.mainloop()