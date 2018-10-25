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

'''
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
