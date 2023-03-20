from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('',views.PostListView.as_view(), name="home"),
    path('new/', views.PostCreateView.as_view(), name="post_new"),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name="post_delete"),
    path('edit/<int:pk>/', views.PostUpdateView.as_view(), name="post_edit"),
    path('greet/', views.greet, name='greet'),
    path('love/', views.love, name='love'),
    path('golden/', views.golden, name='golden'),
]