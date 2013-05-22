# coding: utf-8
import datetime
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from api import buildNewsItems


def home(request):
    """
    Displays a welcome response to the user.

    :param request: a request by the user from the root URL.
    """
    return HttpResponse("Hallo Besucher! Suchen Sie Texte in der ZEIT über Herrn <a href=\"/query/Steinbrück\">"
                        "Steinbrück?</a>")


def query(request, query):
    """
    Takes in a request and a query. Pulls content from the API according to the query and displays it to the page.

    :param request: a request by the user from the URL.
    :param query: a query given by the user via URL request.
    """
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

# moving towards class-based views
from django.views.generic import TemplateView

class ClassView(TemplateView):
    template_name = 'template.html'

    def get_context_data(self, **args):
        query = self.args[0]
        query = unicode(query)
        now = datetime.datetime.now()
        news_items = buildNewsItems(query)
        context = {'current_date': now,
                   'query': query,
                   'news_items': news_items, }
        return context