import cv2

# Cargando imagen
image = cv2.imread("images/kid.jpg")
if image is None:
    print("Error: could not load kid.jpg")
    exit()

# Dibujando el círculo sobre la cara
center = (375, 185)
radius = 60
cv2.circle(image, center, radius, (0, 255, 0), 3)

# Agregando texto
text = "Persona"
text_position = (center[0] - radius, center[1] + radius + 30)
cv2.putText(image, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Mostrando resultado
cv2.imshow("Image with annotations", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardando imagen
cv2.imwrite("images/kid_annotated.jpg", image)