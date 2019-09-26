import bs4
import matplotlib.pyplot as plt
import wordcloud 
import requests
import numpy

url = input("Paste a wikipedia url here:")

#download html
req = requests.get(url)
req.raise_for_status()

#create soup object and use CSS selectors to get element
wikiSoup = bs4.BeautifulSoup(req.text, features="lxml")
text_elem = wikiSoup.select('p')

#iterate through text element and combine paragraphs
full_text = []
for par in text_elem: 
    full_text.append(par.getText().replace('\n', '').replace('\xa0', ' ')) 
full_text = ''.join(full_text)

#create and save wordcloud
wikiCloud = wordcloud.WordCloud().generate(full_text)
plt.imshow(wikiCloud)
plt.show()
plt.savefig('wikiCloud.png')