# Web

## Before start
1. Create SSL cert
```bash
$ openssl req -x509 -out localhost.crt -keyout localhost.key \
  -newkey rsa:2048 -nodes -sha256 \
  -subj '/CN=localhost' -extensions EXT -config <( \
   printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")
```

2. Configure nginx
```bash
$ ./configure_nginx.sh
```

3. Place some image as 'static/img/image.jpg'

## Usage
##### First start
1) Run nginx: ./run_nginx.sh
2) Run server: ./run_server.sh

##### Reload
1) Stop server (Ctrl+C)
2) Reload nginx if needed: nginx -s reload 
3) Run server: ./run_server.sh

##### Stop server
1) Stop server (Ctrl+C)
2) Stop nginx: nginx -s stop

## Лабораторная работа 1

**Цель работы** - создание RESTFul API приложения по поиску рецептов различных блюд по их ингредиентам

##### Краткий перечень функциональных требований
* Регистрация
* Авторизация
* Просмотр списка рецептов
* Поиск рецептов по ингредиентам
* Сортировка рецептов по алфавиту, популярности, обсуждаемости
* Просмотр рецепта
* Добавление/удаление рецепта в избранное
* Просмотр комментариев к рецепту
* Добавление/измененеие/удаление комментариев к рецепту
* Просмотр вопросов пользователей
* Создание/удаление/изменение вопроса
* Просмотр ответов к вопросам
* Создание/удаление/изменение ответов

## Use-case диаграмма
![Изображение](https://github.com/shestakovar/Web/blob/lab_01/docs/img/use_case.png)