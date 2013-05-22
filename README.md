## What's this? ##
It's a simple search interface for [ZEIT ONLINE](http://zeit.de).

## What does it do? ##
It searches for certain terms in headings of ZEIT articles and returns all hits in descending order by date.

## How does it work? ##
It was created using [Django](http://djangoproject.com) and [ZEIT ONLINE Content API](http://developer.zeit.de/index/).

## What is it good for? ##
It's a pet project for gaining skill in Python and Django. It might have useful features someday, e.g. search within
user-defined scopes (title, subtitle, text), clearly defined search operators and basic concept disambiguation.

## What's next? ##
* Summaries and full text should be searchable with respect to the user's choice
* The following search operators should work: (`""`; `*`; `NOT`; `AND`; `OR`; `XOR`)
* Basic concept disambiguation ("Do you mean ...?")
