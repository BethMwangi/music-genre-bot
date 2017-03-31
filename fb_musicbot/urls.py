from django.conf.urls import include, url
from .views import MusicBotView


urlpatterns = [

   url(r'^e91455a54a32dcdb5d33dd1e9d0cc563a87dc2e7408b3b6706/?$', MusicBotView.as_view())

]