from json_api.commands import Redirect, NotFoundError, Error
from json_api.decorators import get_api_request, post_api_request
from players.models import Player


@get_api_request
def get_players_list(request):
    print("Список текущих игроков:\n")
    return Player.objects.all().serialize()

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
