from django.urls import path

from .views import (
    CommentListCreate, CommentDetail,
    LikeListCreate, LikeDetail,
    PlaylistListCreate, PlaylistDetail,
    PlaylistItemListCreate, PlaylistItemDetail,
    SubscriptionViewSet, WatchHistoryViewSet
)


urlpatterns = [
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    path('likes/', LikeListCreate.as_view(), name='like-list-create'),
    path('likes/<int:pk>/', LikeDetail.as_view(), name='like-detail'),
    path('playlists/', PlaylistListCreate.as_view(), name='playlist-list-create'),
    path('playlists/<int:pk>/', PlaylistDetail.as_view(), name='playlist-detail'),
    path('playlist-items/', PlaylistItemListCreate.as_view(),
         name='playlist-item-list-create'),
    path('playlist-items/<int:pk>/', PlaylistItemDetail.as_view(),
         name='playlist-item-detail'),
    path('subscriptions/', SubscriptionViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='subscriptions'),
    path('subscriptions/<int:pk>/', SubscriptionViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='subscription-detail'),
    path('watch_history/', WatchHistoryViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='watch-history')
]
