from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Tweet

# Create your views here.
def tweet_detail_view(request,tweet_id,*args,**kwargs):
    try:
        obj = Tweet.objects.get()
    except:
        raise Http404
    return HttpResponse(f"<h1>hello {tweet_id} - {obj.content}<h1>")
