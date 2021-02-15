#! python3

# ImageSiteDownloader.py - searches for a category of photos, and then downloads all the resulting images

import requests, bs4, webbrowser, os, sys

search_query = input('Enter the term you want to search.')

os.makedirs(search_query,exist_ok = True)

res = requests.get('https://imgur.com/search?q=' + search_query)
res.raise_for_status

soup = bs4.BeautifulSoup(res.text, 'html.parser')
element_list = soup.select('.image-list-link img')

if element_list == []:
	print('Could not find any search result image.')

else:
	for index in range(len(element_list)):
		image_url = element_list[index].get('src')
		print('Downloading image %s...' % (image_url))
		res = requests.get('https:' + image_url)
		res.raise_for_status

		image_file = open(os.path.join(search_query, image_url.split('/')[-1]), 'wb')
		for chunk in res.iter_content(100000):
			image_file.write(chunk)
		image_file.close()
