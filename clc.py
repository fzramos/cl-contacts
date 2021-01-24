"""
    Commamnd Line Contacts Book
    Do CRUD operations on a Phone Book
    Data saved via SQlite3 database
"""

from sys import argv, exit
import sqlite3

def main():

    # checking command line inputs
    if len(argv) != 3:
        print("This program requires 2 command line arguments."\
            + "\nOne for a csv file with people and their STRs."\
            + "\nOne for a csv file with the unidentified persons DNA sequence.")
        exit(1)

    # creating a connection
    conn = sqlite3.connect("contacts.db")
    # corsor object
    cursor = conn.cursor()
    

main()