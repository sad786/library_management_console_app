""""
Here is the details about this Library Mangement System App

1. All the database creation functionality is in data_model.py
    1. Database name is library 
    2. There are 4 Tables in library database
    3. a. Users table include columns id which autoincrement means it will be set up by database itself when user
            entry is created 
        email of the user, password and role mean either he is user or admin

    4. Second table is books having coulumns id which is autoincrement in nature
        title, isbn which is unique id of the book, authro of the book and available status 
    
    5. Third table is borrow_reqest which having the details about who borrwed the book and their start date and end date
    6. Fourth table is borrow_history which will have details of the book taken by each user


2. Main File is library.py 
    from this file app will start and user will have an option to enter their login details
    then detabase will check if the user is admin or simple user with details must be correct
    then corresponding feature will appear for admin or user

3. Admin will have the functionality to 
    1. Add a book into the library
    2. approve or deny request
    3. View User borrow history
    4. Adding New User to the library

4. User file users.py have the following functinality
    1. View Available Books
    2. Request a book
    3. view borrow history

5 ....

"""