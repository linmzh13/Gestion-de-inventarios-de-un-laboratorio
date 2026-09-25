# Sistema de Inventario de Laboratorio de Electrónica
## Equipo de trabajo: Lineth Márquez y Jair Garzón.


## Descripción
Este proyecto consiste en un sistema básico para llevar el control de los equipos de un laboratorio de electrónica.
El sistema permite que el encargado registre equipos y estudiantes, consulte el inventario y revise el estado de los equipos. Los estudiantes pueden consultar los equipos disponibles, solicitar préstamos y actualizar algunos de sus datos.
El programa fue realizado en Python aplicando conceptos de Programación Orientada a Objetos (POO).

## Funciones

### Encargado

Iniciar sesión.
Consultar el inventario.
Registrar equipos.
Registrar estudiantes.
Consultar estudiantes.
Consultar el estado de los equipos.


### Estudiante

Iniciar sesión.
Consultar el inventario.
Solicitar préstamos.
Consultar el estado de un equipo.
Actualizar correo y teléfono.


## Clases

El proyecto cuenta con tres clases principales:
Encargado: permite administrar equipos y estudiantes.
Estudiante: permite consultar equipos, solicitar préstamos y actualizar información.
Equipo: contiene los datos de cada equipo y controla su disponibilidad.

## Archivos

main.py — Programa principal.

encargado.py — Clase Encargado.

estudiante.py — Clase Estudiante.

equipo.py — Clase Equipo.

equipos.txt — Información de los equipos.

estudiantes.txt — Información de los estudiantes.


## Formato de los equipos

Los equipos se guardan en equipos.txt utilizando el siguiente formato:
ID;Nombre;Cantidad;Estado

Ejemplo:
E001;Multimetro;4;Disponible
E002;Osciloscopio;2;Disponible
E003;Protoboard;10;Disponible
E004;Fuente DC;3;Disponible

## Préstamo de equipos

Cuando un estudiante solicita un equipo, el sistema verifica que exista y que esté disponible.
Si hay unidades disponibles, la cantidad se reduce en uno. Cuando la cantidad llega a cero, el equipo pasa a tener el estado No disponible.

## Ejecución

Para ejecutar el proyecto se necesita tener Python instalado.
El programa se inicia ejecutando el archivo:
main.py
Los archivos .py y .txt deben estar dentro de la misma carpeta del proyecto.


## Diagramas de UML:

### Diagrama de casos de uso:

<img width="1171" height="972" alt="Diagrama de caso de uso" src="https://github.com/user-attachments/assets/9a45645b-8adf-47b6-8a1c-5750a9b263f0" />

### Diagrama de clases: 

<img width="1301" height="1297" alt="Diagrama en blanco" src="https://github.com/user-attachments/assets/b9f4f5ce-aa89-4eba-aed8-0fc2480a8d6d" />

### Diagrama de secuencia:

<img width="1536" height="1024" alt="Secuencia" src="https://github.com/user-attachments/assets/6a9a4c90-3787-4ddc-8f5c-c79e486eaa9a" />


