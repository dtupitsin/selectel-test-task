# Тестовое задание для Selectel 

## Задача

API должен принимать от пользователя файлы произвольного размера и сохранять их в контейнер
в облачном хранилище. Нужна возможность посмотреть список загруженных объектов и удалить ненужные.
Пользователей нужно авторизовывать и предоставлять доступ только к их данным.

## Техническое задание

1. API должен реализовывать три метода: GET для просмотра списка файлов, 
PUT для отправки файла, DELETE для удаления файла.
2. Данные клиента должны сохраняться в индивидуальный контейнер в облачном хранилище.
3. Аутентификация клиента осуществляется заголовком X-Auth-Token с UUID внутри. 
Авторизация сводится к проверке корректности UUID с последующим маппингом 1:1 в контейнер.
Клиент может генерировать произвольный UUID – создавать заранее список доступных не нужно.

## Описание 

1. Просмотр доступных файлов

    `GET /api/files`

    Возвращает список загруженых файлов
    ```bash
    $ > curl -H "X-Auth-Token: 18ce71ad-1391-46c7-91de-56948fda0d8a" "http://localhost:8080/api/files"
    ["bash", "bash_profile", "file1", "file3", "file4"]
    ```
 
2. Загрузить новый файл

    `PUT /api/files/{filename}`
    
    Возвращает статус `204` в случае успеха
    
    Пример:
    ```bash
    $ > curl -H "X-Auth-Token: 18ce71ad-1391-46c7-91de-56948fda0d8a" \ 
             "http://localhost:8080/api/files/new_file.txt" \
             --upload-file some_file.txt
    ```

3. Удалить файл

    `DELETE /api/files/{filename}`

    Возвращает статус `204` в случае успеха
    
    Пример:
    ```bash
    $ > curl -H "X-Auth-Token: 18ce71ad-1391-46c7-91de-56948fda0d8a" \ 
             -X DELETE \
             "http://localhost:8080/api/files/new_file.txt"
    ```


## Запуск
Для корректной работы необходим аккаунт в AWS с доступом к S3.
Необходимо поправить поправить конфиг `.env` или передать следующие переменные через 
окружение среды

```dotenv
BUCKET=<S3-bucket-name>
AWS_ACCESS_KEY_ID=<AWS_KEY_ID>
AWS_SECRET_ACCESS_KEY=<AWS_SECRET_KEY>
```

Установить/собрать и запустить сервис можно любым из перечисленных ниже способов

### virtualenv
Для установки локально в отдельном виртуальном окружении
```bash
> python3 -m venv venv
> . venv/bin/activate
(venv) > pip install -r requirements.txt
```

для запуска используется `gunicorn`
```bash
(venv) > gunicorn app:app -b 0.0.0.0:8080 --reload -w 1
```
или используя make
```bash
(venv) > make start-gunicorn
```
### Docker

Собрать и запустить docker-контейнер
 
```bash
> docker build -t file_uploader:latest . -f docker/Dockerfile
> docker run --name file_uploader -d --env-file .env -p 8080:8080 file_uploader:latest
```
или используя make
```bash
> make docker-run   # сборка и запуск
> make docker-logs  # вывод логов
```

### Docker-Compose
Использовать docker-compose

```bash
> docker-compose -f docker/docker-compose.yml up --build -d
> docker-compose -f docker/docker-compose.yml logs -f file_uploader
```

или используя make
```bash
> make run-dev   # сборка и запуск
> make logs      # вывод логов
> make stop-dev  # остановка и очистка
```

### Тесты

Для запуска тестов в `virtualenv` можно использовать 
```shell script
pytest -v
```