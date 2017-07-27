from django.shortcuts import render
from users.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.

#def index(request):
   # return render_to_response('users/index.html', {
  #      'events' : User.objects.all()[:5]
   # })