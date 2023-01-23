# Django 4.2 Lookup API demo

A small demo to try to play with the Lokup API from Django 4.2. 

Here are the main elements:

- A model with a datetime field `published_at`.
- A custom lookup `BooleanPastDate` that filter instances where the date is in the past.
- A list view (`BlogIndexView`) using the custom lookup.

This is pretty new, so I might be doing it wrong. Open to feedback!
