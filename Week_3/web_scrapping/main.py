import pandas as pd
from bs4 import  BeautifulSoup
import requests
def get_topic_titles(doc):
    topic_title_tags = doc.find_all('p', {'class': 'f3 lh-condensed mb-0 mt-1 Link--primary'})
    topic_title = []
    for tag in topic_title_tags:
        topic_title.append(tag.text)
    return topic_title

def get_topic_desc(doc):
    topic_desc_tags = doc.find_all('p', {'class': 'f5 color-fg-muted mb-0 mt-1'})
    topic_desc = []
    for desc in topic_desc_tags:
        topic_desc.append(desc.text.strip())  # strip->removes empty space
    return topic_desc

def get_topic_url(doc):
    topic_link_tags = doc.find_all('a', {'class': 'd-flex no-underline'})

    topic_url = []
    base_url = 'https://github.com'
    for url in topic_link_tags:
        topic_url.append(base_url + url['href'])
    return topic_url

def scrape_topics():
    topics_url = 'https://github.com/topics'
    response = requests.get(topics_url)
    page_contents=response.text
    doc = BeautifulSoup(page_contents, 'html.parser')
    if response.status_code!=200:
        raise Exception('Failed to load the page{}'.format(topics_url))
    topics_dict={
        'title':get_topic_titles(doc),
        'description':get_topic_desc(doc),
        'url':get_topic_url(doc),
    }
    return pd.DataFrame(topics_dict)



def scrape_topics_repo():
    topic_df=