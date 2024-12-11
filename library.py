import sqlite3
from data_model import Database
from admin import *
from users import *  


# Login Functionality here
def login():
    email = input('Enter Email: ')
    password = input('Enter Password: ')

    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute("SELECT id, role FROM users WHERE email = ? AND password = ?",(email,password))
    user = cur.fetchone()
    conn.close()

    if user:
        #print(f"Welcome, {email}!")
        if user[1] == 'admin':
            print(f'Welcome, {email} (Admin)')
            admin_menu()
        else:
            print(f'Welcome, {email} (User)')
            user_menu(user[0])
    else:
        print('Invalid credentials.')

# here our programs will start 
if __name__ == '__main__':
    database = Database()
    database.setup_database()
    add_admin()

    while True:
        print('\n************* Library Management System *****************')
        
        print('1. Login')
        print('2. Exit')

        choice = input('Enter your choice: ')
        
        if choice == '1':
            #admin_or_user = input('Enter admin if you are Admin or User').lower().strip()
            login()

        elif choice == '2':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again')


        