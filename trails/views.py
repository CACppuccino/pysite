from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse, Http404
from trails.models import Person
import os
from django.conf import settings
# Create your views here.


def checkperson(requests, numm):
	try:
		record = Person.objects.get(id=numm)
	except Exception:
		raise Http404("Person doesn't exist")
	records = record.first_name+" "+record.last_name
	return HttpResponse(records)

def index_page(request):
	todpage = '/trails/person/download/'
	return render(request, 'trails/index.html', {'todpage':todpage})

def downloads(request):
	dpage = '../bags/'
	return render(request, 'trails/downloads.html', {'dpage':dpage})

def bags(requests):
    #file_path = 'media/MobileHome-master.zip'
    file_path = os.path.join(settings.MEDIA_ROOT,'MobileHome--master.zip')
    #print("*****",file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
    	    response = HttpResponse(fh.read(), content_type="application/zip")
    	    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
    raise Http404
