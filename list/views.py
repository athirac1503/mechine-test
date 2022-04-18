from django.shortcuts import render

# Create your views here.



def to_do(request):
    return render(request, 'listapp/to_do.html')
