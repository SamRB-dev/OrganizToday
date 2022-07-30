from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
'''Main Page'''
def main(request: "Request") -> "Response":
    return render(request,"main/index.html")

'''Form Handling: Receiving & Processing Post Request'''
def createList(request):
    if (request.method == "POST"):
        title = request.POST['title']
        duration = request.POST['duration']
        if ((title != '') and (duration != '')):
            db = models.List(title=title,duration=duration)
            db.save()
    return render(request,"main/success.html")
