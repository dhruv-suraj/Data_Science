import requests
from bs4 import BeautifulSoup
import pandas as pd

topics_url="https://github.com/topics"
response=requests.get(topics_url)
# print(response.status_code)
# print(len(response.text))
page_contents=response.text
# print(page_contents[:1000])
with open('webpage.html', 'w') as f:
    f.write(page_contents)
#Using BeautifulSoup for web scrapping to get required data

doc=BeautifulSoup(page_contents , 'html.parser')
# print(type(doc))
topic_title_tags=doc.find_all('p',{'class':'f3 lh-condensed mb-0 mt-1 Link--primary'})
topic_desc_tags=doc.find_all('p',{'class':'f5 color-fg-muted mb-0 mt-1'})
# print(len(topic_desc_tags))
# print(topic_desc_tags[:5])
# topic_title_tag0=topic_title_tags[0]
# print(topic_title_tag0)
topic_link_tags=doc.find_all('a',{'class':'d-flex no-underline'})
# print(len(topic_link_tags))
# topic0_url="https://github.com" + topic_link_tags[0]['href']
# print(topic0_url)
topic_title=[]
for tag in topic_title_tags:
    topic_title.append(tag.text)
print(topic_title)

topic_desc=[]
for desc in topic_desc_tags:
    topic_desc.append(desc.text.strip())  #strip->removes empty space
print(topic_desc)

topic_url=[]
base_url='https://github.com'
for url in topic_link_tags:
    topic_url.append(base_url+url['href'])
print(topic_url)

topics_dict={
    'title':topic_title,
    'description':topic_desc,
    'url':topic_url
}

#Converting data in tabular format
topics_df=pd.DataFrame(topics_dict)
print(topics_df)

#Converting to csv
topics_df.to_csv('topics.csv',index=None)

#Getting information from a page
topics_page_url=topic_url[0]
print(topics_page_url)
response=requests.get(topics_page_url)
print(response.status_code)
topic_doc=BeautifulSoup(response.text,'html.parser')
repo_tags=topic_doc.find_all('h1',{'class':'f3 color-fg-muted text-normal lh-condensed'})
print(repo_tags)

def scrape_topics():
    topics_url = 'https://github.com/topics'
   response= requests.get(topics_url)
def scrape_topics_repo():
