class Estudiante:

    def __init__(self, id, nombre, password, correo, rol, telefono):
        self.id = id
        self.nombre = nombre
        self.password = password
        self.correo = correo
        self.rol = rol
        self.telefono = telefono

    def consultar_inventario(self, equipos):
        print("\n--- INVENTARIO ---")

        for equipo in equipos:
            equipo.consultar_inventario()

    def solicitar_prestamo(self, equipo):
        equipo.solicitar_prestamo()

    def actualizar_info(self, correo, telefono):
        self.correo = correo
        self.telefono = telefono
        print("Información actualizada correctamente.")

    def consultar_equipo(self, equipo):
        equipo.consultar_estado()