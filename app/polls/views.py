from django.shortcuts import render, redirect
from .models import Item

def home(request):
    print('metodo home')
    if request.method == 'POST':        
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/polls/')
    print('request.method ',request.method)
    items = Item.objects.all()
    print('items ',items)
    return render(request, 'polls/home.html', {'items': items})
