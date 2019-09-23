from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('signup/',views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('menu/',views.get_menu,name='menu'),
    path('menulist/', views.get_menu_list, name='menulist'),
    path('book_event/', views.book_event, name='book_event'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('vendor/', views.vendor, name='vendor_login'),
    path('package/', views.package, name='package'),
    path('customer/', views.customer, name='customer'),
]
#<str:user_name>
