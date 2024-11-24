from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import reviews_view


urlpatterns = [
    path('', views.contact_list, name='base'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('add/', views.add_contact, name='add_contact'),
    path('reviews/', views.reviews_view, name='reviews'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='phonebook/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reviews/delete/<int:pk>/', views.delete_review, name='delete_review'),
]

