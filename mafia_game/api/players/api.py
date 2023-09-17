from json_api.commands import NotFoundError, Error
from json_api.decorators import get_api_request, post_api_request, delete_api_request
from players.models import Player


@post_api_request
def get_players_list(request, data):
    try:
        return Player.objects.filter(nickname__in=data['nicknames']).serialize()
    except (ValueError, KeyError):
        raise Error(response_code=404)
    
@get_api_request
def get_all_players_list(request):
    try:
        return Player.objects.all().serialize()
    except (ValueError, KeyError):
        raise Error(response_code=404)


@get_api_request
def get_player_by_nickname(request, player_nickname):
    try:
        return Player.objects.get(nickname=player_nickname).serialize()
    except Player.DoesNotExist:
        raise NotFoundError(text=f'Player {player_nickname} is not found')


@post_api_request
def create_player(request, data):
    try:
        if len(data['nickname']) == 0:
            raise Error(response_code=400, text="Lenght of nickname must be > 0")
        if len(data['nickname']) > 100:
            raise Error(response_code=400, text="Lenght of nickname must be < 100")

        try:
            Player.objects.get(nickname=data['nickname'])
            raise Error(response_code=409, text="Player with such nickname exists")
        except Player.DoesNotExist:
            new_player = Player(nickname=data['nickname'], email=data["email"], sex=data["sex"])
            new_player.save()
            return new_player.serialize()
    except (ValueError, KeyError):
        raise Error(response_code=404)


@post_api_request
def change_player_info(request, data, player_nickname):
    try:
        player = Player.objects.get(nickname=player_nickname)
        if 'nickname' in data:
            if (data['nickname'] != player.nickname):
                try:
                    Player.objects.get(nickname=data['nickname'])
                    raise Error(response_code=409, text="Player with such nickname exists")
                except Player.DoesNotExist:
                    player.nickname = data['nickname']
        if 'email' in data:
            player.email = data['email']
        if 'sex' in data:
            player.sex = data['sex']
        player.save()
        return player.serialize()
    except Player.DoesNotExist:
        raise NotFoundError(text=f'Player {player_nickname} is not found')


@get_api_request
def delete_player(request, player_nickname):
    try:
        player = Player.objects.get(nickname=player_nickname)
        player.delete()
        return "player was successfully deleted"
    except Player.DoesNotExist:
        raise NotFoundError(text=f'Player {player_nickname} is not found')

@get_api_request
def delete_all_players(request):
    try:
        players = Player.objects.all()
        for player in players:
            player.delete()
        return "all players was successfully deleted"
    except (ValueError, KeyError):
        raise Error(response_code=404)