from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse, Http404
from trails.models import Person
import os
from django.conf import settings
from django.contrib.auth import authenticate, login
# Create your views here.


def log(request):
	uname = request.POST['username']
	pw = request.POST['password']
	user = authenticate(request, username = uname, password = pw)
	if user is not None:
		return HttpResponse("welcome!")
	else:
		return HttpResponse("wrong password")

def checkperson(requests, numm):
	try:
		record = Person.objects.get(id=numm)
	except Exception:
		raise Http404("Person doesn't exist")
	records = record.first_name+" "+record.last_name
	return HttpResponse(records)

def index_page(request):
	print("0step")
	if request.method == 'POST':
		print("1st step passed")
		username = request.POST['username']
		password = request.POST['password']
		print("2nd step")
		user = authenticate(request, username = username, password = password)
		if user is not None:
			print("3rd step")
			return HttpResponse("welcome!")
		else:
			print("3rd-2 step")
			return HttpResponse("wrong num")
	else:
		todpage = '/trails/person/download/'
		return render(request, 'trails/index.html', {'todpage':todpage})

def downloads(request):
	dpage = '../bags/'
	return render(request, 'trails/downloads.html', {'dpage':dpage})

def bags(requests):
    #file_path = 'media/MobileHome-master.zip'
    file_path = 'init'
    if not settings.DEBUG or not settings.NOT_ON_SERVER: 
        file_path = os.path.join(settings.MEDIA_ROOT,'MobileHome--master.zip')
    else:
        file_path = '/home/cup/Documents/tutorial/media/MobileHome--master.zip'
    print("*****",file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
    	    response = HttpResponse(fh.read(), content_type="application/zip")
    	    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
    raise Http404
