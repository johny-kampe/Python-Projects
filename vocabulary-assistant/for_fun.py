from tkinter import *
import sqlite3 as sql
from urllib.request import pathname2url

def submit():
    #creating database even if it doesn't exist!
    con = sql.connect('organization.db') 
    
    #create cursor
    c = con.cursor()
        
    if (not f_name.get()) and (not l_name.get()) and (not address.get()) and (not phone.get()): 
        print("Empty, give me information!")
    else:
        #insert into table
        c.execute("INSERT INTO worker VALUES(:f_name, :l_name, :address, :phone)",
                {'f_name':f_name.get(), 'l_name':l_name.get(), 
                'address':address.get(), 'phone':phone.get() 
                })
        
    #commit changes
    con.commit()
    
    #close connection
    con.close()
    
    #clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    phone.delete(0, END)
    
def query():

    #creating database even if it doesn't exist!
    con = sql.connect('organization.db') 
        
    #create cursor
    c = con.cursor()
 
    c.execute("SELECT *, oid FROM worker")
    records = c.fetchall()

    print(records)
    
    for count, i in enumerate(records):
        root = Tk()
        root.title('Worker ' + str(count+1))
        root.geometry('280x150')

        #create text boxes
        f_name = Entry(root, width=30)
        f_name.grid(row=0, column=1)

        l_name = Entry(root, width=30)
        l_name.grid(row=1, column=1)

        address = Entry(root, width=30)
        address.grid(row=2, column=1)

        phone = Entry(root, width=30)
        phone.grid(row=3, column=1)


        #create text box labels
        f_name_label = Label(root, text="First Name")
        f_name_label.grid(row=0, column=0)

        l_name_label = Label(root, text="Last Name")
        l_name_label.grid(row=1, column=0)

        address_label = Label(root, text="Address")
        address_label.grid(row=2, column=0)

        phone_label = Label(root, text="Phone number")
        phone_label.grid(row=3, column=0)

        
        f_name.insert(0, i[0])
        l_name.insert(0, i[1])
        phone.insert(0, i[2])
        address.insert(0, i[3])


    #commit changes
    con.commit()
        
    #close connection
    con.close()
    
def deletee():
    #creating database even if it doesn't exist!
    con = sql.connect('organization.db') 
        
    #create cursor
    c = con.cursor()
 
    #delete a record
    c.execute("DELETE FROM worker WHERE oid=" + delete.get())
    delete.delete(0, END)
    
    #commit changes
    con.commit()
        
    #close connection
    con.close()
    
def save():
    #creating database even if it doesn't exist!
    con = sql.connect('organization.db') 
        
    #create cursor
    c = con.cursor()  

    record_id = identity.get()

    c.execute("""UPDATE worker SET 
        first_name = :first, 
        last_name = :last,
        address = :address,
        phone_number = :phone

        WHERE oid = :oid""", { 
            'first':f_name.get(),
            'last':l_name.get(),
            'address': address.get(),
            'phone': phone.get(),
            'oid': record_id
            })

    #commit changes
    con.commit()
        
    #close connection
    con.close()

    root.destroy()

def update():
    global root
    root = Tk()
    root.title('Edit Data')
    root.geometry('280x200')

    #creating database even if it doesn't exist!
    con = sql.connect('organization.db') 
        
    c = con.cursor() #create cursor

    record_id = identity.get() #το record_id περιέψει το id που δόθηκε στο entry "Update ID"

    c.execute("SELECT * FROM worker WHERE oid = " + record_id) #παίρνουμε τα στοιχεία του worker με το id που δοθηκε
    records = c.fetchall() #βάζουμε τα στοιχεία στην μεταβλητή records
    
    con.commit() #commit changes
    
    con.close() #close connection

    global f_name  #create global variables for text box names
    global l_name
    global address
    global phone

    #create text boxes
    f_name = Entry(root, width=30)
    f_name.grid(row=0, column=1)

    l_name = Entry(root, width=30)
    l_name.grid(row=1, column=1)

    address = Entry(root, width=30)
    address.grid(row=2, column=1)

    phone = Entry(root, width=30)
    phone.grid(row=3, column=1)


    #create text box labels
    f_name_label = Label(root, text="First Name")
    f_name_label.grid(row=0, column=0)

    l_name_label = Label(root, text="Last Name")
    l_name_label.grid(row=1, column=0)

    address_label = Label(root, text="Address")
    address_label.grid(row=2, column=0)

    phone_label = Label(root, text="Phone number")
    phone_label.grid(row=3, column=0)

    for recordss in records: 
       f_name.insert(0, recordss[0])
       l_name.insert(0, recordss[1])
       address.insert(0, recordss[2])
       phone.insert(0, recordss[3])

    #create sumbit button
    save_button = Button(root, text="Save record", command=save)
    save_button.grid(row=7, column=0, columnspan=2, pady=10, ipadx=100)

#==============================================================================  
root = Tk()
root.title('Organization')
root.geometry('300x400')

#creating database even if it doesn't exist!
con = sql.connect('organization.db') 

#create cursor
c = con.cursor()

#checks if table worker exists
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='worker' ''')

#if the count is 1, then table exists
if c.fetchone()[0]==1:
	print('Table exists.')
else:
    print('No such table. Create it!')      
    c.execute("""CREATE TABLE worker(first_name text, last_name text, address text,
         phone_number integer)""")

#------------------------------CREATING GUI------------------------------
#create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

phone = Entry(root, width=30)
phone.grid(row=3, column=1)

delete = Entry(root, width=30)
delete.grid(row=4, column=1)

identity = Entry(root, width=30)
identity.grid(row=5, column=1)

#create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

phone_label = Label(root, text="Phone number")
phone_label.grid(row=3, column=0)

delete_label = Label(root, text="Delete ID")
delete_label.grid(row=4, column=0)

update_label = Label(root, text="Update ID")
update_label.grid(row=5, column=0)

#create sumbit button
submit_button = Button(root, text="Add to DB", command=submit)
submit_button.grid(row=7, column=0, columnspan=2, pady=10, ipadx=100)

#create a query button
query_button = Button(root, text="Show records", command=query)
query_button.grid(row=8, column=0, columnspan=2, pady=10,ipadx=92)

#create an update button
update_button = Button(root, text="Update record", command=update)
update_button.grid(row=9, column=0, columnspan=2, pady=10, ipadx=90)

#create a delete button
delete_button = Button(root, text="Delete record", command=deletee)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, ipadx=91)
#-----------------------------------------------------------------------


#commit changes
con.commit()

#close connection
con.close()

root.mainloop()
#==============================================================================