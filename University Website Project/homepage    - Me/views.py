from django.shortcuts import render

# Create your views here.


def index(request):
    # Returns the html file to show.
    return render(request, 'homepage/index.html')
