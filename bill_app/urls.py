from django.urls import path
from . import views


urlpatterns = [
    path('',views.login,name='login'),
    path('base',views.base,name='base'),
    path('dologin',views.dologin,name='dologin'),
    path('logout',views.logout,name='logout'),

    # This is ADMIN panel

    path('admin_home',views.admin_home,name='admin_home'),
    
    
    path('add_category',views.add_category,name='add_category'),
    path('view_category',views.view_category,name='view_category'),
    path('edit_category/<str:id>',views.edit_category,name='edit_category'),
    path('update_category',views.update_category,name='update_category'),
    path('delete_category/<str:id>',views.delete_category,name='delete_category'),
    
    path('add_brand',views.add_brand,name='add_brand'),
    path('view_brand',views.view_brand,name='view_brand'),
    path('edit_brand/<str:id>',views.edit_brand,name='edit_brand'),
    path('update_brand',views.update_brand,name='update_brand'),
    path('delete_brand/<str:id>',views.delete_brand,name='delete_brand'),
    
    path('add_supplier',views.add_supplier,name='add_supplier'),
    path('view_supplier',views.view_supplier,name='view_supplier'),
    path('edit_supplier/<str:id>',views.edit_supplier,name='edit_supplier'),
    path('update_supplier',views.update_supplier,name='update_supplier'),
    path('delete_supplier/<str:id>',views.delete_supplier,name='delete_supplier'),

    path('add_product',views.add_product,name='add_product'),
    path('view_product',views.view_product,name='view_product'),

]