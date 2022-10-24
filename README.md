# API сервис транспортной компании
Состоит из двух связанных бэкенд сервисов:
* API сервер на базе DRF
* База данных Postresql

---
## Цель
Сервер транспортной компании, подключаемый к оборудованию 
внутри локальной сети компании.

---
## Функционал
* Внесение и изменение данных клиентов компании
* Внесение и изменение данных водителей компании
* Внесение и изменение данных заказов компании
* Внесение и изменение вспомогательных данных
* Внесение и изменение данных об автопарке компании
* Внесение и изменение данных поездок компании

---
## Стек технологий
* Языки программирования
  * Python
* Базовые фреймворки
  * Django
  * DRF
* База данных
  * Postgresql
* Сервер
  * WSGI
* Версионирование
  * git
* Среда запуска
  * Docker

---
## Общее описание
Информационный сервис внутреннего использования для 
транспортной компании, позволяющий манипулировать данными о работниках, 
заказах, водителях и транспортных средствах. 
Взаимодействия с данными происходят путем общения клиент-сервер 
по протоколу HTTP в формате JSON. В общем смысле для ведения 
статистики или внесения данных такой подход позволяет 
подключать к сети компании различные устройства 
(компьютеры, телефоны, планшеты, etc), что позволяет 
получать доступ из различных точек (склада, офиса, автопарка, etc),
тем самым оптимизировать условия работы работников компании. 
В качестве среды выполнения используется Docker, 
сконфигурированный для API и БД. Чувствительные данные и
данные конфигурации проекта хранятся в переменных окружения.

---
## Что я изучу
В процессе реализации сервиса я хочу углубить знания построения API 
на базе фреймворка DRF, в частности с использованием Django Rest 
Routers и Viewsets. Освоить переназначение встроенных обработчиков 
ошибок, способы внедрения кросс-табличных и внутре-табличных 
ограничений на базе ORM Django с особенностями реализации 
СУБД Postgresql. Изучу подключение и использование модуля 
для динамической генерации документации Openapi для сервера.

---
## Конфигурация
Среда разработки опирается на `.env` файл который используется 
файлом `docker-compose.yml` при запуске.

Конфигугация, которая должна быть указана для разработчика в 
файле `.env`.

```
SECRET_KEY=*** # django secret key
SERVER_PORT=8000
STAGE=local # для запуска в docker автоматически указывается docker
DB_NAME=transport
DB_USER=postgres
DB_PASSWORD=postgres
DB_PORT=8080
```

---
## Миграции
Используйте `Makefile` для запуска миграции, если модель БД изменится.


---
## Управление зависимостями проекта
У api сервиса есть `pip-tools` для управления зависимостями. 
Зависимости проекта перечислены в файле `requirements.in`. 
Полное дерево зависимостей компилируется в файл `requirements.txt`, 
который используется для установки через `pip`.