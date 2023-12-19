from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('user/', homepage_2, name='homepage2'),
    path('login/', loginpage, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('delete/<str:user>/<int:id>/', delete_post, name='delete'),
    path('update/<str:user>/<int:id>/', update_post, name='update'),
]