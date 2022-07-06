#!/usr/bin/env python3
############################################################################################
#
# https://www.geeksforgeeks.org/generate-simple-ascii-tables-using-prettytable-in-python/
#
############################################################################################
# importing required library with pip3
from prettytable import PrettyTable

# creating an empty PrettyTable
x = PrettyTable()

# adding data into the table
# row by row
x.field_names = ["First name", "Last name", "Salary", "City", "DOB"]
x.add_row(["Shubham", "Chauhan", 60000, "Lucknow", "22 Feb 1999"])
x.add_row(["Saksham", "Chauhan", 50000, "Hardoi", "21 Aug 2000"])
x.add_row(["Preeti", "Singh", 40000, "Unnao", "10 Jan 1995"])
x.add_row(["Ayushi", "Chauhan", 65000, "Haridwar", "30 Jan 2002"])
x.add_row(["Abhishek", "Rai", 70000, "Greater Noida", "16 Jan 1999"])
x.add_row(["Dinesh", "Pratap", 80000, "Delhi", "3 Aug 1998"])
x.add_row(["Chandra", "Kant", 85000, "Ghaziabad", "18 Sept 1997"])

# printing generated table
print(x)
############################################################################################
# creating an empty PrettyTable
x = PrettyTable()

# adding data into the table
# column by column
x.add_column("First name",
             ["Shubham", "Saksham", "Preeti", "Ayushi",
              "Abhishek", "Dinesh", "Chandra"])

x.add_column("Last name", ["Chauhan", "Chauhan", "Singh",
                           "Chauhan", "Rai", "Pratap",
                           "Kant"])

x.add_column("Salary", [60000, 50000, 40000, 65000, 70000,
                        80000, 85000])
x.add_column("City", ["Lucknow", "Hardoi", "Unnao", "Haridwar",
                      "Greater Noida", "Delhi", "Ghaziabad"])

x.add_column("DOB", ["22 Feb 1999", "21 Aug 2000", "10 Jan 1995",
                     "30 Jan 2002", "16 Jan 1999", "3 Aug 1998",
                     "18 Sept 1997"])

# printing generated table
print(x)
############################################################################################
# creating an empty PrettyTable
x = PrettyTable()

# adding data into the table
# column by column
x.field_names = ["First name", "Last name", "Salary", "City", "DOB"]
x.add_row(["Shubham", "Chauhan", 60000, "Lucknow", "22 Feb 1999"])
x.add_row(["Saksham", "Chauhan", 50000, "Hardoi", "21 Aug 2000"])
x.add_row(["Preeti", "Singh", 40000, "Unnao", "10 Jan 1995"])
x.add_row(["Ayushi", "Chauhan", 65000, "Haridwar", "30 Jan 2002"])
x.add_row(["Abhishek", "Rai", 70000, "Greater Noida", "16 Jan 1999"])
x.add_row(["Dinesh", "Pratap", 80000, "Delhi", "3 Aug 1998"])
x.add_row(["Chandra", "Kant", 85000, "Ghaziabad", "18 Sept 1997"])

# With the start and end parameters, we can select
# which rows to display in the output.
print(x.get_string(start=2, end=4))

# With the fields option we can select columns
# which are going to be displayed.
print(x.get_string(fields=["First name", "Salary", "City"]))

############################### NOOK Table #################################################
print(chr(9556), end='')
for i in range(10):
    print(chr(9552), end='')
print(chr(9559))
for i in range(3):
    print(chr(9553), '        ', chr(9553))
print(chr(9562), end='')
for i in range(10):
    print(chr(9552), end='')
print(chr(9565))

