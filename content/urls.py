from django.urls import path
from .views import (EpisodeListCreate,
                    EpisodeDetail,
                    CommentListCreateAPIView,
                    CommentDetailAPIView,
                    LinkDetailAPIView,
                    LinkListCreateAPIView)


urlpatterns = [
    path('comments/', CommentListCreateAPIView.as_view(),
         name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
    path('links/', LinkListCreateAPIView.as_view(), name='link-list-create'),
    path('links/<int:pk>/', LinkDetailAPIView.as_view(), name='link-detail'),
    path('episodes/', EpisodeListCreate.as_view(), name='episode-list-create'),
    path('episodes/<int:pk>/', EpisodeDetail.as_view(), name='episode-detail'),
]
