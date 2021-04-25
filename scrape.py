# isntall beautifulsoup4 library ( ALLOWS us to use HTML file and grab data for scarp it)
# also install requests library ( it allow us to grab HTMl files )

import requests
from bs4 import BeautifulSoup 
import pprint

res = requests.get('https://news.ycombinator.com/news') # get request to grab this page 1
res2 = requests.get('https://news.ycombinator.com/news?p=2') # for page 2
soup = BeautifulSoup(res.text,'html.parser') # use bs to cnvert this string in to object that we can manipulate and use ( modified data according to what we want!)
soup2 = BeautifulSoup(res2.text,'html.parser')

# res.text(string) will convert it in to object html.parser
# print(soup.find(id = "score_26931581")) # we can selectively pick what data we want
# like above we want to find score of this id which is 185 points

# print(soup.select('.score')) # it will grab all the class score on the page

links = soup.select('.storylink')
subtext = soup.select('.subtext')
# print(votes[0].get('id'))
# with bs we can keep chaining this 
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2
def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key= lambda k:k['votes'], reverse=True) # we use keys and pass it the key with votes to srort by votes using lambda function.




def create_custom_hn(links, subtext): #create a function for receive link and votes
  hn = []
  for idx, item in enumerate(links):
  	title = item.getText()
  	href = item.get('href', None)
  	vote = subtext[idx].select('.score')
  	if len(vote):

  	    points = int(vote[0].getText().replace('points', ''))
  	    if points > 99:
  	    	hn.append({'title': title , 'link':href,'votes': points}) # we grab the link and text
         
  return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))

