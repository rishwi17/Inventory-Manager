from django.shortcuts import get_object_or_404, redirect, render
from .models import Furniture, Fashion, Gadgets
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'inv/index.html')

def display_furniture(request):
    items = Furniture.objects.all()
    context = {
        'items': items,
        'header': 'Furniture',
    }
    return render(request, 'inv/index.html', context)


def display_fashion(request):
    items = Fashion.objects.all()
    context = {
        'items': items,
        'header': 'Fashion',
    }
    return render(request, 'inv/index.html', context)


def display_gadgets(request):
    items = Gadgets.objects.all()
    context = {
        'items': items,
        'header': 'Gadgets',
    }
    return render(request, 'inv/index.html', context)


def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'inv/add_new.html', {'form' : form})

def add_furniture(request):
    return add_item(request,FurnitureForm)

def add_fashion(request):
    return add_item(request,FashionForm)

def add_gadgets(request):
    return add_item(request,GadgetsForm)
    

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'inv/edit_item.html', {'form': form})

def edit_furniture(request, pk):
    return edit_item(request, pk, Furniture, FurnitureForm)


def edit_fashion(request, pk):
    return edit_item(request, pk, Fashion, FashionForm)


def edit_gadgets(request, pk):
    return edit_item(request, pk, Gadgets, GadgetsForm)



def delete_furniture(request, pk):

    template = 'inv/index.html'
    Furniture.objects.filter(id=pk).delete()

    items = Furniture.objects.all()

    context = {
        'items': items,
        'header':'Furniture'
    }

    return render(request, template, context)


def delete_fashion(request, pk):

    template = 'inv/index.html'
    Fashion.objects.filter(id=pk).delete()

    items = Fashion.objects.all()

    context = {
        'items': items,
        'header':'Fashion'
    }

    return render(request, template, context)


def delete_gadgets(request, pk):

    template = 'inv/index.html'
    Gadgets.objects.filter(id=pk).delete()

    items = Gadgets.objects.all()

    context = {
        'items': items,
        'header':'Gadgets'
    }

    return render(request, template, context)



