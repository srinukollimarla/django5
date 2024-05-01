from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.static import serve
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
    path("addartist",views.addartist,name="addartist"),
    path('add_admin/', views.add_admin, name='add_admin'),

    path('admin_list/', views.admin_list, name='admin_list'),
    path('admin_artist_signup/', views.admin_artist_signup, name='admin_artist_signup'),
    path('admin_customer_signup/', views.admin_customer_signup, name='admin_customer_signup'),
    #path('login/', views.login_view, name='login'),
    path("checkartistlogin",views.checkartistlogin,name="checkartistlogin"),
    path('artwork/', views.artwork_list, name='artwork_list'),
    path('add_artwork/', views.add_artwork, name='add_artwork'),

    path('auctions_list', views.auction_list, name='auction_list'),
    path('cart/', views.cart_view, name='cart'),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('payment-form/', views.payment_form, name='payment_form'),
    path('charge/', views.charge, name='charge'),



]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)