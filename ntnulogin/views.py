from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from events.models import Event

def index(request):
    return render(request, 'ntnulogin/home.html')

#def renderEvent(request):
#    return TemplateResponse(request, 'events/plugins/event_plugin.html', {})
