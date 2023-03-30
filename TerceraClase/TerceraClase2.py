import cv2

# Cargar la imagen y almacenarla en la variable 'img'
img = cv2.imread("Imagenes/imagen1.jpg")

# Cargar la misma imagen pero en escala de grises y almacenarla en la variable 'img2'
img2 = cv2.imread("Imagenes/imagen1.jpg", 0)

# Mostrar la imagen en una ventana llamada 'Ventana'
cv2.imshow("Ventana", img)

# Esperar hasta que se presione alguna tecla
while True:
    key = cv2.waitKey()

    # Si se presiona la tecla '4', mostrar la imagen original 'img'
    if key == ord("4"):
        cv2.imshow("Ventana", img)
    # Si se presiona la tecla '6', mostrar la imagen en escala de grises 'img2'
    elif key == ord("6"):
        cv2.imshow("Ventana", img2)
    # Si se presiona cualquier otra tecla, salir del bucle
    else:
        break

# Destruir todas las ventanas creadas durante el programa
cv2.destroyAllWindows()
