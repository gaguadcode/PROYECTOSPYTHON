try:
    # Intenta abrir el archivo en modo de lectura
    with open("mi_archivo.txt", 'r') as file:
        # Si el archivo existe, emite un mensaje de error
        print("El archivo ya existe. No puedes continuar.")
except FileNotFoundError:
    # Si el archivo no existe, emite un mensaje y crea un nuevo archivo
    print("El archivo no existe. Creando un nuevo archivo...")
    with open("mi_archivo.txt", 'w') as file:
        # Escribe algunas líneas de texto en el archivo
        file.write("Hola, esta es la primera línea.\n")
        file.write("Aquí va la segunda línea.\n")
        file.write("Esta es la tercera línea.\n")
        file.write("Cuarta línea\n")
        file.write("¡Esta es la quinta línea!\n")

# Abre el archivo en modo de lectura
with open("mi_archivo.txt", 'r') as file:
    # El bucle lee y muestra cada linea
    for line in iter(file.readline, ''):
        print(line.strip())  # strip() elimina el salto de línea al final de cada línea
        print("Posición del cursor:", file.tell())  # Muestra la posición del cursor

# Abre el archivo en modo de escritura y agrega una nueva línea
with open("mi_archivo.txt", 'r+') as file:
    file.write("nueva linea al final\n")

# Abre el archivo en modo de anexar y agrega otra línea al final
with open("mi_archivo.txt", 'a+') as file:
    file.write("¡Otra línea más al final!\n")
    file.seek(0)  # Vuelve al inicio del archivo
    contenido_completo = file.read()  # Lee el archivo completo
    print("\nContenido completo después de anexar y volver al inicio:")
    print(contenido_completo)

try:
    with open("mi_archivo.txt", 'a') as file:
        file.write("¡Otra línea más al final!\n")
        file.seek(0)  # Vuelve al inicio del archivo
        contenido_completo = file.read()  # Lee el archivo completo
        print("\nContenido completo después de anexar y volver al inicio:")
        print(contenido_completo)
except Exception as e:
    print("\nError al abrir en modo 'a':", e)
