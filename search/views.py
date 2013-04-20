# coding: utf-8

import datetime
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from api import buildNewsItems


def home(request):
    return HttpResponse("Hallo Besucher! Suchen Sie Texte in der ZEIT über Herrn <a href=\"/query/Steinbrück\">"
                        "Steinbrück?</a>")


def query(request, query):
    # processes all query results up to 25 max
    now = datetime.datetime.now()
    template = get_template('template.html')
    query = unicode(query)
    news_items = buildNewsItems(query)
    try:
        content = template.render(Context({'current_date': now,
                                           'query': query,
                                           'news_items': news_items, }))
    except IndexError:
        return HttpResponse("Für den Term „" + str(
            query) + "“ gibt es zu wenige Ergebnisse oder es ist ein technischer Fehler aufgetreten.")
    return HttpResponse(content)