import tkinter as tk

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

def dibujar_triangulo(canvas, triangulo):
    # Coordenadas del triángulo
    x0, y0 = 300, 300  # Vértice superior
    x1, y1 = x0 - triangulo.base / 2, y0 - triangulo.altura  # Vértice inferior izquierdo
    x2, y2 = x0 + triangulo.base / 2, y0 - triangulo.altura  # Vértice inferior derecho

    # Dibujar el triángulo en el canvas
    canvas.create_polygon(x0, y0, x1, y1, x2, y2, outline="green", fill="lightgreen")

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Dibujo de Triángulo")

    # Crear un lienzo
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()

    # Crear un objeto Triangulo
    triangulo = Triangulo(base=200, altura=150)
    
    # Dibujar el triángulo
    dibujar_triangulo(canvas, triangulo)

    # Iniciar el bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()
