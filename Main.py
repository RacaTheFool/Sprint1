import sqlite3

connection = sqlite3.connect('Sprint1/debtors.db')
cursor = connection.cursor()

# I used this originally to create the "debtors" database
# cursor.execute("CREATE TABLE debtors (name text, debt real)")

# I used this originally to create the "contacts" database
# cursor.execute("CREATE TABLE contacts (name text, phone text, address text)")


# The user can display the debtors, add a debtor, update
# a debtors balance, delete a debtor, or exit the program.
selection = None
while selection != "0":
    print("1) Display Debtors")
    print("2) Add Debtor")
    print("3) Update Debtors Balance")
    print("4) Delete Debtor")
    print("5) Display Contacts")
    print("6) Add Contact Info for Debtor")
    print("7) Update Debtors Contact Info")
    print("8) Delete Contact")
    print("9) Display Debtors With Contacts that Share the Same Name")
    print("0) Quit")
    selection = input("> ")
    print()
    if selection == "1":
        # Display Debtors
        cursor.execute("SELECT * FROM debtors ORDER BY debtors.name")
        print("{:>25}  {:>25}".format("Name", "Debt"))
        for record in cursor.fetchall():
            print("{:>25}  {:>25}".format(record[0], record[1]))
    elif selection == "2":
        # Add New Debtor
        name = input("Name: ")
        goodInput = False
        # To ensure that the user puts in a valid [float] I
        # use a [try...except] to prevent the program from
        # closing due to incorrect input and prompt the
        # user until they put in something valid.
        debt = None
        while goodInput == False:
            try:
                debt = float(input("Debt: "))
                goodInput = True
            except:
                print("Invalid input")
                goodInput = False
        values = (name, debt)
        cursor.execute("INSERT INTO debtors VALUES (?,?)", values)
        connection.commit()
    elif selection == "3":
        # Update Debtors Debt
        option = None
        print("1) Loan")
        print("2) Payment")
        option = input("> ")
        if option == "1":
            # Debtor Took out another Loan
            name = input("Name: ")
            # To ensure that the user puts in a valid [float] I
            # use a [try...except] to prevent the program from
            # closing due to incorrect input and prompt the
            # user until they put in something valid.
            goodInput = False
            loan = None
            while goodInput == False:
                try:
                    loan = float(input("Loan: "))
                    goodInput = True
                except:
                    print("Invalid input")
                    goodInput = False
            values = (loan, name) # Make sure order is correct
            cursor.execute("UPDATE debtors SET debt = debt + ? WHERE name = ?", values)
            connection.commit()
        elif option == "2":
            # Debtor is Paying Off Part of Their Debt
            name = input("Name: ")
            # To ensure that the user puts in a valid [float] I
            # use a [try...except] to prevent the program from
            # closing due to incorrect input and prompt the
            # user until they put in something valid.
            goodInput = False
            payment = None
            while goodInput == False:
                try:
                    payment = float(input("Payment: "))
                    goodInput = True
                except:
                    print("Invalid input")
                    goodInput = False
            values = (payment, name) # Make sure order is correct
            cursor.execute("UPDATE debtors SET debt = debt - ? WHERE name = ?", values)
            connection.commit()
    elif selection == "4":
        # Delete debtor
        name = input("Name: ")
        values = (name, )
        cursor.execute("DELETE FROM debtors WHERE name = ?", values)
        connection.commit()
    elif selection == "5":
        # Displays Contacts
        cursor.execute("SELECT * FROM contacts ORDER BY contacts.name")
        print("{:>25}  {:>25} {:>25}".format("Name", "Phone", "Address"))
        for record in cursor.fetchall():
            print("{:>25}  {:>25} {:>25}".format(record[0], record[1], record[2]))
    elif selection == "6":
        # Create New Contact
        name = input("Name: ")
        phone = input("Phone: ")
        address = input("Address: ")
        values = (name, phone, address)
        cursor.execute("INSERT INTO contacts VALUES (?, ?, ?)", values)
        connection.commit()
    elif selection == "7":
        # Update Contact Info
        option = None
        print("1) Update Phone")
        print("2) Update Address")
        option = input("> ")
        if option == "1":
            # Update Phone
            name = input("Name: ")
            phone = input("Phone: ")
            values = (phone, name) # Make sure order is correct
            cursor.execute("UPDATE contacts SET phone = ? WHERE name = ?", values)
            connection.commit()
        elif option == "2":
            # Update Address
            name = input("Name: ")
            address = input("Address: ")
            values = (address, name) # Make sure order is correct
            cursor.execute("UPDATE contacts SET address = ? WHERE name = ?", values)
            connection.commit()
    elif selection == "8":
        # Delete Contact Info
        name = input("Name: ")
        values = (name, )
        cursor.execute("DELETE FROM contacts WHERE name = ?", values)
        connection.commit()
    elif selection == "9":
        # Display Both Tables Together For Each Name That is Found in Both
        cursor.execute("SELECT debtors.*, contacts.phone, contacts.address From debtors INNER JOIN contacts ON debtors.name = contacts.name ORDER BY debtors.name")
        print()
        print("{:>25}  {:>25} {:>25} {:>25}".format("Name", "Debt", "Phone", "Address"))
        for record in cursor.fetchall():
            print("{:>25}  {:>25} {:>25} {:>25}".format(record[0], record[1], record[2], record[3]))
        print()
    print()

# Close the database connection before exiting
connection.close()