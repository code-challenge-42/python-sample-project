# FastAPI
__Objetivo: Crear un API en FastAPI para gestionar libros.__

__Instrucciones__
 - Crea un modelo Libro con id, titulo y autor.
 - Implementa un endpoint para:
 - Agregar un libro con POST.
 - Obtener un libro por id con GET.
 - Usa try-except para el manejo de errores.
 - Usa deepcopy antes de devolver los datos.

__Notas__

pip install -r requirements.txt
flask run

__Test__

curl -X POST http://127.0.0.1:8000/producto/ -H "Content-Type: application/json" -d '{"nombre": "Vaso", "precio": "98"}'
curl -X GET http://127.0.0.1:8000/libro/1/