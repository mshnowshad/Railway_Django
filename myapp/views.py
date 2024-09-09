from django.shortcuts import render,redirect
from .models import Names_app
from .forms import Names_appForm
from django.contrib import messages
# Create your views here.


def index(request):
    lists = Names_app.objects.all()


    #add task in list
    if request.method == "POST":
        form = Names_appForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully!")
            return redirect('index')
    else:
        form = Names_appForm()


    context = {
        "lists":lists,
        "form":form,
    }
    return render(request, 'index.html',context)