import os

"""
Este script recorre los directorios y archivos en una ruta específica e imprime las rutas completas de los archivos.
"""


"""
Ruta base para recorrer los directorios y archivos.
"""
ruta = "/mnt/local/datos"

"""
Recorre los directorios y archivos en la ruta especificada e imprime las rutas completas de los archivos.
"""
for directorio, subdirectorio, archivos in os.walk(ruta):
    for archivo in archivos:
        ruta_archivo = os.path.join(directorio, archivo)
        print(ruta_archivo)
