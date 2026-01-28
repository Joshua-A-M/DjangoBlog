from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    #   chapter two implementation
    #   int path converter is used for the year, month, and day parameters
    #   the slug path converter is used for the post parameter
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    # path('<int:id>/', views.post_detail, name='post_detail'),
    # path('favorite/add/<int:id>/', views.add_favorite, name='add_favorite'),
    # path('favorites/', views.favorites, name='favorites'),
]