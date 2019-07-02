#!/usr/bin/python

# Bisham Singh
# June 27, 2019
#
# this script does the following:
#   (1) creates in in-memory SQL database
#   (2) extracts data from 2 Excel files and loads them to the SQL database
#   (3) gets user input and if the user input is in the list of state abbreviations,
#       extract the details from the database and write to user.
#
# TODO: more error checking

import pandas
import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()


def getList():
    global conn, c

    c.execute("create table states (abbreviation text, name text)")
    c.execute("create table mottos (state text, motto text)")

    df = pandas.read_excel('./states.xls')
    for a in df.values:
        # print a[0], a[1]
        c.execute("insert into states VALUES ('" + str(a[0].lower()) +
                  "','" + a[1] + "')")
    conn.commit()

    dm = pandas.read_excel('./motto.xls')
    for a in dm.values:
        # print a[0].strip(), a[1]
        c.execute("insert into mottos VALUES ('" + a[0].strip() +
                  "','" + a[1].replace("'", "''") + "')")
    conn.commit()

    return


def main():
    global c

    try:
        getList()

    except IOError, ValueError:
        print('An error occured trying to read files.')
        exit(1)

    except:
        print('An error occured.')
        exit(1)

    while True:
        name = raw_input('Enter input please: ')
        clean_name = name.strip().lower()
        query = "select s.name, m.motto from states as s " \
                "inner join mottos as m " \
                "on m.state = s.name " \
                "where s.abbreviation = '" + clean_name + "'"
        r = c.execute(query)
        state = "none"
        for a in r:
            state = a[0]
            motto = a[1]
        if state != "none":
            print name.upper() + " is " + state + ' with motto "' + motto + '"'
        else:
            print "I didn't find that state. Please try again."


main()
