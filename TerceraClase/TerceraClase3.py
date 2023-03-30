import cv2

# Carga una imagen llamada "imagen1.jpg" en la variable img
img = cv2.imread("Imagenes/imagen1.jpg")

# Carga una imagen llamada "imagen1.jpg" en la variable img2 y conviértela a escala de grises
img2 = cv2.imread("Imagenes/imagen1.jpg", 0)

# Crea una ventana llamada "Ventana" con la propiedad de tamaño normal
cv2.namedWindow("Ventana", cv2.WINDOW_NORMAL)

# Establece la propiedad de la ventana "Ventana" en pantalla completa
cv2.setWindowProperty("Ventana", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Bucle infinito para mostrar las imágenes en la ventana "Ventana"
while True:
    # Espera a que se pulse una tecla
    key = cv2.waitKey()

    # Si se pulsa la tecla "4", muestra la imagen original en la ventana "Ventana"
    if key == ord("4"):
        cv2.imshow("Ventana", img)
    
    # Si se pulsa la tecla "6", muestra la imagen en escala de grises en la ventana "Ventana"
    elif key == ord("6"):
        cv2.imshow("Ventana", img2)
    
    # Si se pulsa cualquier otra tecla, sale del bucle
    else:
        break

# Destruye la ventana "Ventana" y libera los recursos
cv2.destroyAllWindows()
