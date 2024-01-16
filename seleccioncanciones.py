import random

# Listas de canciones y sus duraciones en minutos
canciones_ingles = ["Imagine", "Bohemian Rhapsody", "Hey Jude", "Hotel California"]
duracion_ingles = [3.0, 6.0, 7.5, 6.5]

canciones_espanol = ["La Bamba", "Cielito Lindo", "Besame Mucho", "El Rey"]
duracion_espanol = [2.5, 3.2, 4.0, 3.8]

# Combinar las dos listas en un diccionario usando zip
canciones_dict = dict(zip(canciones_ingles + canciones_espanol, duracion_ingles + duracion_espanol))

# Ordenar el diccionario por duración de canciones de mayor a menor
canciones_ordenadas = dict(sorted(canciones_dict.items(), key=lambda item: item[1], reverse=True))

# Seleccionar las 3 canciones más largas
top_3_canciones = dict(list(canciones_ordenadas.items())[:3])

# Seleccionar aleatoriamente algunas canciones
num_canciones_aleatorias = 2
canciones_aleatorias = dict(random.sample(canciones_dict.items(), num_canciones_aleatorias))

# Mostrar resultados
print("Diccionario de Canciones:")
print(canciones_dict)

print("\nTop 3 Canciones Más Largas:")
print(top_3_canciones)

print("\nSelección Aleatoria de Canciones:")
print(canciones_aleatorias)
