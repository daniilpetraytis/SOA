# Сериализация и десериализация данных

Сейчас реализована сериализация/десериализация для 5 типов - apache, json, message_pack, xml, yaml. Можно получать результат как по отдельному типу, так и по всем сразу.

Начало работы
```bash
git clone git@github.com:daniilpetraytis/SOA.git
cd hw_1
docker-compose up --build
```

В другом окне терминала
```bash
nc -u 0.0.0.0 2000
```

Чтобы запустить все типы
```bash
get_result all 
```
Чтобы запустить каждый тип по отдельности (вместо format_name ставим одно из списка: apache, json, message_pack, xml, yaml
```bash
get_result format_name 
```
