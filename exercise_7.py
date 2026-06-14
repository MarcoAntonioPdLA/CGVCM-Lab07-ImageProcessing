import cv2
import numpy as np

# Canvas
canvas = np.ones((500, 700, 3), dtype=np.uint8) * 255
history = []

# Estado
drawing = False
start_point = (0, 0)
shape = "line"

print("Controles:")
print("  L - modo linea")
print("  C - modo circulo")
print("  R - modo rectangulo")
print("  U - deshacer ultimo trazo")
print("  S - guardar dibujo")
print("  Q - salir")

def mouse_callback(event, x, y, flags, param):
    global drawing, start_point, canvas

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
        history.append(canvas.copy())

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)

        if shape == "line":
            cv2.line(canvas, start_point, end_point, (0, 0, 0), 2)
        elif shape == "circle":
            radius = int(((end_point[0]-start_point[0])**2 + (end_point[1]-start_point[1])**2) ** 0.5)
            cv2.circle(canvas, start_point, radius, (0, 0, 0), 2)
        elif shape == "rectangle":
            cv2.rectangle(canvas, start_point, end_point, (0, 0, 0), 2)

cv2.namedWindow("Drawing App")
cv2.setMouseCallback("Drawing App", mouse_callback)

# Ejecución del programa
while True:
    cv2.imshow("Drawing App", canvas)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('l') or key == ord('L'):
        shape = "line"
        print("Modo: linea")
    elif key == ord('c') or key == ord('C'):
        shape = "circle"
        print("Modo: circulo")
    elif key == ord('r') or key == ord('R'):
        shape = "rectangle"
        print("Modo: rectangulo")
    elif key == ord('u') or key == ord('U'):
        if history:
            canvas = history.pop()
            print("Undo")
    elif key == ord('s') or key == ord('S'):
        cv2.imwrite("images/drawing.png", canvas)
        print("Guardado como drawing.png")
    elif key == ord('q') or key == ord('Q'):
        break

cv2.destroyAllWindows()