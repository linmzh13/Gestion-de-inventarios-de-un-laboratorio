class Encargado:

    def __init__(self, id, cuenta, password, correo, rol):
        self.id = id
        self.cuenta = cuenta
        self.password = password
        self.correo = correo
        self.rol = rol

    def registrar_persona(self, estudiantes, estudiante):
        estudiantes.append(estudiante)
        print("Estudiante registrado correctamente.")

    def consultar_inventario(self, equipos):
        print("\n--- INVENTARIO ---")

        for equipo in equipos:
            equipo.consultar_inventario()

    def registrar_equipo(self, equipos, equipo):
        equipos.append(equipo)
        print("Equipo registrado correctamente.")

    def consultar_estudiante(self, estudiantes):
        print("\n--- ESTUDIANTES ---")

        for estudiante in estudiantes:
            print("ID:", estudiante.id)
            print("Nombre:", estudiante.nombre)
            print("Correo:", estudiante.correo)
            print("Teléfono:", estudiante.telefono)
            print()