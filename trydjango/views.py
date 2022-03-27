"""
To render HTML web pages
"""

from django.http import HttpResponse




def home_view(request):
    """
    Take in a request (Django sends request) and 
    return HTML as response (We pick to return the response"""
    # from the database

    #Django template
    name = 'khan'
    HTML_STRING =f"""<h1>Hello {name}!</h1>"""
    return HttpResponse(HTML_STRING)