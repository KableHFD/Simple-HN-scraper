import requests
from bs4 import BeautifulSoup
import pprint

for i in range(0, 3):
	response = requests.get('https://news.ycombinator.com/news?p={}'.format(i+1))
	soup = BeautifulSoup(response.text, "html.parser")
	links = soup.select('.storylink')
	subtext = soup.select('.subtext')

	def sorted_by_points(hnlist):
		return sorted(hnlist, key = lambda k:k['vote'], reverse=True)

	def creat_custom_hn(links, subtext):
		hn = []
		for idx, item in enumerate(links):
			title = links[idx].getText()
			href = links[idx].get('href', )
			vote = subtext[idx].select('.score')
			if len(vote):
				points = int(vote[0].getText().replace(' points', ' '))
				if points > 99:
					hn.append({'title': title, "link": href, "vote": points})
		return sorted_by_points(hn)

	pprint.pprint(creat_custom_hn(links, subtext))

