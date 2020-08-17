from django.urls import path
from .views import loginfunc, logoutfunc

urlpatterns = [
    path('login/', loginfunc, name="login"),
    # path('list/', listfunc, name="list"),
    path('logout/', logoutfunc, name="logout"),
]