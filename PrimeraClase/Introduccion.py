# Importamos la libreria opencv
import cv2

# Utilizando el comando "imread" de opencv, leeremos la imagen1.jpg y la guardaremos en la variable img
img = cv2.imread("Imagenes/imagen1.jpg")


# Utilizando el comando "imshow" de opencv, mostraremos la imagen en una ventana llamada ventana1
cv2.imshow("ventana1", img)

# Controla el tiempo de muestreo de la señal de entreada por teclado
cv2.waitKey()


# Destruye o cierra las ventanas creadas por Opencv
cv2.destroyAllWindows()

#
cv2.imwrite("PrimeraClase/imagenGuardada1.jpg", img)