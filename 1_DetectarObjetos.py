import pymongo
import os
import imageai
from imageai.Detection import ObjectDetection

"""
Este script detecta objetos en imágenes utilizando el modelo YOLOv3 y actualiza una base de datos MongoDB con los resultados.
"""

rutaModelosIA = "/mnt/local/datos/Desarrollo/ModelosIA"

"""
Lista de extensiones de archivo permitidas para el procesamiento.
"""
extensionesValidas = ["jpg", "jpeg", "png"]

"""
Lee los documentos de la base de datos MongoDB.
"""
def leeBaseDatos():
    client = pymongo.MongoClient("localhost", 27017)
    db = client["inventario"]
    coleccion = db["archivos"]    
    return coleccion.find()

"""
Actualiza un documento en la base de datos MongoDB con los objetos detectados.
"""
def actualizarBaseDatos(id, objetosDetectados, contador):
    try:
        client = pymongo.MongoClient("localhost", 27017)
        db = client["inventario"]
        coleccion = db["archivos"]
        coleccion.update_one({"_id": id}, {"$set": {f"objeto{contador}": objetosDetectados}})
    except Exception as e:
        print("Error al actualizar la base de datos: " + str(e))

"""
Detecta objetos en una imagen utilizando el modelo YOLOv3.
"""
def detectarObjetos(imagen):
    salida = []
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(rutaModelosIA , "yolov3.pt"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=imagen, minimum_percentage_probability=30)
    numeroObjetos = len(detections)
    contador = 0
    objeto = []
    for eachObject in detections:        
        contador += 1    
        nombre = eachObject["name"]
        probabilidad = eachObject["percentage_probability"]
        coordenadas = eachObject["box_points"]
        x1, y1, x2, y2 = coordenadas
        objeto = [contador, nombre, probabilidad, coordenadas]        
        salida.append(objeto)
        objeto = []              
    return salida

"""
Función principal que recorre los documentos de la base de datos y procesa las imágenes para detectar objetos.
"""
if __name__ == '__main__':
    for documento in leeBaseDatos():
        try:
            os.system("clear")
            if documento["extensioArchivo"] in extensionesValidas:            
                objetosDetectados = detectarObjetos(documento["ruta_archivo"])
                if len(objetosDetectados) > 0:
                    contador = 0
                    print("Se detectaron objetos en el archivo: " + documento["nombre_archivo"])           
                    for objeto in objetosDetectados:
                        contador += 1
                        actualizarBaseDatos(documento["_id"], objeto, contador)
                        print(objeto)
        except Exception as e:
            print("Error al procesar el archivo: " + documento["nombre_archivo"] + " - " + str(e))
            pass
