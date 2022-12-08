
from django.urls import path
from . import views
urlpatterns = [
path('index', views.index, name="index"),
path('dequeue', views.dequeue, name="dequeue"),
path('enqueue',views.enqueue,name='enqueue')
]
