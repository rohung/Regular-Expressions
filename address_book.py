from person import Person
import re
import sys


names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()


class Address():

    def search_entries(self):
        # using regular expression patterns and grouping into name groups. 
        line = re.compile(r'''
            ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t #Last and first names
            (?P<email>[-\w\d.+]+@[-\w\d.]+)\t #Email
            (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #Phone 
            (?P<job>[\w\s]+,\s[\w\s.]+)\t? #Job and company
            (?P<twitter>@[\w\d]+)?$ #Twitter
           ''', re.X|re.M)
        
        #prompts the user for an input and make the first letter of the word uppercase.
        search_person = input("Enter the first or last name: ").title()
        person = Person()
        if any(search_person in names for names in line.findall(data)):
            for match in line.finditer(data):     
                if search_person in match.groupdict()['name'].title().replace(',', ''):
                    person.name = match.groupdict()['name']
                    person.email = match.groupdict()['email'] 
                    person.phone = match.groupdict()['phone']
                    person.job = match.groupdict()['job']
                    person.twitter = match.groupdict()['twitter']
                    print(person)
                    
        else: 
            next_step = input("{} was not found. Enter [y]es to try again or [q]uit to exit ".format(search_person))
            if next_step.lower() == 'q':
                sys.exit()
            else:
                self.search_entries()
    
    #prompts user for 's' or 'q' input
    def __init__(self):
        start_input = input("Welcome! Enter [s]earch to look up an " +
                            "address book entry or [q]uit to quit!").lower()

        if start_input == 'q':
            sys.exit()
        else:
            repeat = True
            while repeat != 'q':
                self.search_entries()    
                print('\n'+'='*20)
                repeat = input("[S]earch again or [q]uit!").lower()
            sys.exit()


Address()