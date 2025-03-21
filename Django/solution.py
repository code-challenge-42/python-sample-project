from django.db import models
from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from copy import deepcopy
import json

# Modelo de Usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()

# Vista basada en clases
class UsuarioView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            usuario = Usuario.objects.create(**data)
            return JsonResponse({"mensaje": "Usuario creado", "id": usuario.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def get(self, request, usuario_id):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            usuario_dict = deepcopy({"nombre": usuario.nombre, "email": usuario.email, "edad": usuario.edad})
            return JsonResponse(usuario_dict)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)
