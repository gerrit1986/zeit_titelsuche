# coding: utf-8
import datetime
import requests


def buildNewsItems(query):
    """
    Returns news_items: a list containing tuples which contains at indices

    0: title of the document
    1: subtitle of the document
    2: href to the document
    3: release_date of the document
    :param query: query given by the user via URL request
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
            # pretty date format
            release_date = result['release_date']
            release_date = release_date[0:10] + ' ' + release_date[11:-1]
            release_date = datetime.datetime.strptime(release_date, '%Y-%m-%d %H:%M:%S')
            # zip news items
            news_items.append((result['title'], result['subtitle'], result['href'], release_date))
    except (KeyError, ValueError):
        pass
    return news_items