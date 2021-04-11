from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

#def signup(request):
    #return render(request, 'signup.html')

#def signin(request):
    #return render(request, 'signin.html')

#def forgot(request):
    #return render(request, 'signin.html')