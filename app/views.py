from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

from app.forms import *

def topic(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            to=Topic.objects.get_or_create(topic_name=tn)[0]
            to.save()

            QLTO=Topic.objects.all()
            d1={'Topic':QLTO}
            return render(request,'display_topic.html',d1)
        else:
            return HttpResponse('invalid data')
    return render(request,'inserttopic.html',d)

def webpage(request):
    EWFO=Webpageform()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=Webpageform(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            e=WFDO.cleaned_data['email']

            wo=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
            wo.save()

            QLWO=Webpage.objects.all()
            d1={'Webpage':QLWO}

            return render(request,'dispaly_webpage.html',d1)
    return render(request,'insertwebpage.html',d)

def multiple(request):
    QLWO=Webpage.objects.all()
    d={'Webpage':QLWO}
    
    return render(request,'dispaly_webpage.html',d)