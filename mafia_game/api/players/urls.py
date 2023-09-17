from django.urls import path
from . import api

urlpatterns = (
    path(r'list/', api.get_players_list, name='api.players.player.list'),
    path(r'player/<str:player_nickname>/', api.get_player_by_nickname, name='api.players.get_player_by_nickname'),
    path(r'create_player/', api.create_player, name='api.players.create_player'),
    path(r'change_player_info/<str:player_nickname>/', api.change_player_info, name='api.players.change_player_info'),
    path(r'delete_player/<str:player_nickname>/', api.delete_player, name='api.players.delete_player'),
)
