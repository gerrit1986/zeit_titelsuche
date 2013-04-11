# coding: utf-8
import datetime
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from api import buildNewsItems

# homepage, 3 hardcoded items, old version
def home(home):
    now = datetime.datetime.now()
    template = get_template('template.html')
    news_items = buildNewsItems('Merkel')
    html = template.render(Context({'current_date': now,
                                    'query' : 'Merkel',
                                    'news_title1' : news_items[0][0],
                                    'news_title2' : news_items[1][0],
                                    'news_title3' : news_items[2][0],
                                    'news_link1' : news_items[0][2],
                                    'news_link2' : news_items[1][2],
                                    'news_link3' : news_items[2][2]}))
    return HttpResponse(html)

# query, length depends on number of results
def query(request, query):
    now = datetime.datetime.now()
    template = get_template('template.html')
    query = unicode(query)
    news_items = buildNewsItems(query)
    try:
        content = template.render(Context({'current_date': now,
                                        'query' : query,
                                        'news_items': news_items,}))
    except IndexError:
        # return messages.add_message(request, messages.INFO, 'Zu wenige Ergebnisse!')
        return HttpResponse("Ein Fehler ist aufgetreten. Für den Term „" + str(query) + "“ gibt es zu wenige "
                                                                                         "Ergebnisse.")
    return HttpResponse(content)