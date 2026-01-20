import requests
import json

# URL base de la API
BASE_URL = "http://localhost:8080/api/categories"

# Datos para crear 10 categorías
categories_data = [
    {
        "name": "Electrónica"
    },
    {
        "name": "Ropa y Accesorios"
    },
    {
        "name": "Hogar y Jardín"
    },
    {
        "name": "Deportes y Recreación"
    },
    {
        "name": "Libros y Media"
    },
    {
        "name": "Alimentos y Bebidas"
    },
    {
        "name": "Belleza y Cuidado Personal"
    },
    {
        "name": "Juguetes y Juegos"
    },
    {
        "name": "Automóviles y Accesorios"
    },
    {
        "name": "Salud y Bienestar"
    }
]

# Crear las 10 categorías
for i, category in enumerate(categories_data, 1):
    try:
        response = requests.post(BASE_URL, json=category)
        if response.status_code == 201 or response.status_code == 200:
            print(f"✓ Categoría {i} creada exitosamente: {category['name']}")
            if response.text:
                print(f"  Respuesta: {response.json()}")
        else:
            print(f"✗ Error al crear categoría {i}")
            print(f"  Status: {response.status_code}")
            print(f"  Respuesta: {response.text}")
    except Exception as e:
        print(f"✗ Error de conexión al crear categoría {i}: {str(e)}")

print("\n✓ Proceso completado")
