from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required

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

class IndexClassView(ListView):
  model = Item
  template_name="food/index.html"
  context_object_name = "items"


def item(request):
  return HttpResponse('<h1>this is an item view</h1>')


def detail22(request, item_id):
  item = Item.objects.get(pk=item_id)
  ctx = {
    "item": item
  }
  return render(request, "food/details.html", context=ctx)

class DetailClassView(DetailView):
  model = Item
  template_name="food/details.html"
  context_object_name= "item"

def create_item(request):
  form = ItemForm(request.POST or None)
  
  if form.is_valid():
    form.save()
    return redirect("food:index")
  
  return render(request, "food/item-form.html",context= {'form': form})

#@login_required(login_url="login")
class CreateItemView(CreateView):
    model = Item
    fields = ["item_name", "item_desc", "item_price", "item_image"]
    template_name = "food/item-form.html"
    
    def form_valid(self, form):
      form.instance.user_name = self.request.user
      
      return super().form_valid(form)
    
    #def get_success_url(self) -> str:
     #   return reverse('food:detail',kwargs={"pk":self.request})
    



def update_item(request, item_id):
  item = Item.objects.get(id=item_id)
  form = ItemForm(request.POST or None,instance=item)
  if form.is_valid():
    form.save()
    return redirect("food:index")
  return render(request, "food/item-form.html", context={'form': form})

class UpdateItemView(UpdateView):
    model = Item
    context_object_name= "form"
    template_name = "food/item-form.html"
    
    def get_success_url(self) -> str:
      pass


  
def delete_item(request, item_id):
  #Item.objects.delete(id=item_id)
  item = Item.objects.get(id=item_id)
  if request.method == "POST":
    item.delete()
    return redirect("food:index")
  
  return render(request, "food/item-delete.html", context={"item": item})
  #items = Item.objects.all()
  #return render(request,"food/index.html", {"items": items})
  
class ItemDeleteView(DeleteView):
    model = Item
    template_name = "food/item-delete.html"
    context_object_name = "item"
    
    def get_success_url(self) -> str:
        return reverse_lazy('food:index')
  