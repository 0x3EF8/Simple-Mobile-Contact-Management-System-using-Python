import sqlite3
dbase = sqlite3.connect('contacts.db')
dbase.execute('create table if not exists' +
              ' contact(name text,contact text)')
cur=dbase.cursor()

def welcome():
    inn = input("All or New or Edit or Search or Delete: ")
    return inn.lower()
def check(sname):
    cur.execute(f'select name from contact where name="{sname}"')
    obj = cur.fetchone()
    if obj:
        return True
    else:
        return False
def valid_no(sname):
    while True:
        scontact = input(f"Enter {sname}'s phone no: ")
        if len(scontact)== 10 or len(scontact)== 8:
            return scontact
        else:
            print("Number is invalid.")

def delete():
    sname = input('Enter the name to be deleted: ')
    sname = sname.title()
    if check(sname):
        cur.execute(f"delete from contact where name='{sname}'")
        print("Delete successful")
    else:
        print(f"No contact exist named '{sname}'")
    dbase.commit()
def new():
    sname = input("Enter new contact name: ")
    sname = sname.title()
    scontact=valid_no(sname)
    cur.execute('insert into contact values(?,?)',
                (f'{sname}', f'{scontact}'))
    print("new contact added!")
    dbase.commit()
def all():
    cur.execute('select * from contact')
    obj = cur.fetchall()
    if obj==None:
        print("No contact exist!")
    for a in obj:
        print('name: ', a[0], ' no: ', a[1])
    dbase.commit()


def update_number():
    sname = input("Enter the contact name to be updated: ")
    sname = sname.title()
    if check(sname):
        scontact = valid_no(sname)
        cur.execute(f'update contact set contact="{scontact}" where name="{sname}"')
        print("update successful")
    else:
        print(f"No contact exist named {sname}")
    dbase.commit()


def update_name():
    snum = input("Enter the contact number to be edited: ")
    sname = input("Enter the new contact name: ")
    cur.execute(f'select name from contact where contact="{snum}"')
    obj=cur.fetchone()
    if obj:
        cur.execute(f'update contact set name="{sname.title()}" where contact="{snum}"')
        print("update successful")
    else:
        print(f"No contact exist which has number: {snum}")
    dbase.commit()

def search_number():
    snum = input("Enter the contact number to be searched: ")
    cur.execute(f'select name from contact where contact like "%{snum}%"')
    obj = cur.fetchone()
    if obj:
        obj = obj[0]
        print("name: ", obj)
        cur.execute(f'select contact from contact where name="{obj}"')
        obj = cur.fetchone()
        print("contact: ", obj[0])
    else:
        print(f"No contact exist which has number: {snum}")
    dbase.commit()

def search_name():
    sname = input("Enter the contact name to be searched: ")
    cur.execute(f'select name from contact where name like "%{sname}%"')
    obj=cur.fetchone()
    if obj:
        obj = obj[0]
        print("name: ",obj)
        cur.execute(f'select contact from contact where name="{obj}"')
        obj=cur.fetchone()
        print("contact: ",obj[0])
    else:
        print(f"No contact exist which named: {sname}")
    dbase.commit()


#main
print("WELCOME to Mobile Contact Management System")
while(True):
    inn = welcome()
    if inn=='new':
        new()
    elif inn=='all':
        all()
    elif inn=='edit':
        while True:
            i = input("Edit name or number: ")
            if i=='name':
                update_name()
                break
            elif i=='number' or i=='num':
                update_number()
                break
            else:
                print("Select from the option")
    elif inn=='search':
        while True:
            i = input("Search name or number: ")
            if i=='name':
                search_name()
                break
            elif i=='number' or i=='num':
                search_number()
                break
            else:
                print("Select from the option")
    elif inn=='delete':
        delete()
    elif inn=='exit':
        print('VISIT AGAIN!!')
        break
    else:
        print("Select from the option")

dbase.close()



