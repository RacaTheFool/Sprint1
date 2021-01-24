# Overview

I wanted to demonstrate some simple database manipulation using Python with SQLite3. This includes the creation of tables in a database and adding, deleting, and updating information within those tables. I also demonstrate an inner join that takes the information that is the same in both tables and displaying the result.

I wanted to keep it simple by using only two tables (debtors and contacts). The debtors table has the name and total debt, while the contacts table has the name, phone, and address. The commonality between the two tables is the name, which is the table column used in the inner join mentioned above.

The user can manipulate the information in the tables using the Python program I wrote. The user is prompted to enter a number to select what they would like to do. The tables were both created beforehand using code that I commented out near the top (this program does not demonstrate adding or deleting columns from tables). I left that code in for those who don't already know the syntax to create a table in this format.

[Software Demo Video](https://youtu.be/HY7POGb3RRQ)

# Development Environment

* Visual Studio Code
* GitHub / Git
* Python
* SQLite3

# Useful Websites

* [W3Schools - SQL](https://www.w3schools.com/sql/)
* [W3Schools - Python](https://www.w3schools.com/python/default.asp)
* [Python SQLite3](https://docs.python.org/3.8/library/sqlite3.html)