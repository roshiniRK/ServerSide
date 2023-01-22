from django.shortcuts import render
from datetime import datetime
# Create your views here.

def home(request):
    context = {}
    context['TimeStamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render(request, 'myfirstapp/home.html',context)    