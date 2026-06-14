import cv2

# Cargando imágenes redimensionadas
image_1 = cv2.imread("images/cat_resized.jpg")
image_2 = cv2.imread("images/dog_resized.jpg")
image_3 = cv2.imread("images/kid_resized.jpg")
for name, image in zip(["cat_resized.jpg", "dog_resized.jpg", "kid_resized.jpg"], [image_1, image_2, image_3]):
    if image is None:
        print(f"Error: could not load {name}")
        exit()

# Extrayendo los canales
red_channel = image_1[:, :, 2]
green_channel = image_2[:, :, 1]
blue_channel = image_3[:, :, 0]

# Creando la nueva imagen
combined_image = cv2.merge([blue_channel, green_channel, red_channel])

# Mostrando resultado
cv2.imshow("Combined channels", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardando imagen para el siguiente ejercicio
cv2.imwrite("images/combined.jpg", combined_image)