from django.shortcuts import render,redirect
from .models import Names_app
from .forms import Names_appForm
# Create your views here.


def index(request):
    prods = Names_app.objects.all()


    #add task in list
    if request.method == "POST":
        form = Names_appForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Names_appForm()


    context = {
        "prods":prods,
        "form":form,
    }
    return render(request, 'index.html',context)