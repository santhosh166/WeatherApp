from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import urllib.request
import json
# Create your views here.
def details(request):
    if request.method=="POST":
        city=request.POST['city']
        if len(city)<1:
            return render(request,'index.html')
        source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=c71849926b454a44866ea9de80c0907b').read()
        source_data=json.loads(source)
        data={
            "City":city.capitalize(),
            "Icon":source_data["weather"][0]["icon"],
            "Temp":str(source_data["main"]["temp"])+" ℃",
            "Description":source_data["weather"][0]["description"]
        }
    else:data={}
    return render(request,'index.html',data)