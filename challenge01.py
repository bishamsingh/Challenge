#!/usr/bin/python

def main():
    while True:
        name = raw_input('Enter your keyboard input: ')
        if (name.strip().lower() == "hello") or (name.strip().lower() == "hola")  or (name.strip().lower() == "hi"):
            print "Greetings"
        else:
            print "Sorry, I don't understand"

main()