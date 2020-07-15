from django.shortcuts import render, redirect

from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required


# def index(request):
#     item_list = Item.objects.all()
#     context = {
#         'item_list':item_list,
#     }
#     return render (request,'food/index.html',context)
# Class based Index Vieew
class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

# def detail(request,item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item':item,
#     }
#     return render (request,'food/detail.html',context)
class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'


# def create_item(request):
#     form = ItemForm(request.POST or None)
#
#     if  form.is_valid():
#         form.save()
#         return redirect('food:index')
#     return render(request,'food/item-form.html',{'form':form})

# class based view
# @login_required
class CreateItem(CreateView):
    model = Item;
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)






def update_item(request,item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if  form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form,'item':item })


# delete method
def delete_item(request,item_id):
    item = Item.objects.get(pk=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item':item })

