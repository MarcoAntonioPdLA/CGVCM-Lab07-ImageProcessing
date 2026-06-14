import cv2

# Cargando la imagen combinada
combined_image = cv2.imread("images/combined.jpg")
if combined_image is None:
    print("Error: could not load combined.jpg")
    exit()

# Convirtiendo a negativo
negative_image = 255 - combined_image

cv2.imshow("Negative", negative_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("images/combined_negative.jpg", negative_image)

# Convirtiendo a escala de grises
gray_image = cv2.imread("images/combined.jpg", cv2.IMREAD_GRAYSCALE)

# Mostrando resultado
cv2.imshow("Grayscale", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardando imagen
cv2.imwrite("images/combined_gray.jpg", gray_image)