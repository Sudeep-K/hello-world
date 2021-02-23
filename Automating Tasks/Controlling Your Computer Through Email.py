#! python3

# Controlling Your Computer Through Email.py - checks an email account every 15 minutes for any
# instructions you email it and executes those instructions automatically

import imapclient, pyzmail, bs4, webbrowser, subprocess

imapclient._MAXLINES = 1000000

# asks for user credentials
user_email = input('Enter your email ID.')
user_password = input('Enter your password.')
from_email = input('Enter the email your are recieving from.')
torrent_file_path = input('Enter the path for "torrent.exe"')

# logs in to IMAP server using user credentials
imapclient_object = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapclient_object.login(user_email, user_password)

# searches for mail from the desired user
imapclient_object.select_folder('INBOX', readonly=True)
UIDs = imapclient_object.search('(FROM %s)'%(from_email))

# fetches the raw message from mail
raw_messages = imapclient_object.fetch(UIDs, ['BODY[]'])

# decodes the raw message to user readable form
for UID in UIDs:
	messages = pyzmail.PyzMessage.factory(raw_messages[UID][b'BODY[]'])

	# if the message has html_part save it to variable 'html_part'
	if messages.html_part != None:
		html_text = messages.html_part.get_payload().decode(messages.html_part.charset)
		file_name = messages.get_subject()
		print(file_name)

	# use beautiful soup to extract the torrent link
	soup = bs4.BeautifulSoup(html_text, 'lxml')
	link_elements = soup.select('a')

	# after extracting torrent link from the message use 'webbrowser' to download the torrent link
	for link_element in link_elements:
		torrent_link = link_element.get('href')
		webbrowser.open(torrent_link)

	# use subprocess module to 
	subprocess.Popen([torrent_file_path, file_name])




