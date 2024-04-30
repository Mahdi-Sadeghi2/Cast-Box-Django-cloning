from django.urls import path

from .views import ChannelListCreate, ChannelDetail, register_user, login, logout

urlpatterns = [
    path('channels/', ChannelListCreate.as_view(), name='channel-list-create'),
    path('channels/<int:pk>/', ChannelDetail.as_view(), name='channel-detail'),
    path('register/', register_user, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
