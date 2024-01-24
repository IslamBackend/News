from django.urls import path
from news import views

urlpatterns = [
    path('api/v1/test/', views.hello_world),

    path('api/v1/news/', views.news_list),  # GET -> list, POST -> create
    path('api/v1/news/<int:news_id>/', views.news_detail),  # GET -> retrieve or detail, PUT -> update, DELETE -> delete


    path('api/v1/comments/', views.comments_list),
]