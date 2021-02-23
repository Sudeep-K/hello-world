#! python3

# Random Chore Assignment Emailer.py -  takes a list of people’s email addresses and a list
# of chores that need to be done and randomly assigns chores to people

import smtplib, random

# asks user for email ID and password
user_email = input('Enter your gmail address.\n')
user_password = input('Enter your password.\n')

# connects to smtp server and logs in as user
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()
smtp_object.login(user_email, user_password)

# list of chores and email addresses to send chores to
chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
email_addresses = ['thisuserdoesnotexists1@example.com', 'thisuserdoesnotexists2@example.com', 'thisuserdoesnotexists3@example.com', 'thisuserdoesnotexists4@example.com']

# 'chore_dictionary' stores the 'email address' as key and the 'chore' as value
chore_dictionary = {}

# assigns random chore to each email address
for email in email_addresses:
	random_chore = random.choice(chores)
	chore_dictionary[email] = random_chore
	chores.remove(random_chore)

# sends email assigning 'chore' to each 'email address'
for email, chore in chore_dictionary.items():
	smtp_object.sendmail(user_email, email, 'Subject: Assigned Chore\n Dear, %s\n You have been assigned %s'%(email, chore))




