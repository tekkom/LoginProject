from django.shortcuts import render
from events.models import Event
from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('events/index.html', {
        'events' : Event.objects.all()[:5]
    })
