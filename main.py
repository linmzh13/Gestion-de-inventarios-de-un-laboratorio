from encargado import Encargado
from estudiante import Estudiante
from equipo import Equipo


equipos = []
estudiantes = []


encargado = Encargado(
    "UPN001",
    "admin",
    "4567",
    "administrador1@gmail.com",
    "Encargado"
)


def cargar_equipos():

    try:
        archivo = open("equipos.txt", "r")

        for linea in archivo:

            datos = linea.strip().split(";")

            if len(datos) == 4:

                equipo = Equipo(
                    datos[0],
                    datos[1],
                    int(datos[2]),
                    datos[3]
                )

                equipos.append(equipo)

        archivo.close()

    except FileNotFoundError:

        print("No existe el archivo equipos.txt")


def guardar_equipos():

    archivo = open("equipos.txt", "w")

    for equipo in equipos:

        archivo.write(
            equipo.id + ";" +
            equipo.nombre + ";" +
            str(equipo.cantidad) + ";" +
            equipo.estado + "\n"
        )

    archivo.close()


def cargar_estudiantes():

    try:
        archivo = open("estudiantes.txt", "r")

        for linea in archivo:

            datos = linea.strip().split(";")

            if len(datos) == 6:

                estudiante = Estudiante(
                    datos[0],
                    datos[1],
                    datos[2],
                    datos[3],
                    datos[4],
                    datos[5]
                )

                estudiantes.append(estudiante)

        archivo.close()

    except FileNotFoundError:

        print("No existe el archivo estudiantes.txt")


def guardar_estudiantes():

    archivo = open("estudiantes.txt", "w")

    for estudiante in estudiantes:

        archivo.write(
            estudiante.id + ";" +
            estudiante.nombre + ";" +
            estudiante.password + ";" +
            estudiante.correo + ";" +
            estudiante.rol + ";" +
            estudiante.telefono + "\n"
        )

    archivo.close()


def buscar_equipo(id):

    for equipo in equipos:

        if equipo.id == id:
            return equipo

    return None


def iniciar_sesion():

    id = input("Ingrese su ID: ")
    password = input("Ingrese su contraseña: ")

    if id == encargado.id and password == encargado.password:
        return encargado

    for estudiante in estudiantes:

        if id == estudiante.id and password == estudiante.password:
            return estudiante

    return None


def menu_encargado():

    while True:

        print("\n==============================")
        print("       MENÚ ENCARGADO")
        print("==============================")

        print("1. Consultar inventario")
        print("2. Registrar equipo")
        print("3. Registrar estudiante")
        print("4. Consultar estudiantes")
        print("5. Consultar estado de equipo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")


        if opcion == "1":

            encargado.consultar_inventario(equipos)


        elif opcion == "2":

            id = input("ID del equipo: ")
            nombre = input("Nombre del equipo: ")
            cantidad = int(input("Cantidad: "))

            equipo = Equipo(
                id,
                nombre,
                cantidad,
                "Disponible"
            )

            encargado.registrar_equipo(
                equipos,
                equipo
            )

            guardar_equipos()


        elif opcion == "3":

            id = input("ID del estudiante: ")
            nombre = input("Nombre: ")
            password = input("Contraseña: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")

            estudiante = Estudiante(
                id,
                nombre,
                password,
                correo,
                "Estudiante",
                telefono
            )

            encargado.registrar_persona(
                estudiantes,
                estudiante
            )

            guardar_estudiantes()


        elif opcion == "4":

            encargado.consultar_estudiante(
                estudiantes
            )


        elif opcion == "5":

            id_equipo = input(
                "Ingrese el ID del equipo: "
            )

            equipo = buscar_equipo(id_equipo)

            if equipo != None:

                equipo.consultar_estado()

            else:

                print("Equipo no encontrado.")


        elif opcion == "6":

            print("Sesión finalizada.")
            break


        else:

            print("Opción no válida.")


def menu_estudiante(estudiante):

    while True:

        print("\n==============================")
        print("       MENÚ ESTUDIANTE")
        print("==============================")

        print("1. Consultar inventario")
        print("2. Solicitar préstamo")
        print("3. Consultar estado de equipo")
        print("4. Actualizar información")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")


        if opcion == "1":

            estudiante.consultar_inventario(
                equipos
            )


        elif opcion == "2":

            id_equipo = input(
                "Ingrese el ID del equipo: "
            )

            equipo = buscar_equipo(id_equipo)

            if equipo != None:

                estudiante.solicitar_prestamo(
                    equipo
                )

                guardar_equipos()

            else:

                print("Equipo no encontrado.")


        elif opcion == "3":

            id_equipo = input(
                "Ingrese el ID del equipo: "
            )

            equipo = buscar_equipo(id_equipo)

            if equipo != None:

                estudiante.consultar_equipo(
                    equipo
                )

            else:

                print("Equipo no encontrado.")


        elif opcion == "4":

            correo = input(
                "Nuevo correo: "
            )

            telefono = input(
                "Nuevo teléfono: "
            )

            estudiante.actualizar_info(
                correo,
                telefono
            )

            guardar_estudiantes()


        elif opcion == "5":

            print("Sesión finalizada.")
            break


        else:

            print("Opción no válida.")


cargar_equipos()
cargar_estudiantes()


print("\n==============================")
print("   SISTEMA DE INVENTARIO")
print("==============================")


usuario = iniciar_sesion()


if usuario != None:

    print("\nBienvenido", usuario.nombre if usuario.rol == "Estudiante" else usuario.cuenta)

    if usuario.rol == "Encargado":

        menu_encargado()

    elif usuario.rol == "Estudiante":

        menu_estudiante(usuario)

else:

    print("\nID o contraseña incorrectos.")