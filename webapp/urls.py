
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import path, include 
from django.conf.urls.static import static
# from webapp.views import home,itemdetails
from webapp.views import HomeView,ItemDetailView,add_to_cart,about_us,contact,cart_item,profile


app_name='webapp'
urlpatterns = [
    # path('',home,name='homapage')
    path('home/', HomeView.as_view(),name='homepage'),
    path('product/<slug>/',ItemDetailView.as_view(),name='product'),
    path('add_to_cart/<slug>/',add_to_cart,name='add_to_cart'),
    path('about/',about_us,name='about'),
    path('contact/',contact,name='contact'),
    path('cart/',cart_item,name='cart_item'),
    path('accounts/profile/',profile,name='profile'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
