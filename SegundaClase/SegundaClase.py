import cv2

# Mandamos llamar la imagen en escala de grises, y se guarda en la variable img
img = cv2.imread("Imagenes/imagen1.jpg", cv2.IMREAD_GRAYSCALE) # Tambien se puede trazar por un 0 zero

cv2.imshow("imagen en escala de grises", img)

# Controla el tiempo de muestreo de la señal de entreada por teclado
cv2.waitKey()

# Destruye o cierra las ventanas creadas por Opencv
cv2.destroyAllWindows()
