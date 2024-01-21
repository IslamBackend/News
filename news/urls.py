from django.urls import path
from news import views

urlpatterns = [
    path('api/v1/test/', views.hello_world),
    path('api/v1/news/', views.news_list),
    path('api/v1/news/<int:news_id>/', views.news_detail),

    path('api/v1/comments/', views.comments_list),
]