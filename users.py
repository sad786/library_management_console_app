import sqlite3

# User Functions
def user_menu(user_id):
    while True:
        print("\nUser Menu:")
        print("1. View Available Books")
        print("2. Request a Book")
        print("3. View Borrow History")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            view_available_books()
        elif choice =='2':
            request_book(user_id)
        elif choice == '3':
            view_user_borrow_history(user_id)
        elif choice == '4':
            break
        else:
            print("Invalid Choice! Please try again.")

# Viewing available books
def view_available_books():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute("SELECT id, title, author FROM books WHERE available = 1")
    books = cur.fetchall()
    conn.close()

    if books:
        for book in books:
            print(f"Book ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")
    else:
        print("No books available.")


# book request by given user id 
def request_book(user_id):
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    book_id = input('Enter book ID to request: ')
    start_date = input('Enter star date (YYYY-MM-DD): ')
    end_date = input('Enter end date (YYYY-MM-DD): ')

    cur.execute("SELECT available FROM books WHERE id = ?",(book_id,))
    book = cur.fetchone()

    if not book:
        print("Book not found: ")
    elif not book[0]:
        print('Book is not available.')
    else:
        cur.execute("""
            INSERT INTO borrow_requests (user_id, book_id, start_date, end_date,status)
            VALUES (?,?,?,?,?)""",(user_id,book_id,start_date,end_date,'not available'))
        cur.execute("""
            INSERT INTO borrow_history (user_id, book_id, borrowed_date)
            VALUES (?,?,?)""",(user_id,book_id,start_date))
        print('Book Request Successfull!')
        
    conn.close()  #closing the database connection

def view_user_borrow_history(user_id):
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute("""
            SELECT b.title, bh.borrowed_date, bh.returned_date
                FROM borrow_history bh JOIN books b ON bh.book_id = b.id
                WHERE bh.user_id = ?
                """,(user_id,))
    history = cur.fetchall()
    conn.close()
    
    if history:
        for record in history:
            print(f"Book: {record[0]},Borrowed: {record[1]},Returned: {record[2] or 'Not Returned'}")
    else:
        print('No Borrow history found')