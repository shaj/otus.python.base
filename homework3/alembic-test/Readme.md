[Welcome to Alembic’s documentation](https://alembic.sqlalchemy.org/en/latest/)

https://stackoverflow.com/questions/32032940/how-to-import-the-own-model-into-myproject-alembic-env-py

# Основные команды

Восстановление базы

```
alembic upgrade head
```

Автоматическая миграция

```
alembic revision --autogenerate -m "Тут комментарий к ревизии"
```
