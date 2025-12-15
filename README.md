# Proyecto 1: FileSystem (Árboles y Trie)

Esto es un simulador de sistema de archivos en consola hecho para el curso de Estructura de Datos. Usa un **Árbol General** para las carpetas/archivos y un **Trie** para el autocompletado de búsqueda.

## Objetivo

Implementar las funciones básicas de manejo de archivos (crear, mover, renombrar, eliminar) y un sistema de búsqueda rápida por prefijo, reforzando el uso de árboles y estructuras auxiliares.

## Estructuras Clave

| Estructura | Función | Notas |
| :--- | :--- | :--- |
| **Árbol General** | Jerarquía de archivos | Se usa para crear la estructura de carpetas y archivos. |
| **Trie** | Autocompletado (search) | Permite buscar nombres de nodos por prefijo de forma rápida. |
| **JSON** | Persistencia | Guarda y carga todo el estado del árbol en un archivo local. |

**Lenguaje:** Python.

## Ejecución

1.  **Requisito:** Tener Python 3.x.
2.  **Iniciar:** Ejecutar `python filesystem_project.py`
3.  **Pruebas:** Ejecutar `python -m unittest test_filesystem.py`

## Guía de Comandos

| Comando | Función | Ejemplo |
| :--- | :--- | :--- |
| `mkdir <nombre>` | Crea una carpeta. | `mkdir Tareas` |
| `touch <nombre>` | Crea un archivo. | `touch nota.txt` |
| `ls [ruta]` | Lista el contenido de la ruta. | `ls` o `ls /Documentos` |
| `cd <ruta>` | Cambia de directorio. | `cd Tareas` o `cd ..` |
| `rename <ruta> <nuevo_nombre>`| Renombra un archivo/carpeta. | `rename /Docs borrador_final` |
| `mv <origen> <destino>` | Mueve un nodo a una nueva carpeta. | `mv viejo.txt /Papelera` |
| `rm <ruta>` | Elimina el nodo a la papelera temporal. | `rm archivo_basura.tmp` |
| `search <prefijo>` | Búsqueda rápida por prefijo. | `search proy` |
| `export preorden` | Muestra el recorrido del árbol en preorden. | `export preorden` |
| `exit` | Guarda el estado del sistema y sale. | `exit` |
