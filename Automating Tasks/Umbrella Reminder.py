#! python3

# Umbrella Reminder.py - runs just before you wake up in the morning and checks whether it’s raining that day

import requests, bs4, time
from twilio.rest import Client

url = 'https://forecast.weather.gov/MapClick.php?lat=37.7897&lon=-122.3957'

# gets the current time in seconds and increment it by 24 hours
trigger_time = time.time() + 86400
	
# this loop runs in an infinite loop checking time every seconds
while True:

	# if the current time is greater then the specified time then check the weather information and notify user
	if time.time() > time_now:
	
		# extract weather webpage using request and scrape the weather information using bs4 module
		res = requests.get(url)
		res.raise_for_status()

		soup = bs4.BeautifulSoup(res.text, 'lxml')
		matched_elements = soup.select('.short-desc')
		weather_today = matched_elements[0].text

		# asks user for user credentials
		account_SID = input('Enter your account SID.')
		auth_token = input('Enter your authentication token.')
		twilio_number = input('Enter your twilio number.')
		user_number = input('Enter your phone number you want to message.')

		# create a client_object using the user credential
		client_object = Client(account_SID, auth_token)

		# if the weather is 'rainy' them notify user to carry umbrella
		if str.lower(weather_today) == 'rainy':
			message = client_object.messages.create(body = 'Don\'t forget to carry umbrella it\'s %s'%(weather_today), from_ = twilio_number, to = user_number)

		# after completion of this block of code set the trigger time to 24 hours+ of current time.
		trigger_time += 86400

	# sleep the program every second
	time.sleep(1)
	