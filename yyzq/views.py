from django.shortcuts import render
from django.http import Http404, HttpResponse
import datetime

def index(request):
	now = datetime.datetime.now()
	return render(request, 'index.html', {'current_time':now})