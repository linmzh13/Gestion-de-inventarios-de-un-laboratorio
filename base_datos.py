import sqlite3

from equipo import Equipo
from estudiante import Estudiante
from encargado import Encargado


# ==============================
# CONECTAR A LA BASE DE DATOS
# ==============================

def conectar():

    return sqlite3.connect("inventario.db")


# ==============================
# CREAR BASE DE DATOS
# ==============================

def crear_base_datos():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipos (
            id TEXT PRIMARY KEY,
            nombre TEXT,
            cantidad INTEGER,
            estado TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id TEXT PRIMARY KEY,
            nombre TEXT,
            password TEXT,
            correo TEXT,
            rol TEXT,
            telefono TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS encargados (
            id TEXT PRIMARY KEY,
            cuenta TEXT,
            password TEXT,
            correo TEXT,
            rol TEXT
        )
    """)

    conexion.commit()
    conexion.close()


# ==============================
# GUARDAR EQUIPO
# ==============================

def guardar_equipo(equipo):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO equipos
        (id, nombre, cantidad, estado)
        VALUES (?, ?, ?, ?)
    """, (
        equipo.id,
        equipo.nombre,
        equipo.cantidad,
        equipo.estado
    ))

    conexion.commit()
    conexion.close()


# ==============================
# ACTUALIZAR EQUIPO
# ==============================

def actualizar_equipo(equipo):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE equipos
        SET nombre = ?,
            cantidad = ?,
            estado = ?
        WHERE id = ?
    """, (
        equipo.nombre,
        equipo.cantidad,
        equipo.estado,
        equipo.id
    ))

    conexion.commit()
    conexion.close()


# ==============================
# CARGAR EQUIPOS
# ==============================

def cargar_equipos():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, cantidad, estado
        FROM equipos
    """)

    datos = cursor.fetchall()

    conexion.close()

    equipos = []

    for dato in datos:

        equipo = Equipo(
            dato[0],
            dato[1],
            dato[2],
            dato[3]
        )

        equipos.append(equipo)

    return equipos


# ==============================
# GUARDAR ESTUDIANTE
# ==============================

def guardar_estudiante(estudiante):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO estudiantes
        (id, nombre, password, correo, rol, telefono)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        estudiante.id,
        estudiante.nombre,
        estudiante.password,
        estudiante.correo,
        estudiante.rol,
        estudiante.telefono
    ))

    conexion.commit()
    conexion.close()


# ==============================
# ACTUALIZAR ESTUDIANTE
# ==============================

def actualizar_estudiante(estudiante):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE estudiantes
        SET nombre = ?,
            password = ?,
            correo = ?,
            rol = ?,
            telefono = ?
        WHERE id = ?
    """, (
        estudiante.nombre,
        estudiante.password,
        estudiante.correo,
        estudiante.rol,
        estudiante.telefono,
        estudiante.id
    ))

    conexion.commit()
    conexion.close()


# ==============================
# CARGAR ESTUDIANTES
# ==============================

def cargar_estudiantes():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, password, correo, rol, telefono
        FROM estudiantes
    """)

    datos = cursor.fetchall()

    conexion.close()

    estudiantes = []

    for dato in datos:

        estudiante = Estudiante(
            dato[0],
            dato[1],
            dato[2],
            dato[3],
            dato[4],
            dato[5]
        )

        estudiantes.append(estudiante)

    return estudiantes


# ==============================
# GUARDAR ENCARGADO
# ==============================

def guardar_encargado(encargado):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO encargados
        (id, cuenta, password, correo, rol)
        VALUES (?, ?, ?, ?, ?)
    """, (
        encargado.id,
        encargado.cuenta,
        encargado.password,
        encargado.correo,
        encargado.rol
    ))

    conexion.commit()
    conexion.close()


# ==============================
# CARGAR ENCARGADOS
# ==============================

def cargar_encargados():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, cuenta, password, correo, rol
        FROM encargados
    """)

    datos = cursor.fetchall()

    conexion.close()

    encargados = []

    for dato in datos:

        encargado = Encargado(
            dato[0],
            dato[1],
            dato[2],
            dato[3],
            dato[4]
        )

        encargados.append(encargado)

    return encargados