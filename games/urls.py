from django.urls import path

from games.views import GameTemplate

urlpatterns = [
    path("items", GameTemplate.as_view())
]
