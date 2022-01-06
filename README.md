# Dockerizing Django with Celery, Redis, Gunicorn, and Nginx
Uses gunicorn + nginx + ci/cd.

1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

2. Run the collectstatic management command:

    ```sh
    $ docker-compose exec web python manage.py collectstatic
    ```


1. Test it out at [http://localhost](http://localhost/feed/rss/)
1. Admin at [http://localhost/admin](http://localhost/admin) 
```sh
username: admin
password: admin
```
