# coding: utf-8
# from datetime import datetime
import json
import requests
from django.contrib import messages


def buildNewsItems(query):
    """Returns news_items: a list containing tuples with
    0: title
    1: subtile
    2: href
    3: release_date
    """
    title_query = 'title:' + unicode(query)
    params = {
        'q' : title_query,
        'limit' : '3',
        'fields' : 'title,subtitle,href,release_date',
    }
    url = 'http://api.zeit.de/content?'
    headers = {'X-Authorization': 'YOUR API KEY'}
    request = requests.get(url, params=params, headers=headers)
    json = request.json()
    news_items = []
    try:
        for result in json['matches']:
            news_items.append((result['title'], result['subtitle'], result['href'], result['release_date']))
    except KeyError:
        pass
    return news_items


# What happens here? Try below to check:
# news = buildNewsItems('Merkel')

# print all results to the console
# try:
#     for result in json['matches']:
#         print 'Titel:', result['title']
#         print 'Untertitel:', result['subtitle']
#         print 'Link:', result['uri']
#         print '--------'
# except KeyError:
#     pass

    # some attempts to better time formatting
    # time = news[0][3]
    # print time
    # date = time[0:10]
    # clock = time[11:-1]
    # time = datetime.strptime(date + ' ' + clock, "%Y-%m-%d %H:%M:%S")
    # print time