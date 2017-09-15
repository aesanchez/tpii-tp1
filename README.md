# Trabajo Practico n° 1

Repositorio para el desarrollo del primer Trabajo Practico de la materia Taller de Proyectos II (I119) de la [UNLP](http://www.unlp.edu.ar/)  

## Deploy en Heroku

Se puede observar lo implementado en [Heroku](https://tpii-tp1.herokuapp.com/).

#### Pasos para deployar una aplicacion Flask en Heroku.

1. Instalar prerequisitos:

    `$ pip install flask gunicorn`

2. Desarrollar aplicacion Flask
3. Detallar nuestro *requirements.txt* con como minimo:

    ```
    Flask
    gunicorn
    ```

4. Crear el Procfile con el siguiente contenido:

    `web: gunicorn app:app`

5. Instalar [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) e iniciar sesion:

    `$ heroku login`

6. Crear un dominio en Heroku
7. En el directorio del proyecto:

    ```
    $ heroku git:remote -a <mi_nombre_de_aplicacion_en_heroku>
    $ git push heroku master
    ```

## Alumnos
* Agustín Sánchez
* Agustín García
* Nahuel Ternouski
