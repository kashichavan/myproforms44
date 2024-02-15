from django.urls import path
from . import views

urlpatterns = [
    path('studentview/',views.studentview,name='studentview'),
    path('studentview2/',views.studentview2,name='studentview2')
]
