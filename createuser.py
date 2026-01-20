import requests
import json

# URL base de la API
BASE_URL = "http://localhost:8080/api/users"

# Datos para crear 10 usuarios
users_data = [
    {
        "name": "Usuario 1",
        "email": "usuario1@example.com",
        "password": "password123",
        "phone": "0987654321"
    },
    {
        "name": "Usuario 2",
        "email": "usuario2@example.com",
        "password": "password123",
        "phone": "0987654322"
    },
    {
        "name": "Usuario 3",
        "email": "usuario3@example.com",
        "password": "password123",
        "phone": "0987654323"
    },
    {
        "name": "Usuario 4",
        "email": "usuario4@example.com",
        "password": "password123",
        "phone": "0987654324"
    },
    {
        "name": "Usuario 5",
        "email": "usuario5@example.com",
        "password": "password123",
        "phone": "0987654325"
    },
    {
        "name": "Usuario 6",
        "email": "usuario6@example.com",
        "password": "password123",
        "phone": "0987654326"
    },
    {
        "name": "Usuario 7",
        "email": "usuario7@example.com",
        "password": "password123",
        "phone": "0987654327"
    },
    {
        "name": "Usuario 8",
        "email": "usuario8@example.com",
        "password": "password123",
        "phone": "0987654328"
    },
    {
        "name": "Usuario 9",
        "email": "usuario9@example.com",
        "password": "password123",
        "phone": "0987654329"
    },
    {
        "name": "Usuario 10",
        "email": "usuario10@example.com",
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
