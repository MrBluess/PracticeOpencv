import cv2   # Importamos la biblioteca OpenCV
import numpy as np   # Importamos la biblioteca NumPy

# Creamos una matriz tridimensional de 100x100 píxeles con 3 canales de color (RGB) con valores de píxel inicializados en cero
ImagenObscura = np.zeros((100, 100, 3), np.uint8)

# Seleccionamos el valor de píxel en la posición [97,97] de la matriz ImagenObscura
pixel = ImagenObscura[97, 97]

# Imprimimos el valor del píxel seleccionado
print(pixel)
