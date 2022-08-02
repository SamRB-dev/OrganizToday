from django.shortcuts import render #Rendering HTML
from django.http import HttpResponse #HTTP response
from . import models #DBs tables

# Create your views here.
'''Main Page'''
def main(request: "Request") -> "Response":
    entries = models.Schedule.objects.all()
    return render(request,"main/index.html",{'data':entries})

'''Form Handling: Receiving & Processing Post Request'''
def createList(request):
    if (request.method == "POST"):
        title = request.POST['title']
        duration = request.POST['duration']
        if ((title != '') and (duration != '')):
            db = models.Schedule(title=title,duration=duration)
            db.save()
    return render(request,"main/success.html")