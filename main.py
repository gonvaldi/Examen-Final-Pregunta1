import tkinter as tk
import math
from geometria.geometria import Geometria

class Triangulo(Geometria):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        # Asumimos que es un triángulo isósceles
        lado = math.sqrt((self.base / 2) ** 2 + self.altura ** 2)
        return self.base + 2 * lado

def dibujar_triangulo(canvas, triangulo):
    # Coordenadas del triángulo
    x0, y0 = 300, 300  # Vértice superior
    x1, y1 = x0 - triangulo.base / 2, y0 - triangulo.altura  # Vértice inferior izquierdo
    x2, y2 = x0 + triangulo.base / 2, y0 - triangulo.altura  # Vértice inferior derecho

    # Dibujar el triángulo en el canvas
    canvas.create_polygon(x0, y0, x1, y1, x2, y2, outline="blue", fill="cyan")

    # Calcular el área y el perímetro
    area = triangulo.calcular_area()
    perimetro = triangulo.calcular_perimetro()

    # Mostrar área y perímetro en el canvas
    canvas.create_text(100, 50, text=f"Área: {area:.2f}", font=("Arial", 12), fill="black")
    canvas.create_text(100, 80, text=f"Perímetro: {perimetro:.2f}", font=("Arial", 12), fill="black")

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Dibujo de Triángulo")

    # Crear un lienzo
    canvas = tk.Canvas(root, width=555, height=380)
    canvas.pack()

    # Crear un objeto Triangulo
    triangulo = Triangulo(base=191, altura=144)
    
    # Dibujar el triángulo y mostrar el área y perímetro
    dibujar_triangulo(canvas, triangulo)

    # Iniciar el bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()
