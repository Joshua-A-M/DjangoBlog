from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    # path('favrorite/add/<int:id>/', views.add_favorite, name='add_favorite'),
    # path('favorites/', views.favorites, name='favorites'),
]