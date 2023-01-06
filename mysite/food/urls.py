from django.urls import path
from . import views

app_name = "food"
urlpatterns = [
    #/food
    #path("", views.index, name = "index"),
    path("", views.IndexClassView.as_view(), name= "index"),
   # path("item", views.item, name="item"),
    #"food/id"
    path("<int:pk>/", views.DetailClassView.as_view(), name="detail"),
    #path("<int:item_id>/", views.detail, name="detail"),
    #add
    path("add", views.CreateItemView.as_view(), name="create_item"),
    #edit
    path("update/<int:item_id>", views.update_item, name="update_item"),
    #delete
   # path("delete/<int:item_id>", views.delete_item, name="delete_item")
    path("delete/<int:pk>", views.ItemDeleteView.as_view(), name="delete_item")
]
