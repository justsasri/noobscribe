from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from noobscribe.socials.models import YoutubeChannel, YoutubeVideo


class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'account/index.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'



class YoutubeChannelListView(ListView):
    model = YoutubeChannel
    template_name = 'socialaccount/youtube_channel_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class YoutubeVideoListView(ListView):
    model = YoutubeChannel
    template_name = 'socialaccount/youtube_video_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)