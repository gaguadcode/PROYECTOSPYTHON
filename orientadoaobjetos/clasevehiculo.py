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
    def __init__(self,  marca, modelo, estado, ruedas):
        super().__init__(self, marca, modelo, estado)
        self._ruedas = ruedas
    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando.")

    def frenar(self):
        print(f"{self.marca} {self.modelo} frenando.")
    @staticmethod
    def numero_ruedas(self):
        print(f'el coche tiene {self._ruedas}')
class Moto(Vehiculo):
    def __init__(self,  marca, modelo, estado, ruedas):
        super().__init__(self, marca, modelo, estado)
        self._ruedas = ruedas
    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando fuertemente.")

    def frenar(self):
        print(f"{self.marca} {self.modelo} frenando bruscamente.")
    @staticmethod
    def numero_ruedas(self):
        self._ruedas = 2
        print(f'la moto tiene {self._ruedas}')
