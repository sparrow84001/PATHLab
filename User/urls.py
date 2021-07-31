from django.urls import path
from . import views

urlpatterns = [
		path('',views.login),
        path('logcode',views.logcode),
		path('home',views.Is_logged_in),
        path('registration',views.registration),
        path('register',views.register_view,name='register_user'),
        path('register_user',views.register_user),
]