from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse, Http404
from trails.models import Person
# Create your views here.

def checkperson(requests, numm):
	try:
		record = Person.objects.get(id=numm)
	except Exception:
		raise Http404("Person doesn't exist")
	records = record.first_name+" "+record.last_name
	return HttpResponse(records)


def bags(requests):
	return HttpResponse('bagsss')
