from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from webapp.models import Item,OrderItem,Order
from django.shortcuts import redirect

# def home(request):
#     context={
#         'item':Item.objects.all
#     }
#     return render(request,'webapp/item_list.html',context)
# def itemdetails(request,id):
#     item=Item.Objects.all(id=id)
#     context={
#         'item':item
#     }
#     return render(request,'webapp/item_details.html',context)


class HomeView(ListView):
    model=Item
    template_name='item_list.html'


class ItemDetailView(DetailView):
    model=Item
    template_name='webapp/product.html'    

def add_to_cart(request,slug):
    item=get_object_or_404(Item,slug=slug)    
    order_item=OrderItem.objects.create(item=item)
    order_qs=Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]
        if order.item.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save
    else:
        ordered_date=timezone.now()
        order=Order.objects.create (user=request.user,ordered_date=ordered_date)  
        order.item.add(order_item)  
        return redirect("webapp:product",kwargs={'slug':slug})   
def about_us(request):
    return render(request,'about_us1.html')

def contact(request):
    return render(request,'contact_us.html') 
def cart_item(request):
    return render(request,'cart/cart_list.html')       
def profile(request):
    return render(request,'accounts/profile.html') 

