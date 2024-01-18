from clasevehiculomejorada import  Coche, Moto, Barco, Bicicleta
import json
# instancio varios objetos
mi_coche = Coche(marca="Toyota", modelo="Corolla", estado="apagado", ruedas=4)
mi_moto = Moto(marca="Honda", modelo="CBR", estado="apagado", ruedas=2)
mi_barco = Barco(marca="Yamaha", modelo="Speedboat", estado="apagado", eslora=10.5)
mi_bicicleta = Bicicleta(marca="Trek", modelo="Mountain Bike", estado="apagado", tipo="Montaña")
#Guardo en json los datos
mi_coche.guardar_en_json("vehiculos.json")
mi_moto.guardar_en_json("vehiculos.json")
mi_barco.guardar_en_json("vehiculos.json")
mi_bicicleta.guardar_en_json("vehiculos.json")

# quiero sacar el cuarto elemento del json
with open('vehiculos.json', 'r') as file:
    json_data = json.load(file)

# Iterar sobre los elementos 
iterador = iter(json_data)

# Utilizar next para obtener elemento a elemento
try:
    while True:
        elemento = next(iterador)
        print("Elemento:", elemento)
except StopIteration:
    print("Fin de la lista.")