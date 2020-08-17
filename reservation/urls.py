from django.urls import path
from .views import listfunc, prevlistfunc, nextlistfunc, reservefunc, completefunc

urlpatterns = [
    path('list/', listfunc, name="list"),
    path('prevlist/<int:counter>/', prevlistfunc, name="prevlist"),
    path('nextlist/<int:counter>/', nextlistfunc, name="nextlist"),
    path('reserve/<int:teacherid>/<str:newtoday>/<str:worktime>/', reservefunc, name="reserve"),
    path('complete/<int:teacherid>/<str:newtoday>/<str:worktime>/', completefunc, name="complete"),
]