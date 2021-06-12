from django.shortcuts import render
from ..hello import *
from .forms import *

def function(request):
    form = MyForm()
    if request.method=='POST':
        form = MyForm(request.POST)
        if form.is_valid():
            x = int(form.data['x'])
            y = int(form.data['y'])
            return render(request, "function.html", {'form' : form , 'soma' : add(x , y)})
    return render(request, "function.html", {'form' : form ,'soma' : 0})



