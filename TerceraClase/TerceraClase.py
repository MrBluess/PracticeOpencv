import cv2

# Jugando con waitKey()

img = cv2.imread("Imagenes/imagen1.jpg")
img2 = cv2.imread("Imagenes/imagen1.jpg", 0)

while True:
    cv2.imshow("color", img)
    cv2.imshow("grises", img2)

    key = cv2.waitKey()

    if key == ord("g"):
        cv2.imwrite("TerceraClase/imagenGuardada.png", img2)

    elif key == ord("c"):
        cv2.imwrite("TerceraClase/imagenGuardada.png", img)

    else:
        break

cv2.destroyAllWindows()