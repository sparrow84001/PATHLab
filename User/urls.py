from django.urls import path
from . import views

urlpatterns = [
		path('',views.login),
        path('logcode',views.logcode),
		path('home',views.Is_logged_in),
        path('registration',views.registration),
]