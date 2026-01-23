import requests
import json

# URL base de la API
BASE_URL = "http://localhost:8080/api/categories"

# Datos para crear 10 categorías
categories_data = [
    {
        "name": "Electrónica",
        "description": "Dispositivos electrónicos modernos incluyendo computadoras, smartphones, accesorios tecnológicos y más."
    },
    {
        "name": "Ropa y Accesorios",
        "description": "Prendas de vestir para todas las edades, estilos y ocasiones. Incluye ropa formal, casual y deportiva."
    },
    {
        "name": "Hogar y Jardín",
        "description": "Artículos para el hogar, muebles, decoración, herramientas de jardinería y equipos para el cuidado del jardín."
    },
    {
        "name": "Deportes y Recreación",
        "description": "Equipo deportivo, artículos de fitness, juegos al aire libre y equipos para actividades recreativas."
    },
    {
        "name": "Libros y Media",
        "description": "Libros de todos los géneros, películas en DVD, música, audiolibros y contenido digital."
    },
    {
        "name": "Alimentos y Bebidas",
        "description": "Productos comestibles frescos, conservas, bebidas, alimentos gourmet y complementos nutricionales."
    },
    {
        "name": "Belleza y Cuidado Personal",
        "description": "Cosméticos, productos de skincare, higiene personal, fragancias y tratamientos de belleza."
    },
    {
        "name": "Juguetes y Juegos",
        "description": "Juguetes educativos y de entretenimiento para niños, juegos de mesa y juegos de construcción."
    },
    {
        "name": "Automóviles y Accesorios",
        "description": "Accesorios para vehículos, repuestos, herramientas de automoción y equipos de mantenimiento."
    },
    {
        "name": "Salud y Bienestar",
        "description": "Productos para la salud, suplementos vitamínicos, equipos de bienestar y artículos médicos de uso personal."
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
