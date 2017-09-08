from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse, Http404
from trails.models import Person
import os
# Create your views here.

def checkperson(requests, numm):
	try:
		record = Person.objects.get(id=numm)
	except Exception:
		raise Http404("Person doesn't exist")
	records = record.first_name+" "+record.last_name
	return HttpResponse(records)

def index_page(request):
	return render(request, 'trails/index.html')

def bags(requests):
    file_path = os.path.join(settings.MEDIA_ROOT, 'MobileHome-master.zip')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/zip")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
