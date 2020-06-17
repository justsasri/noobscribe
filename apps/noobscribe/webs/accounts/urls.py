from django.urls import path, include
from allauth import urls as allauth_urls

from .views import (
    AccountView, ProfileView,
    YoutubeChannelListView,
    YoutubeVideoListView
)

urlpatterns = [
    path('', AccountView.as_view(), name='account_home'),
    path('profile/', ProfileView.as_view(), name='account_profile'),
    path('youtube/channels/', YoutubeChannelListView.as_view(), name='youtube_channel_list'),
    path('youtube/videos/', YoutubeVideoListView.as_view(), name='youtube_video_list')
]

urlpatterns += allauth_urls.urlpatterns