import requests
import random
import time

# URL base de la API
BASE_URL = "http://localhost:8080/api/products"

# IDs de usuarios disponibles (creados anteriormente)
USER_IDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# IDs de categorías disponibles (asumiendo que existen del 1-10)
CATEGORY_IDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Palabras para generar nombres buscables
BRANDS = ["Samsung", "Apple", "Sony", "LG", "HP", "Dell", "Lenovo", "ASUS", "Canon", "Nikon", 
          "Nike", "Adidas", "Puma", "Levi's", "Tommy", "Ralph Lauren", "Gucci", "Louis Vuitton",
          "Philips", "Bosch", "Siemens", "Electrolux", "Whirlpool", "Fujitsu", "Panasonic"]

PRODUCTS = ["Laptop", "Monitor", "Mouse", "Teclado", "Auriculares", "Webcam", "Router", 
            "Impresora", "Escáner", "Proyector", "TV", "Microondas", "Refrigerador", 
            "Lavadora", "Secadora", "Horno", "Licuadora", "Cafetera", "Aspiradora",
            "Zapatos", "Camiseta", "Pantalón", "Chaqueta", "Sombrero", "Guantes", "Calcetines",
            "Mochila", "Bolso", "Cinturón", "Corbata", "Reloj", "Gafas", "Anillo",
            "Collar", "Pulsera", "Pendientes", "Cámara", "Lente", "Trípode", "Flash"]

ADJECTIVES = ["Profesional", "Premium", "Económico", "Compacto", "Portátil", "Inalámbrico",
              "HD", "Ultra", "Smart", "Inteligente", "Digital", "Analógico", "Vintage",
              "Moderno", "Clásico", "Deportivo", "Casual", "Formal", "Elegante", "Resistente"]

# Generar datos de 1000 productos
def generate_products(count=1000):
    products = []
    for i in range(count):
        brand = random.choice(BRANDS)
        product = random.choice(PRODUCTS)
        adjective = random.choice(ADJECTIVES)
        
        name = f"{brand} {adjective} {product} v{random.randint(1, 5)}"
        
        # Generar descripción
        description = f"Producto de alta calidad: {name}. Características: durabilidad, rendimiento y diseño moderno. Ideal para profesionales y usuarios domésticos."
        
        # Precio entre $10 y $5000
        price = round(random.uniform(10, 5000), 2)
        
        # Usuario aleatorio (al menos 5 usuarios)
        owner_id = random.choice(USER_IDS)
        
        # Al menos 2 categorías por producto
        num_categories = random.randint(2, 4)
        categories = random.sample(CATEGORY_IDS, min(num_categories, len(CATEGORY_IDS)))
        
        product_data = {
            "name": name,
            "description": description,
            "price": price,
            "userId": owner_id,
            "categoryIds": categories
        }
        
        products.append(product_data)
    
    return products

print("Generando 1000 productos...")
products = generate_products(1000)

print(f"Iniciando carga de {len(products)} productos en la API...")
print(f"URL: {BASE_URL}\n")

success_count = 0
error_count = 0
start_time = time.time()

for i, product in enumerate(products, 1):
    try:
        response = requests.post(BASE_URL, json=product, timeout=10)
        
        if response.status_code == 201 or response.status_code == 200:
            success_count += 1
            if i % 100 == 0:
                elapsed = time.time() - start_time
                print(f"✓ {i}/1000 productos cargados exitosamente (tiempo: {elapsed:.2f}s)")
        else:
            error_count += 1
            if error_count <= 5:  # Mostrar solo los primeros 5 errores
                print(f"✗ Error al cargar producto {i}: {product['name']}")
                print(f"  Status: {response.status_code}")
                print(f"  Respuesta: {response.text[:100]}")
    
    except requests.exceptions.Timeout:
        error_count += 1
        if error_count <= 5:
            print(f"✗ Timeout al cargar producto {i}")
    
    except Exception as e:
        error_count += 1
        if error_count <= 5:
            print(f"✗ Error de conexión al cargar producto {i}: {str(e)}")
    
    # Pequeña pausa entre peticiones para no sobrecargar el servidor
    if i % 50 == 0:
        time.sleep(0.5)

elapsed = time.time() - start_time

print("\n" + "="*60)
print("RESUMEN DE CARGA MASIVA")
print("="*60)
print(f"✓ Productos cargados exitosamente: {success_count}/1000")
print(f"✗ Errores: {error_count}/1000")
print(f"⏱️  Tiempo total: {elapsed:.2f} segundos")
print(f"📊 Velocidad: {success_count/elapsed:.2f} productos/segundo")
print("="*60)
