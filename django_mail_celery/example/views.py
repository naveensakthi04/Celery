from django.http import HttpResponse
from django.shortcuts import render
from .tasks import sleepy, send_email_task


# Create your views here.

def index(request):
    send_email_task.delay()
    return HttpResponse('<h1>EMAIL SENT!</h1>')
