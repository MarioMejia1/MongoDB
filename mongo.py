import os
from pymongo import MongoClient

# Obtener la cadena de conexión desde una variable de entorno
mongo_uri = os.getenv('MONGODB_URI')

# Conectar con MongoDB
client = MongoClient(mongo_uri)

# Seleccionar la base de datos
db = client.provincias_rd

# Crear una colección llamada provincias
provincias = db.provincias

# Datos de ejemplo de provincias de República Dominicana
datos_provincias = [
    {"nombre": "Santo Domingo"},
    {"nombre": "Santiago"},
    {"nombre": "San Cristóbal"},
    {"nombre": "La Altagracia"},
    {"nombre": "La Romana"}
]

# Insertar los datos en la colección
provincias.insert_many(datos_provincias)

print("Datos insertados correctamente en la base de datos.")

# Consultar todas las provincias
todas_las_provincias = provincias.find()

# Imprimir las provincias
print("Listado de provincias:")
for provincia in todas_las_provincias:
    print(provincia["nombre"])

# Cerrar la conexión con MongoDB
client.close()
