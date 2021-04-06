Первый проект на django
=======================

*За основу взята база из homework3*

TODO
-----

1. Перенести модель в Djando
2. Подключиться к postgres. Проверить psycopg2.
3. Сделать миграции
4. Очистка базы и заполнение тестовыми данными
   - применимо для Балука
5. Перенести статику и разметку
6. 


Темы уроков
-----------

**Урок 26** - Знакомство с Django. админка; модели; миграции.

**Урок 27** - Django ORM, django-debug-toolbar. 

  - связи OneToOne, OneToMany, ManyToMany;
  - select_related/prefetch_related;
  - django-debug-toolbar.

**Урок 28** - Django и отложенные задачи.

  - celery и rabbitmq;
  - отправка электронной почты в неблокирующем режиме;
  - проверка статуса отложенной задачи.
    
**Урок 29** - больше Django.

  - Class Based views;
  - generics;
  - Django Forms.
