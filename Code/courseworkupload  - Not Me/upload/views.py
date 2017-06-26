from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from .forms import docform
from .models import Document


def upload(request):
    if request.method == 'POST':
        form = docform(request.POST)
        if form.is_valid():
            newdoc = Document (newfile=request.FILES['newfile'])
            newdoc.save()

        return HttpResponseRedirect(reverse('upload'))
    else:
        form = docform()

    return render( request,'upload.html',)

