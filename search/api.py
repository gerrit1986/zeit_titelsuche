# coding: utf-8
import datetime
import requests


def buildNewsItems(query):
    """Returns news_items: a list containing tuples with
    0: title
    1: subtile
    2: href
    3: pub_date
    """
    title_query = 'title:' + unicode(query)
    params = {
        'q': title_query,
        'limit': '25',
        'fields': 'title,subtitle,href,release_date',
    }
    url = 'http://api.zeit.de/content?'
    headers = {'X-Authorization': 'API-KEY'}
    request = requests.get(url, params=params, headers=headers)
    json = request.json()
    news_items = []
    try:
        for result in json['matches']:
            pub_date = result['release_date']
            pub_date = pub_date[0:10] + ' ' + pub_date[11:-1]
            pub_date = datetime.datetime.strptime(pub_date, '%Y-%m-%d %H:%M:%S')
            news_items.append((result['title'], result['subtitle'], result['href'], pub_date))
    except (KeyError, ValueError):
        pass
    return news_items

print buildNewsItems('Merkel')