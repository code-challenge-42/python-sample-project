# Django
__Objetivo: Implementar un endpoint en Django que cree y recupere usuarios desde la base de datos.__

__Instrucciones__
 - Crea un modelo Usuario con nombre, email y edad.
 - Implementa una vista que permita:
    - Crear un usuario mediante un POST.
    - Obtener un usuario por su id con GET.
 - Usa try-except para manejar errores de base de datos.
 - Asegúrate de usar deepcopy antes de modificar los datos.

__Notas__

python manage.py makemigrations usuarios
python manage.py migrate

python manage.py runserver