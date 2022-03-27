"""
To render HTML web pages
"""

from django.http import HttpResponse

HTML_STRING ="""
<h1>Hello World</h1>"""


def home(request):
    """
    Take in a request (Django sends request) and 
    return HTML as response (We pick to return the response"""
    return HttpResponse(HTML_STRING)