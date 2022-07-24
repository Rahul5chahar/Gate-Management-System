from django.shortcuts import render
from django.views.generic import CreateView
from .models import Entry_Exit
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def Entry_Exit_view(request):
    a = Entry_Exit.objects.all()
    return render(request, "entryexit.html", {'qs': a} )

def output(request, id):
    if request.method == 'POST':
        if '_entry' in request.POST:
            entry_timestamp = Entry_Exit.objects.filter(pk=id).update(entry_timestamp=datetime.now())
            
            return redirect('entryexit')
        elif '_exit' in request.POST:
             exit_timestamp = Entry_Exit.objects.filter(pk=id).update(exit_timestamp=datetime.now())

             return redirect('entryexit')

    return redirect('entryexit')
