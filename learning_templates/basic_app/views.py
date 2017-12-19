from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    context_dict = {'text':'Hello today is:', 'date':now.strftime('%m-%d-%Y')}
    return render(request,'basic_app/index.html',context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
