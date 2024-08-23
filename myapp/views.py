from django.shortcuts import render
from .models import Names_app
# Create your views here.


def index(request):
    prods = Names_app.objects.all()
    return render(request, 'index.html',{'prods':prods})