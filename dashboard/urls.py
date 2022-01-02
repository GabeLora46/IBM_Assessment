from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name= 'dashboard-index'),
    path('staff/', views.staff_index, name= 'staff-index'),
    path('portal/', views.admin_index, name='admin-index'),
    path('staff/orders/<int:key>/', views.staff_delete, name= 'staff-sent'),
    path('staff/view/<int:pk>/', views.staff_view, name= 'staff-view'),
    path('portal/delete/<int:key>/', views.admin_fire, name='admin-fire'),
    #path('portal/view/<int:key>/', views.admin_staff_profile, name='admin-view'),


]