import hashlib

"""
Este script genera un hash SHA-512 a partir del contenido de un archivo.
"""

def generarHash(archivo):
    """
    Genera un hash SHA-512 a partir del contenido de un archivo.
    """
    with open(archivo, 'rb') as f:
        data = f.read()
    return hashlib.sha512(data).hexdigest()
archivo = './python/imageai_1/image.jpg'
archivo = './python/imageai_1/image.jpg'

"""
Imprime el hash generado para el archivo especificado.
"""
print(generarHash(archivo))
