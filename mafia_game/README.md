### Запуск
```bash
git clone clone https://github.com/daniilpetraytis/SOA.git
cd SOA/mafia_game
docker compose up -d
```
### Работа
Протестировать работу можно следующими запросами через утилиту `curl`
- Создание игрока (`/api/players/create_player/`)
Пример запроса:
```bash
$ curl  http://127.0.0.1:8000/api/players/create_player/ --header "Content-Type: application/json" --data '{"nickname":"player1", "sex":"male", "email":"player1@mail.ru"}'
```
Пример ответа:
```json
{"data": {"sex": "male", "id": 5, "nickname": "player1", "email": "player1@mail.ru"}, "version": "0.1.0", "mode": "local"}
```

- Получение информации по конкретному игроку (`/api/players/player/<str:player_nickname>/`)
Пример запроса:
```bash
$ curl  http://127.0.0.1:8000/api/players/player/player1/
```
Пример ответа:
```json
{"data": {"sex": "male", "id": 5, "nickname": "player1", "email": "player1@mail.ru"}, "version": "0.1.0", "mode": "local"}
```

- Получение информации по нескольким игрокам (`/api/players/list/`)
Пример запроса:
```bash
$ curl  http://127.0.0.1:8000/api/players/list/ --header "Content-Type: application/json" --data '{"nicknames":["player1", "player2"]}'
```
Пример ответа:
```json
{"data": [{"sex": "male", "id": 5, "nickname": "player1", "email": "player1@mail.ru"}, {"sex": "male", "id": 6, "nickname": "player2", "email": "player1@mail.ru"}], "version": "0.1.0", "mode": "local"}
```

- Получение информации по всем игрокам (`/api/players/list/all`)
Пример запроса:
```bash
$ curl http://127.0.0.1:8000/api/players/list/all/
```
Пример ответа:
```json
{"data": [{"nickname": "daniil", "id": 1, "email": "p@mail.ru", "sex": "m"}, {"nickname": "daniil2", "id": 2, "email": "p@mail.ru", "sex": "m"}, {"nickname": "daniil_petr", "id": 3, "email": "p@mail.ru", "sex": "m"}, {"nickname": "player2_changed", "id": 4, "email": "player@mail.ru", "sex": "w"}], "version": "0.1.0", "mode": "local"}
```

- Изменение информации игрока (`/api/players/change_player_info/<str:player_nickname>/`)
Пример запроса:
```bash
$ curl  http://127.0.0.1:8000/api/players/change_player_info/player1/ --header "Content-Type: application/json" --data '{"nickname":"player1", "email":"changed_email"}'
```
Пример ответа:
```json
{"data": {"sex": "male", "email": "changed_email", "id": 5, "nickname": "player1"}, "version": "0.1.0", "mode": "local"}
```

- Удаление игрока (`/api/players/delete_player/<str:player_nickname>/`)
Пример запроса:
```bash
$ curl http://127.0.0.1:8000/api/players/delete_player/player1/
```
Пример ответа:
```json
{"data": "player was successfully deleted", "version": "0.1.0", "mode": "local"}
```

- Удаление всех игроков (`/api/players/delete_all_players/`)
Пример запроса:
```bash
$ curl http://127.0.0.1:8000/api/players/delete_all_players/
```
Пример ответа:
```json
{"data": "all players was successfully deleted", "version": "0.1.0", "mode": "local"}
```