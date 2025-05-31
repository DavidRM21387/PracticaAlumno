class DatonInvalidoError(Exception):
    """Excepcion para datos inválidos en la clase Alumnos."""
    pass

class Alumno:
    def __init__(self, nombre: str, apellido: str, edad: int, matricula: int):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.matricula = matricula

    def mostrar_info(self) -> None:
        """Muestra informacion completa del alumno"""
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad} años")
        print(f"Matricula: {self.matricula}")
        print("-" * 40)

    @staticmethod
    def mayor_de_edad(alumno1: "Alumno", alumno2: "Alumno") -> "Alumno":
        """
        recibe dos objertos alumno y devuelve el que tenga mayor edad,
        si tienen la misma edad, devuelve none.
        """
        if alumno1.edad > alumno2.edad:
            return alumno1
        elif alumno2.edad > alumno1.edad:
            return alumno2
        else:
            return None

def llenar_alumnos(lista_alumnos: list) -> None:
    """
    Solicita al usuario la cantidad de alumnos que va a ingresar
    y luego pide nombre, apellido, edad y matricula de cada uno.
    Si hay un error en los datos se activa el DatonInvalidoError
    con un mensaje
    """ 
    try:
        cantidad_input = input("Cauntos alumnos va ingresar? ")
        cantidad = int(cantidad_input)
        if cantidad <= 0:
            raise DatonInvalidoError("La cantidad de alumnos debe ser mayor a 0.")
    except ValueError:
        raise DatonInvalidoError(f"Valor invalido para la cantidad de alumnos: '{cantidad_input}'. Debe ser un numero entero.")
    except DatonInvalidoError:
        # relanzamos para que lo capture el main
        raise

    for i in range(cantidad):
        print(f"--- Ingresando datos del alumno {i + 1} de {cantidad}---")
        nombre = input("Nombre: ").strip()
        apellido = input("apellido: ").strip()

        # edad
        try:
            edad_input = input("edad: ")
            edad = int(edad_input)
            if edad < 0:
                raise DatonInvalidoError("La edad no puede ser negativa.")
        except ValueError:
            raise DatonInvalidoError(f"Valor no valido para edad: '{edad_input}'. Debe ser un numero entero.")
        except DatonInvalidoError:
            # relanzamos para que lo capture el main
            raise

        # matricula
        try:
            matricula_input = input("Matricula: ")
            matricula = int(matricula_input)
            if matricula <= 0:
                raise DatonInvalidoError(f"La matricula debe ser un numero positivo: {matricula_input}.")
        except ValueError:
            raise DatonInvalidoError(f"Valor invalido para matricula: {matricula_input}. Debe ser un numero entero.")
        except DatonInvalidoError:
            # relanzamos para que lo capture el main
            raise

        # Si todos los datos son validos, creamos el objeto alumno y lo agregamos a la lista
        alumno = Alumno(nombre, apellido, edad, matricula)
        lista_alumnos.append(alumno)

def main():
    lista_de_alumnos = []

    # primero llenamos la list de almnos
    try:
        llenar_alumnos(lista_de_alumnos)
    except DatonInvalidoError as err:
        print(f"Error al ingresar los datos de los alumnos: {err}")
        print("El programa se cerrara, por favor intente de nuevo.")
        return

    # despues mostramos la informacion de cada alumno 
    print("\n--- Informacion de los alumnos ---")
    for idx, alumno in enumerate(lista_de_alumnos, start=1):
        print(f"Alumno {idx}:")
        alumno.mostrar_info()

    # Comparar a los dos primeros alumnos(Si hay al menos dos)
    if len(lista_de_alumnos) >= 2:
        alumno1 = lista_de_alumnos[0]
        alumno2 = lista_de_alumnos[1]
        mas_viejo = alumno.mayor_de_edad(alumno1, alumno2)

        print("\n--- Comparacion de los dos primeros alumnos ---")
        print(f"Alumno 1: {alumno1.nombre} {alumno1.apellido}, Edad: {alumno1.edad}")
        print(f"Alumno 2: {alumno2.nombre} {alumno2.apellido}, Edad: {alumno2.edad}")

        if mas_viejo is None:
            print("Ambos alumnos tienen la misma edad.")
        else:
            print(f"El alumno mayor es: {mas_viejo.nombre} {mas_viejo.apellido}, Edad: {mas_viejo.edad}")
    else:
        print("No hay suficientes alumnos para comparar edades.")

if __name__ == "__main__":
    main()
