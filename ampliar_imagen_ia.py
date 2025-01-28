from waifu2x import run


"""
Este script utiliza la biblioteca waifu2x para ampliar una imagen.
"""

output_img_path = "foreground_actual.png"
"""
Ruta de la imagen de entrada.
"""
input_img_path = "foreground.png"

"""
Ruta de la imagen de salida.
"""
output_img_path = "foreground_actual.png"

"""
Ejecuta el proceso de ampliación de imagen.
"""
run(input_img_path, output_img_path)
