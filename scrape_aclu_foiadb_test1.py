
from bs4 import BeautifulSoup

import requests, json, time

node = 7777

foia_list = []

while node >= 7766:

	url = "https://www.thetorturedatabase.org/rest/fullnode/retrieve?nid=" + str(node)
	print("scraping now!",url,"hooray")
	painting_page = requests.get(url)

	page_html = painting_page.text


	soup = BeautifulSoup(page_html, "html.parser")

	all_titles = soup.find_all("type", "title")

	for a_title in all_titles:

		the_a_link = a_title.text

		the_title = the_a_link.text
		the_link = the_a_link.text

# make an empty dictionary
		obj = {}

		# define key for the dictionary and its value
		obj['title'] = the_title
		obj['type'] = the_link

		# add these into the list defined at the beginning]

		foia_list.append(obj)


	node = node - 1

# if put json.dump at indent of page loop adding 1 then it will happen each page
# if put no indent it will only write the dump at end

	json.dump(foia_list,open('foia_list.json','w'),indent=2)

# to sleep between each loop
	time.sleep(1)


#returns a list of divs
# title element gets treated like a dictionary
# while loop  - lets us go through all the search result pages

