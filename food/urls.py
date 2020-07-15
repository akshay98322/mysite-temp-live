from .import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    # home
    path('', views.IndexClassView.as_view(),name='index'),
    # food details
    path('<int:pk>/', views.FoodDetail.as_view(),name='detail'),

    # add item
    path('add',views.CreateItem.as_view(),name='create_item'),
    #edit item
    path('update/<int:item_id>/', views.update_item,name='update_item'),
    #delete item
    path('delete/<int:item_id>/', views.delete_item,name='delete_item'),


]