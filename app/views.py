from django.shortcuts import render

# Create your views here.

def bay(request):
    return render(request,'bay.html')