from colorama import Fore
class ListaPeliculas:
    def __init__(self):
        self.peliculas = []

    def añadir_pelicula(self, nombre):
        if nombre not in self.peliculas:
            self.peliculas.append(nombre)
            print(f'Película "{nombre}" añadida a la lista.')
        else:
            print(f'La película "{nombre}" ya está en la lista.')

    def eliminar_pelicula(self, nombre):
        if nombre in self.peliculas:
            self.peliculas.remove(nombre)
            print(f'Película "{nombre}" eliminada de la lista.')
        else:
            print(f'La película "{nombre}" no está en la lista.')

    def mostrar_peliculas(self):
        if not self.peliculas:
            print('La lista de películas está vacía.')
        else:
            print('Lista de películas:')
            for pelicula in self.peliculas:
                print(f'- {pelicula}')

    def buscar_pelicula(self, nombre):
        if nombre in self.peliculas:
            print(f'La película "{nombre}" está en la lista.')
        else:
            print(f'La película "{nombre}" no está en la lista.')

# Función principal
def main():
    lista_peliculas = ListaPeliculas()

    while True:
        print('\n--- Menú ---')
        print(f'{Fore.BLUE}1.{Fore.BLUE} Añadir Película')
        print(f'{Fore.GREEN}2.{Fore.GREEN} Eliminar Película')
        print(f'{Fore.RED}3.{Fore.RED} Mostrar Lista de Películas')
        print(f'{Fore.YELLOW}4.{Fore.YELLOW} Buscar Película')
        print(f'{Fore.WHITE}5.{Fore.WHITE} Salir')

        opcion = input('Selecciona una opción (1-5): ')

        if opcion == '1':
            nombre = input('Introduce el nombre de la película: ')
            lista_peliculas.añadir_pelicula(nombre)
        elif opcion == '2':
            nombre = input('Introduce el nombre de la película a eliminar: ')
            lista_peliculas.eliminar_pelicula(nombre)
        elif opcion == '3':
            lista_peliculas.mostrar_peliculas()
        elif opcion == '4':
            nombre = input('Introduce el nombre de la película a buscar: ')
            lista_peliculas.buscar_pelicula(nombre)
        elif opcion == '5':
            print('Saliendo del programa. ¡Hasta luego!')
            break
        else:
            print('Opción no válida. Por favor, elige una opción válida.')

if __name__ == "__main__":
    main()
