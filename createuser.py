import requests
import json

# URL base de la API
BASE_URL = "http://localhost:8080/api/users"

# Datos para crear 10 usuarios
users_data = [
    {
        "name": "Carlos Rodríguez",
        "email": "carlos.rodriguez@techcorp.com",
        "password": "password123",
        "phone": "0987654321"
    },
    {
        "name": "María García",
        "email": "maria.garcia@innovate.com",
        "password": "password123",
        "phone": "0987654322"
    },
    {
        "name": "Juan Martínez",
        "email": "juan.martinez@solutions.com",
        "password": "password123",
        "phone": "0987654323"
    },
    {
        "name": "Ana López",
        "email": "ana.lopez@digital.com",
        "password": "password123",
        "phone": "0987654324"
    },
    {
        "name": "Roberto Sánchez",
        "email": "roberto.sanchez@enterprise.com",
        "password": "password123",
        "phone": "0987654325"
    },
    {
        "name": "Sandra Pérez",
        "email": "sandra.perez@webservices.com",
        "password": "password123",
        "phone": "0987654326"
    },
    {
        "name": "Felipe Flores",
        "email": "felipe.flores@cloudtech.com",
        "password": "password123",
        "phone": "0987654327"
    },
    {
        "name": "Patricia Díaz",
        "email": "patricia.diaz@softtech.com",
        "password": "password123",
        "phone": "0987654328"
    },
    {
        "name": "Jorge Hernández",
        "email": "jorge.hernandez@devops.com",
        "password": "password123",
        "phone": "0987654329"
    },
    {
        "name": "Valentina Castillo",
        "email": "valentina.castillo@nextgen.com",
        "password": "password123",
        "phone": "0987654330"
    }
]

# Crear los 10 usuarios
for i, user in enumerate(users_data, 1):
    try:
        response = requests.post(BASE_URL, json=user)
        if response.status_code == 201 or response.status_code == 200:
            print(f"✓ Usuario {i} creado exitosamente")
            print(f"  Respuesta: {response.json()}")
        else:
            print(f"✗ Error al crear usuario {i}")
            print(f"  Status: {response.status_code}")
            print(f"  Respuesta: {response.text}")
    except Exception as e:
        print(f"✗ Error de conexión al crear usuario {i}: {str(e)}")

print("\n✓ Proceso completado")
