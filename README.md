# Sistema de Gestión de Inventarios en Python

## Descripción
Este proyecto implementa un Sistema de Gestión de Inventarios utilizando Programación Orientada a Objetos en Python.

El sistema permite:
- Añadir productos
- Mostrar productos
- Actualizar productos
- Eliminar productos
- Persistencia de datos mediante archivo de texto
- Manejo robusto de excepciones

## Conceptos Aplicados
- Programación Orientada a Objetos (POO)
- Encapsulamiento
- Persistencia de datos
- Manejo de archivos
- Manejo de excepciones (FileNotFoundError, PermissionError, ValueError)

## Estructura del Proyecto

SistemaInventario/
│
├── producto.py
├── inventario.py
├── main.py
├── inventario.txt
└── README.md

## Cómo ejecutar

1. Abrir el proyecto en PyCharm.
2. Ejecutar el archivo main.py.
3. Usar el menú interactivo en consola.

##  Manejo de Excepciones

El sistema controla:
- Archivo inexistente (se crea automáticamente).
- Errores de permisos.
- Entradas inválidas del usuario.
- Líneas corruptas en el archivo.
## Autor
Jefferson Galeas

Universidad Estatal Amazonica

Programacion Orientada a Objetos
