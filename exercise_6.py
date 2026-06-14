import cv2

# Cargando imagen
image = cv2.imread("images/dog.jpg")
if image is None:
    print("Error: could not load dog.jpg")
    exit()

# Convirtiendo a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicando threshold binario
threshold_value = 127
_, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

# Mostrando resultado
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray_image)
cv2.imshow("Binary threshold", binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardando resultado
cv2.imwrite("images/dog_binary.jpg", binary_image)