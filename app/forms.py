from django import forms
from app.models import *

class Topicform(forms.Form):
     topic_name=forms.CharField()

class Webpageform(forms.Form):
     tl=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]

     topic_name=forms.ChoiceField(choices=tl)
     name=forms.CharField()
     url=forms.URLField()
     email=forms.EmailField()
class multiple(forms.Form):
     wl=[[to.pk,to.topic_name] for to in Webpage.objects.all()]
     topic_name=forms.MultipleChoiceField(choices=wl)