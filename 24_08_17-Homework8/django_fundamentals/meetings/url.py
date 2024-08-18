from django.urls import path
from django.contrib.auth import views as auth_views

from meetings import views

urlpatterns = [
    path("<int:id>", views.detail, name="detail"),
    path("rooms", views.rooms_list, name="rooms"),
    path("new", views.new, name="new"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("delete/<int:id>", views.delete, name="delete"),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
