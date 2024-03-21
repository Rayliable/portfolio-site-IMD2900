from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name="register"),
    path('<int:pk>/profile/', views.ProfileView.as_view(), name="profile"),
    path('<int:pk>/edit_profile/', views.ProfileEditView.as_view(), name="edit_profile"),
    path('logout/', views.logout_view, name="logout"),
]
