from django.urls import path

from . import views

urlpatterns = [
    path('table/', views.new_form, name='create_table'),
    path('table/<int:pk>/', views.table_page, name = 'table_page'),  
]