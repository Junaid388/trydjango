from django.shortcuts import render
from articles.models import Article

# Create your views here.
def article_detail_view(request, id=None):
    # from the database
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)

    #Django template
    context = {
        'object' : article_obj,
    }
    return render(request, "articles/detail.html", context=context)