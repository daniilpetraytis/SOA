from django.urls import path, include

urlpatterns = [
    path('players/', include('api.players.urls')),
]