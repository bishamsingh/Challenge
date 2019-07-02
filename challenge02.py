#!/usr/bin/python

# Bisham Singh
# June 27, 2019
#
# this script does the following:
#   (1) gets a list of the words that are equivalent to "hello" from the website https://www.indifferentlanguages.com/words/hello
#   (2) gets user input and if the user input is in the list of words for hello returns "Greetings" otherwise "Sorry, I don't understand"
#
# TODO:

from lxml import html
import requests


def getList():
    hello_list = {}
    page = requests.get('https://www.indifferentlanguages.com/words/hello')
    tree = html.fromstring(page.content)
    for a in tree.xpath('//a[@class="translation-link "]'):
        hello_list[a.text.lower()] = 1
    if len(hello_list) <= 0:
        print "ERROR: Unable to download list"
        exit(1)
    return sorted(hello_list)


def main():
    h_list = getList()
    while True:
        name = raw_input('Enter input please: ')
        if name.strip().lower() in h_list:
            print "Greetings"
        else:
            print "Sorry, I don't understand"


main()
