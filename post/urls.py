from django.urls import path
from . import views


urlpatterns = {
    path('hello/', views.hello, name='hello'),
    path('greet/', views.greet, name='greet'),
    path('love/', views.love, name='love'),
    path('golden/', views.golden, name='golden'),
}