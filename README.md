Для проверки созданы фикстуры user_data.json с пользователями (в т.ч. и админ) и habits.json с привычками.
Для проверки необходимо присвоить пользователям Telegram-ID либо Telegram-username, а также создать telegram_bot и совзаимодейтвовать Telegram-username с ботом.

###### Для запуска файла в Docker:

Ввести команду в терминал: docker-compose up -d --build

# Курсовая работа 8. Docker.

## Контекст

Для быстрого масштабирования проекта применяется контейнеризация. Для этого вам предстоит «завернуть» ваш проект в Docker и настроить на самостоятельный запуск.

Для выполнения задания используйте курсовой проект, над которым вы работали в курсе DRF.

## Критерии приемки курсовой работы

* Для разных сервисов создали отдельные контейнеры (django, postgresql, redis, celery, при необходимости список можно самостоятельно расширять).
* Всё оформили в файле docker-compose, при необходимости создали вспомогательные Dockerfiles.
* Проект готов быть размещенным на удаленном сервере:
  * его можно запустить по инструкции, приложенной в Readme-файл;
  * для запуска не требуется дополнительных настроек.
* Решение выложили на GitHub.

## Задание 1

Cоздайте отдельные контейнеры для сервисов в проекте.

Как минимум для следующих сервисов:

* Django,
* PostrgeSQL,
* Redis,
* Celery.

Как максимум — для всех сервисов проекта.

_Весь проект должен запускаться одной командой и при этом иметь возможность быть перенесенным на отдельный удаленный сервер для запуска на нём._
