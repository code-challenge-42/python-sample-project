# Flask
__Objetivo: Implementar un API con Flask para manejar productos.__

__Instrucciones__
 - Crea un modelo Producto con id, nombre y precio.
 - Implementa un endpoint para:
 - Crear un producto con POST.
 - Obtener un producto por id con GET.
 - Usa try-except para capturar errores.
 - Usa deepcopy antes de devolver los datos.

 __Notas__

pip install -r requirements.txt
uvicorn main:app --reload

__Test__

curl -X POST http://127.0.0.1:8000/libro/ -H "Content-Type: application/json" -d '{"titulo": "Clean Code", "autor": "Robert Cecil Martin"}'
curl -X GET http://127.0.0.1:8000/libro/1/