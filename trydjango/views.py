"""
To render HTML web pages
"""

from django.http import HttpResponse
from articles.models import Article
import random
from django.template.loader import render_to_string




def home_view(request):
    """
    Take in a request (Django sends request) and 
    return HTML as response (We pick to return the response"""
    random_id = random.randint(1,2)
    # from the database
    article_obj = Article.objects.get(id=random_id)

    article_queryset = Article.objects.all()

    #Django template
    context = {
        'object_list' : article_queryset,
        'title' : article_obj.title,
        'content' : article_obj.content
    }

    # tmpl = get_templates('home-view.html')
    # tmpl_string = tmpl.render_to_string(context=context)

    HTML_STRING = render_to_string('home-view.html', context=context)

    # HTML_STRING ="""<h1>{title}</h1>
    # <p>{content}</p>""".format(**context)
    
    return HttpResponse(HTML_STRING)