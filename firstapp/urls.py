
from django.urls import path
from .views import MyclassView

urlpatterns = [
    path('index',MyclassView.as_view(),name='index')
]
