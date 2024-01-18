import json
from datetime import datetime
from abc import ABC, abstractmethod
import uuid # librería para crear ids de vehiculo
class Vehiculo(ABC):
    def __init__(self, marca, modelo, estado):
        self.id = str(uuid.uuid4())
        self.marca = marca
        self.modelo = modelo
        self._estado = estado
        self.fecha_creacion = datetime.now() # el vehiculo se crea cuando se instancia el objeto y se añade la fecha
        self.fecha_ultimo_uso = None # fecha en la que se apagó el coche por última vez

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado):
        self._estado = nuevo_estado
        self.fecha_ultimo_uso = datetime.now()

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

    def encender(self):
        self._estado = 'encendido'
        self.fecha_ultimo_uso = datetime.now()
        print(f"{self.marca} {self.modelo} ha sido encendido.")

    def apagar(self):
        self._estado = 'apagado'
        self.fecha_ultimo_uso = datetime.now()
        print(f"{self.marca} {self.modelo} ha sido apagado.")

    def obtener_atributos(self):
        # Retorna un diccionario con los atributos del vehículo
        return {
            "id": self.id,
            "marca": self.marca,
            "modelo": self.modelo,
            "estado": self._estado,
            "fecha_creacion": self.fecha_creacion.strftime("%d-%m-%Y"),
            "fecha_ultimo_uso": self.fecha_creacion.strftime("%d-%m-%Y") if self.fecha_ultimo_uso else None
        }

    def guardar_en_json(self, archivo_json):
        # Cargar existentes o inicializar una lista vacía
        try:
            with open(archivo_json, 'r') as file:
                vehiculos = json.load(file)
        except FileNotFoundError:
            vehiculos = []

        # Agregar el vehículo actual a la lista
        vehiculos.append(self.obtener_atributos())

        # Guardar la lista actualizada en el archivo JSON
        with open(archivo_json, 'w') as file:
            json.dump(vehiculos, file, indent = 4)

class Coche(Vehiculo):
    def __init__(self, marca, modelo, estado, ruedas):
        super().__init__(marca, modelo, estado)
        self._ruedas = ruedas

    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando.")

    def frenar(self):
        print(f"{self.marca} {self.modelo} frenando.")

    def numero_ruedas(self):
        print(f'El coche tiene {self._ruedas} ruedas.')

class Moto(Vehiculo):
    def __init__(self, marca, modelo, estado, ruedas):
        super().__init__(marca, modelo, estado)
        self._ruedas = ruedas

    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando fuertemente.")

    def frenar(self):
        print(f"{self.marca} {self.modelo} frenando bruscamente.")

    def numero_ruedas(self):
        print(f'La moto tiene {self._ruedas} ruedas.')

class Barco(Vehiculo):
    def __init__(self, marca, modelo, estado, eslora):
        super().__init__(marca, modelo, estado)
        self.eslora = eslora
    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando fuertemente.")

    def frenar(self):
        print(f"{self.marca} {self.modelo} frenando bruscamente.")

    def navegar(self):
        print(f"{self.marca} {self.modelo} navegando.")

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, estado, tipo):
        super().__init__(marca, modelo, estado)
        self.tipo = tipo
    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando fuertemente.")

    def frenar(self):
        print(f"{self.marca} {self.modelo} frenando bruscamente.")

    def pedalear(self):
        print(f"{self.marca} {self.modelo} pedaleando.")

'''# Ejemplo de uso
mi_coche = Coche(marca="Toyota", modelo="Corolla", estado="apagado", ruedas=4)
mi_coche.encender()
mi_coche.acelerar()
mi_coche.frenar()
mi_coche.numero_ruedas()

# Guardar los atributos del coche en un archivo JSON
mi_coche.guardar_en_json("vehiculos.json")

mi_moto = Moto(marca="Honda", modelo="CBR", estado="apagado", ruedas=2)
mi_moto.encender()
mi_moto.acelerar()
mi_moto.frenar()
mi_moto.numero_ruedas()

# Guardar los atributos de la moto en el mismo archivo JSON
mi_moto.guardar_en_json("vehiculos.json")

#otros ejemplos:
mi_barco = Barco(marca="Yamaha", modelo="Speedboat", estado="apagado", eslora=10.5)
mi_bicicleta = Bicicleta(marca="Trek", modelo="Mountain Bike", estado="apagado", tipo="Montaña")
mi_barco.guardar_en_json("vehiculos.json")
mi_bicicleta.guardar_en_json("vehiculos.json")

#Finalmente hago un print del json
with open("vehiculos.json", 'r') as file:
        contenido = json.load(file)
        print(json.dumps(contenido, indent=4))'''