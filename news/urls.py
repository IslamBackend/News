from django.urls import path
from news import views

urlpatterns = [
    path('test/', views.hello_world),

    path('', views.news_list),  # GET -> list, POST -> create
    path('<int:news_id>/', views.news_detail),  # GET -> retrieve or detail, PUT -> update, DELETE -> delete

    path('comments/', views.comments_list),
]
