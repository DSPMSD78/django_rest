from django.shortcuts import render
from .models import Item


# Create your views here.
def base(request):
    return render(request, 'base.html')

def addItem(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        item = Item.objects.create(name=name)
        item.save()
    return render(request, 'add_item.html')