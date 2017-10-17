from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse, Http404
from trails.models import Dashboard_news, Documents, Works, Profile 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
import os
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from .forms import Works_upload_form
# Create your views here.

def lost_street_index(request):
	userLogout = '../logout'
	data = {}
	data['userLogout'] = userLogout	
	data['userUrl'] = '../usr/dashboard'
	data['uploadForm'] = Works_upload_form
	if request.method == 'GET':
		return render(request, 'trails/loststreet.html', data)
	elif request.method == 'POST':
		form = Works_upload_form(request.POST, request.FILES)
		print (form)
		if form.is_valid():
			#form = Works_upload_form(request.POST, request.FILES)
			form.save()
			return HttpResponse('file uploaded successfully')
		else:
			return HttpResponse('file invalid!')
	else:
		return HttpResponse('failed to upload')	
		

def contri_index(request):
	userLogout = '../logout'
	data = {}
	data['userLogout'] = userLogout	
	data['userUrl'] = '../usr/dashboard'
	return render(request,'trails/contribute.html',data)

def user_register(request):
	userLogout = '../logout'
	data = {}
	data['userLogout'] = userLogout	
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		
		if form.is_valid():
			user = form.save(commit = False)
			username = form.cleaned_data['username']
			raw_password = form.cleaned_data['password1']
			user.set_password(raw_password)
			user.save()
			user_auth = authenticate(username = username, password = raw_password)
			user.set_password(raw_password)
			login(request, user_auth)

			return redirect('dash_board')
		else:
			return HttpResponse('invalid registration')
	else:
		form = UserCreationForm()
		data['userUrl'] = '../dashboard'
		data['form'] = form
		return render(request,'trails/register.html', data)

def index_page(request):
	if request.method == 'POST':
		# print("1st step passed")
		username = request.POST['username']
		password = request.POST['password']
		# print("2nd step")
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)		
#			return HttpResponse("welcome!")

#			return render
		else:
			return HttpResponse("wrong num")
	userUrl = '/trails/usr/dashboard'
	userLogout = '/trails/usr/logout'
	todpage = '/trails/person/download/'
	data = {'todpage':todpage,'userUrl':userUrl,'userLogout':userLogout }
	data['toHist'] = '/trails/con'
	data['lstreetUrl'] = '/trails/lstreet'
	return render(request, 'trails/index.html',data)

def log_user_out(request):
	logout(request)
	return redirect('index')
	
def downloads(request):
	dpage = '../bags/'
	return render(request, 'trails/downloads.html', {'dpage':dpage})

def dashboard(request):
	userUrl = '#'
	userLogout = '../logout'
	data = {}
	data['userUrl'] = userUrl
	data['userLogout'] = userLogout
	logged_user = None	

	if request.user.is_authenticated():
		data['groups'] = request.user.groups
		data['activity'] = Dashboard_news.objects.all().order_by('-time')[:15]
		data['profile'] = Profile.objects.get(user= request.user)
		print(data['profile'].headImg)
	return render(request,'trails/dashboard.html', data)

def bags(requests):
    #file_path = 'media/MobileHome-master.zip'
    file_path = 'init'
    if not settings.DEBUG or not settings.NOT_ON_SERVER: 
        file_path = os.path.join(settings.MEDIA_ROOT,'MobileHome--master.zip')
    else:
        file_path = '/home/cup/Documents/tutorial/media/MobileHome--master.zip'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
    	    response = HttpResponse(fh.read(), content_type="application/zip")
    	    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
    raise Http404
