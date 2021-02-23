#! python3

# Auto Unsubscriber.py - scans through your email account, finds all the
# unsubscribe links in all your emails, and automatically opens them in a browser.

import imapclient, pyzmail, bs4, webbrowser

# asks user for login credentials.
user_email = input('Enter your email address.')
user_password = input('Enter your password.')

# connect to 'imap' server and login using the user credentials provided.
imapclient_object = imapclient.IMAPClient('imap.gmail.com', ssl = True)
imapclient_object.login(user_email, user_password)

# selects 'INBOX' folder from your email and search for all mails
imapclient_object.select_folder('INBOX', readonly = True)
UIDs = imapclient_object.search(['ALL'])

# fetch the body part of the mails and store the unique IDs to 'UIDs' list and stores raw_messages.
raw_messages = imapclient_object.fetch(UIDs, ['BODY[]'])

# decode messages from mail given using 'pyzmail' module
for UID in UIDs:
	message = pyzmail.PyzMessage.factory(raw_messages[UID][b'BODY[]'])

	if message.html_part != None:
		html_text = message.html_part.get_payload().decode(message.html_part.charset)
	
	# searches for the html_part of the message and pass it to 'beautiful soup'.
	# search then for all links in message
	soup = bs4.BeautifulSoup(html_text, 'lxml')
	link_elements = soup.select('a')

	# if the link selected is 'Unsubscribe' link then open them using 'webbrowser' module.
	for link_element in link_elements:
		if link_element.getText() == 'Unsubscribe':
			webbrowser.open(link_element.get('href'))