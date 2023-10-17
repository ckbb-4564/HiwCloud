from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'app_general/home.html')