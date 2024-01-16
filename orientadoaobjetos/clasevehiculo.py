from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo, estado):
        self.marca = marca
        self.modelo = modelo
        self._estado = estado  # Atributo protegido

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado):
        self._estado = nuevo_estado

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

    def encender(self):
        self._estado = 'encendido'
        print(f"{self.marca} {self.modelo} ha sido encendido.")

    def apagar(self):
        self._estado = 'apagado'
        print(f"{self.marca} {self.modelo} ha sido apagado.")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, estado, ruedas):
        super().__init__(marca, modelo, estado)
        self._ruedas = ruedas

    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando.")

    def frenar(self):
        print(f"{self.marca} {self.modelo} frenando.")

    @staticmethod
    def numero_ruedas():
        print(f'El coche tiene 4 ruedas.')

class Moto(Vehiculo):
    def __init__(self, marca, modelo, estado, ruedas):
        super().__init__(marca, modelo, estado)
        self._ruedas = ruedas

    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando fuertemente.")

    def frenar(self):
        print(f"{self.marca} {self.modelo} frenando bruscamente.")

    @staticmethod
    def numero_ruedas():
        print(f'La moto tiene 2 ruedas.')

# Ejemplo de uso
mi_coche = Coche(marca="Toyota", modelo="Corolla", estado="apagado", ruedas=4)
mi_coche.encender()
mi_coche.acelerar()
mi_coche.frenar()
mi_coche.numero_ruedas()

mi_moto = Moto(marca="Honda", modelo="CBR", estado="apagado", ruedas=2)
mi_moto.encender()
mi_moto.acelerar()
mi_moto.frenar()
mi_moto.numero_ruedas()

