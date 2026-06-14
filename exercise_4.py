import cv2
import numpy as np

# Cargando imagen
image = cv2.imread("images/cat.jpg")
if image is None:
    print("Error: could not load cat.jpg")
    exit()

# Separando canales
b_channel, g_channel, r_channel = cv2.split(image)
zeros = np.zeros_like(b_channel)

show_b = True
show_g = True
show_r = True

print("Controles:")
print("  R - alternar canal rojo")
print("  G - alternar canal verde")
print("  B - alternar canal azul")
print("  Q - salir")

while True:
    b = b_channel if show_b else zeros
    g = g_channel if show_g else zeros
    r = r_channel if show_r else zeros

    display_image = cv2.merge([b, g, r])
    cv2.imshow("Channel Viewer", display_image)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('r') or key == ord('R'):
        show_r = not show_r
    elif key == ord('g') or key == ord('G'):
        show_g = not show_g
    elif key == ord('b') or key == ord('B'):
        show_b = not show_b
    elif key == ord('q') or key == ord('Q'):
        break

cv2.destroyAllWindows()