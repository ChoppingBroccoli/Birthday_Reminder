'''
+-------------+
+ Psuedo Code +
+-------------+
Collect First and Last Name via user prompt
Collect Date of birthday (MM/DD/YYYY)
    Store information in a dictionary
    Write the dictionary to a text file
What is your relation to person?
How old is the person having the birthday?
Used Regex to validate input

Notifications
    Create alert (pop-up, notification, etc.) 2 weeks before date
    Create alert (pop-up, notification, etc.) 1 weeks before date
    Create alert (pop-up, notification, etc.) 5 days before date
    Create alert (pop-up, notification, etc.) 1 day before date

Once per day...
    Open the file
    Compare birthday against current date
        enable approprirate notification


Consider using shelf file objects vs dictionaries.
See the bookmark at https://www.udemy.com/automate/learn/v4/t/lecture/3470542?start=420

+------------------------+
+ List all keys in the   +
+ 'Birthdays' shelf file +
+------------------------+
list(birthdayShelf.keys())

+--------------------------+
+ List all values in the   +
+ 'Birthdays' shelf file   +
+--------------------------+
list(birthdayShelf.values())

'''

import shelve

# values are getting overwritten during each run because the keys already exist
# how to make the data persistent???
birthdayShelf = shelve.open('Birthdays') # creates the shelf file (Birthdays)
birthdayShelf['first_name'] = [input('Enter First Name: ')] # prompt for first name and store value in  'first_name' key
birthdayShelf['last_name'] = [input('Enter Last Name: ')] # prompt for last name and store value in 'last_name' key
birthdayShelf['relation'] = [input('Enter Relation: ')] # prompt for relationship and store value in 'relation' key
birthdayShelf['birthday'] = [input('Enter Birthday (MM/DD/YYYY): ')] # prompt for first name and store value in 'birthday' key
birthdayShelf.close()


'''

+------------------------------------------+
+ Code below was my first go at the        +
+ program. While studying Python I learned +
+ of the shelve module which can be used   +
+ in place of dict. Going to give shelve a +
+ try vs dict.                             +
+------------------------------------------+


# initialize varibles
myBirthdays = [] # first name, last name, relation, birthday
firstName = ''
lastName = ''
relation = ''
birthday = ''

# open BirthdayData.txt in append mode to write data to
# use writeBirthdays to store the data
# need to be able to write each dict key:value pair to the file
writeBirthdays = open('BirthdayData.txt', 'a')


# Ask user for input and append to the dictionary then write it to a file
# This needs to be in a loop or function. Otherwise, myBirthdays dict gets initialized at every run
myBirthdays.append({'firstName':input('What is the First Name? ')})
myBirthdays.append({'lastName':input('What is the Last Name? ')})
myBirthdays.append({'relation':input('What is your relationship? ')})
myBirthdays.append({'birthday':input('What is the birthday (MM/DD/YYYY)? ')})

print(myBirthdays)
'''
