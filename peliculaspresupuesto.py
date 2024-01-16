from colorama import Fore
class ListaPeliculas:
    def __init__(self):
        self.peliculas = {}

    def añadir_pelicula(self, nombre, director, año, presupuesto):
        if nombre not in self.peliculas:
            self.peliculas[nombre] = {'Director': director, 'Año': año, 'Presupuesto': presupuesto}
            print(f'Película "{nombre}" añadida a la lista.')
        else:
            print(f'La película "{nombre}" ya está en la lista.')

    def eliminar_pelicula(self, nombre):
        if nombre in self.peliculas:
            del self.peliculas[nombre]
            print(f'Película "{nombre}" eliminada de la lista.')
        else:
            print(f'La película "{nombre}" no está en la lista.')

    def mostrar_peliculas(self):
        if not self.peliculas:
            print('La lista de películas está vacía.')
        else:
            print('Lista de películas:')
            for pelicula, metadata in self.peliculas.items():
                print(f'"{pelicula}" - Director: {metadata["Director"]}, Año: {metadata["Año"]}, Presupuesto: {metadata["Presupuesto"]}')

    def modificar_pelicula(self, nombre, director, año, presupuesto):
        if nombre in self.peliculas:
            self.peliculas[nombre]['Director'] = director
            self.peliculas[nombre]['Año'] = año
            self.peliculas[nombre]['Presupuesto'] = presupuesto
            print(f'Metadatos de la película "{nombre}" modificados.')
        else:
            print(f'La película "{nombre}" no está en la lista.')

    def buscar_pelicula(self, nombre):
        if nombre in self.peliculas:
            print(f'La película "{nombre}" está en la lista.')
            metadata = self.peliculas[nombre]
            print(f'Metadatos: Director: {metadata["Director"]}, Año: {metadata["Año"]}, Presupuesto: {metadata["Presupuesto"]}')
        else:
            print(f'La película "{nombre}" no está en la lista.')

    def modificar_presupuestos(self, porcentaje):
        for pelicula in self.peliculas.values():
            presupuesto_actual = pelicula['Presupuesto']
            nuevo_presupuesto = presupuesto_actual * (1 + porcentaje / 100)

            # Asegurar que el nuevo presupuesto no sea menor a 1
            nuevo_presupuesto = max(nuevo_presupuesto, 1)

            pelicula['Presupuesto'] = nuevo_presupuesto

# Función principal
def main():
    lista_peliculas = ListaPeliculas()

    while True:
        print('\n--- Menú ---')
        print(f'{Fore.BLUE}1.{Fore.BLUE} Añadir Película')
        print(f'{Fore.GREEN}2.{Fore.GREEN} Eliminar Película')
        print(f'{Fore.RED}3.{Fore.RED} Mostrar Lista de Películas')
        print(f'{Fore.YELLOW}4.{Fore.YELLOW} Modificar Pelicula')
        print(f'{Fore.BLACK}5.{Fore.BLACK} Buscar Película')
        print(f'{Fore.WHITE}6.{Fore.WHITE} Modificar presupuestos')
        print(f'{Fore.WHITE}7.{Fore.WHITE} Salir')

        opcion = input('Selecciona una opción (1-7): ')

        if opcion == '1':
            nombre = input('Introduce el nombre de la película: ')
            director = input('Introduce el nombre del director: ')
            año = input('Introduce el año de lanzamiento: ')
            presupuesto = float(input('Introduce el presupuesto de la película: '))
            lista_peliculas.añadir_pelicula(nombre, director, año, presupuesto)
        elif opcion == '2':
            nombre = input('Introduce el nombre de la película a eliminar: ')
            lista_peliculas.eliminar_pelicula(nombre)
        elif opcion == '3':
            lista_peliculas.mostrar_peliculas()
        elif opcion == '4':
            nombre = input('Introduce el nombre de la película a modificar: ')
            director = input('Introduce el nuevo nombre del director: ')
            año = input('Introduce el nuevo año de lanzamiento: ')
            presupuesto = float(input('Introduce el nuevo presupuesto de la película: '))
            lista_peliculas.modificar_pelicula(nombre, director, año, presupuesto)
        elif opcion == '5':
            nombre = input('Introduce el nombre de la película a buscar: ')
            lista_peliculas.buscar_pelicula(nombre)
        elif opcion == '6':
            try:
                porcentaje = float(input('Introduce el porcentaje de aumento para los presupuestos: '))
                if porcentaje < 0:
                    raise ValueError("El porcentaje debe ser positivo.")
                lista_peliculas.modificar_presupuestos(porcentaje)
                print(f'Presupuestos modificados en un {porcentaje}%')
            except ValueError as e:
                print(f'Error: {e}')
        elif opcion == '7':
            print('Saliendo del programa. ¡Hasta luego!')
            break
        else:
            print('Opción no válida. Por favor, elige una opción válida.')

if __name__ == "__main__":
    main()
