from django.urls import path
from .views import register_user,MyLoginView,user_list

urlpatterns = [
    path('register/',register_user, name='register_user'),
    path('login/',MyLoginView.as_view()),
    path('user_list/',user_list, name='user_list')
]