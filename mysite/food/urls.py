from django.urls import path
from . import views

app_name = "food"
urlpatterns = [
    #/food
    path("", views.index, name = "index"),
    path("item", views.item, name="item"),
    #"food/id"
    path("<int:item_id>/", views.detail, name="detail"),
    #add
    path("add", views.create_item, name="create_item"),
    #edit
    path("update/<int:item_id>", views.update_item, name="update_item"),
    path("delete/<int:item_id>", views.delete_item, name="delete_item")
]
