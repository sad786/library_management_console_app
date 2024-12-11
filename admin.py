import sqlite3

# add Admin User
def add_admin():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE role = 'admin'")
    if not cur.fetchone():
        cur.execute('INSERT INTO users (email,password,role) VALUES (?,?,?)',('admin@library.com','admin123','admin'))
        conn.commit()
        conn.close()

# adding user into database
def add_user(email,password,role):
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (email,password,role) VALUES (?,?,?)",(email,password,role))
    conn.commit()
    conn.close()


# add admin functions
def admin_menu():
    while True:
        print('\nAdmin Menu:')
        print('1. Add a Book')
        print('2. View Borrow Requests')
        print('3. Approve/Deny a Borrow Request')
        print('4. View User Borrow History')
        print('5. Add User Entry')
        print('6. Exit')
        # here we will ask choice of user
        choice = input('Enter your choice: ')
        if choice == '1':
            add_book()
        elif choice == '2':
            view_borrow_requests()
        elif choice == '3':
            approve_deny_requests()
        elif choice == '4':
            view_user_history()
        elif choice == '5':
            user_email = input('Enter Email of User: ')
            password = input('Enter Password: ')
            add_user(user_email,password,'user')
        elif choice == '6':
            break
        else:
            print('Invalid Choice! Please Enter a valid Choice')


# adding book 
def add_book():
    title = input('Enter book title: ')
    author = input('Enter author name: ')
    isbn = input('Enter book ISBN: ')

    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO books (title, author, isbn) VALUES (?,?,?)',(title,author,isbn))
        conn.commit()
        print('Book added successfully!')
    except sqlite3.IntegrityError:
        print('Book with this ISBN already exists.')
    conn.close()

# borrow book request
def view_borrow_requests():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute("""
            SELECT br.id, u.email,
                b.title, br.start_date, br.end_date, br.status
                FROM borrow_requests br JOIN users u ON br.user_id=u.id
                JOIN books b ON br.book_id = b.id
            """)
    request = cur.fetchall()
    conn.close()

    if request:
        for req in request:
            print(f"""Request ID: {req[0]}, User: {req[1]},
                  Book: {req[2]}, Dates: {req[3]} to {req[4]},
                  Status: {req[5]}""")
    else:
        print('No borrow requests found')

    
# Approve and Deny Request 
def approve_deny_requests():
    req_id = input('Enter request ID to approve/deny: ')
    action = input("Enter 'approve' or 'deny': ").lower()
    
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM borrow_requests WHERE id =?',(req_id,))
    req = cur.fetchone()

    if not req:
        print('Request not found')
        conn.close()
        return
    if action == 'approve':
        cur.execute("UPDATE borrow_requests SET status = 'Approved' WHERE id = ?",(req_id,))
        cur.execute("UPDATE books SET available = 0 WHERE id = ?",(req[2],))
        print('Request Approved!')
    elif action == 'deny':
        cur.execute("UPDATE borrow_requests SET status = 'Denied' WHERE id = ?",(req_id,))
        print('Request Denied!')
    else:
        print('Invalid action.')
    
    conn.commit()
    conn.close()

# View user History
def view_user_history():
    user_email = input('Enter user email: ')
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute("""
            SELECT b.title, bh.borrowed_date,
                bh.returned_date FROM borrow_history bh
                JOIN books b ON bh.book_id = b.id
                JOIN users u ON bh.user_id = u.id
                WHERE u.email = ?
                """,(user_email,))
    history = cur.fetchall()
    conn.close()

    if history:
        for record in history:
            print(f"""Book: {record[0]}, Borrowed: {record[1]},
                  Returned: {record[2] or 'Not Returned'}""")
    else:
        print('No borrow history found')
