from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Item
from django.template import loader
from .forms import ItemForm

# Create your views here.
# function name will be the view

def index(request):
  items = Item.objects.all()
  temp = loader.get_template("food/index.html")
  context = {
    "items": items
  }

  #return HttpResponse(temp.render(context, request))
  return render(request, "food/index.html", context=context)

def item(request):
  return HttpResponse('<h1>this is an item view</h1>')

def detail(request, item_id):
  item = Item.objects.get(pk=item_id)
  ctx = {
    "item": item
  }
  return render(request, "food/details.html", context=ctx)

def create_item(request):
  form = ItemForm(request.POST or None)
  
  if form.is_valid():
    form.save()
    return redirect("food:index")
  
  return render(request, "food/item-form.html",context= {'form': form})

def update_item(request, item_id):
  item = Item.objects.get(id=item_id)
  form = ItemForm(request.POST or None,instance=item)
  if form.is_valid():
    form.save()
    return redirect("food:index")
  return render(request, "food/item-form.html", context={'form': form})
  
def delete_item(request, item_id):
  #Item.objects.delete(id=item_id)
  item = Item.objects.get(id=item_id)
  if request.method == "POST":
    item.delete()
    return redirect("food:index")
  
  return render(request, "food/item-delete.html", context={"item": item})
  #items = Item.objects.all()
  #return render(request,"food/index.html", {"items": items})