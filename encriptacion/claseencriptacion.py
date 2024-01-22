import os
import hashlib
from dotenv import load_dotenv

class HashConSalt:
    salt = None  # Atributo de clase para almacenar el salt
    # fuerzo a definir el salt antes de instanciar el objeto de creacion de hash
    def __init__(self):
        if not HashConSalt.salt:
            raise ValueError("El salt no ha sido configurado. Llame al método estático 'configurar_salt' primero.")

    @staticmethod
    def configurar_salt(nuevo_salt):
        HashConSalt.salt = nuevo_salt.encode()

    def hash_nombre_apellido(self, nombre, apellido):
        nombre_completo = nombre + " " + apellido
        nombre_completo_codificado = nombre_completo.encode()

        # Combinar el nombre completo codificado con el salt
        entrada_con_salt = nombre_completo_codificado + HashConSalt.salt

        # Crear el hash
        hash_objeto = hashlib.sha256(entrada_con_salt)
        hash_hex = hash_objeto.hexdigest()

        return hash_hex

# Cargar variables de entorno del archivo .env
load_dotenv()

# Obtener el salt del archivo .env
salt_from_env = os.environ.get("SALT")

# Configurar el salt en la clase
HashConSalt.configurar_salt(salt_from_env)

# Crear una instancia de la clase HashConSalt
hash_con_salt_instancia = HashConSalt()

# Ejemplo de uso
nombre_anonimizado = hash_con_salt_instancia.hash_nombre_apellido("Juan", "Pérez")
print(nombre_anonimizado)
