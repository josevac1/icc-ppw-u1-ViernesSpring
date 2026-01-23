import requests
import random
import time

BASE_URL = "http://localhost:8080"
API_PRODUCTS = f"{BASE_URL}/api/products"
API_USERS = f"{BASE_URL}/api/users"
API_CATEGORIES = f"{BASE_URL}/api/categories"

TIMEOUT = 30
TARGET_SUCCESS = 1000
MAX_ATTEMPTS = TARGET_SUCCESS * 5   # evita loop infinito si el backend está mal

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


def fetch_ids(url: str) -> list[int]:
    r = requests.get(url, timeout=TIMEOUT)
    r.raise_for_status()
    data = r.json()
    return [item["id"] for item in data]


def generate_unique_name(used_names: set[str]) -> str:
    # Genera y asegura que NO se repita en este script
    # Agrego un sufijo más grande para bajar prácticamente a 0 la colisión
    while True:
        brand = random.choice(BRANDS)
        product = random.choice(PRODUCTS)
        adjective = random.choice(ADJECTIVES)
        version = random.randint(1, 5)
        serial = random.randint(100000, 999999)  # extra para evitar duplicados en BD
        name = f"{brand} {adjective} {product} v{version}-{serial}"
        if name not in used_names:
            used_names.add(name)
            return name


def build_product(user_ids, category_ids, used_names: set[str]) -> dict:
    name = generate_unique_name(used_names)
    description = (
        f"Producto de alta calidad: {name}. "
        f"Características: durabilidad, rendimiento y diseño moderno."
    )
    price = round(random.uniform(10, 5000), 2)
    owner_id = random.choice(user_ids)

    num_categories = random.randint(2, min(4, len(category_ids)))
    categories = random.sample(category_ids, num_categories)

    return {
        "name": name,
        "description": description,
        "price": price,
        "userId": owner_id,
        "categoryIds": categories
    }


print("Leyendo usuarios y categorías desde la API...")
USER_IDS = fetch_ids(API_USERS)
CATEGORY_IDS = fetch_ids(API_CATEGORIES)

if not USER_IDS:
    raise SystemExit("❌ No hay usuarios. Ejecuta createuser.py primero.")
if len(CATEGORY_IDS) < 2:
    raise SystemExit("❌ Necesitas al menos 2 categorías. Arregla createcategories.py / API primero.")

print(f"Usuarios disponibles: {USER_IDS}")
print(f"Categorías disponibles: {CATEGORY_IDS}")
print(f"\nCreando productos hasta lograr {TARGET_SUCCESS} exitosos...\n")

session = requests.Session()
used_names = set()

success = 0
fails = 0
attempts = 0
start = time.time()

while success < TARGET_SUCCESS and attempts < MAX_ATTEMPTS:
    attempts += 1
    product = build_product(USER_IDS, CATEGORY_IDS, used_names)

    try:
        resp = session.post(API_PRODUCTS, json=product, timeout=TIMEOUT)

        if resp.status_code in (200, 201):
            success += 1
            if success % 100 == 0:
                elapsed = time.time() - start
                print(f"✓ {success}/{TARGET_SUCCESS} creados (intentos: {attempts}, tiempo: {elapsed:.2f}s)")
        else:
            fails += 1
            # Muestra pocos errores para no spamear
            if fails <= 10:
                print(f"✗ Falló intento {attempts} (success={success}): {product['name']}")
                print(f"  Status: {resp.status_code}")
                print(f"  Body: {resp.text[:250]}")
            time.sleep(0.2)

    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
        fails += 1
        if fails <= 10:
            print(f"✗ Error conexión/timeout en intento {attempts}: {e}")
        time.sleep(0.5)

elapsed = time.time() - start

print("\n" + "="*60)
print("RESUMEN")
print("="*60)
print(f"✅ Creados: {success}/{TARGET_SUCCESS}")
print(f"❌ Fallos: {fails}")
print(f"🔁 Intentos totales: {attempts}")
print(f"⏱️  Tiempo: {elapsed:.2f}s")
print("="*60)

if success < TARGET_SUCCESS:
    print("⚠️ No se llegó a 1000. Eso ya indica que el backend está fallando demasiado (mira logs de Spring).")
else:
    print("🎉 Listo: se generaron y crearon los 1000 productos.")
