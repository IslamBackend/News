from django.urls import path
from users import views


urlpatterns = [
    path('login/', views.Login.as_view()),
    path('register/', views.register),
    path('logout/', views.logout),
    path('profile/', views.profile),
]