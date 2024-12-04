import tkinter as tk
from red_black_tree import RedBlackTree, Node
from tkinter import messagebox
from math import atan2, degrees, pi, cos, sin 

class TreeVisualizer:
    def __init__(self, tree):
        self.tree = tree
        self.window = tk.Tk()
        self.window.title("Red-Black Tree Visualizer")

        # Definir el tamaño de la ventana para Full HD
        self.window.geometry("1920x1080")
        self.window.resizable(True, True)  # Hacer la ventana redimensionable

        # Canvas para dibujar el árbol con resolución Full HD (1920x1080)
        self.canvas_width = 1920
        self.canvas_height = 900  # Un poco menos para los botones
        self.canvas = tk.Canvas(self.window, width=self.canvas_width, height=self.canvas_height, bg="#F4F4F4")
        self.canvas.pack()

        # Frame para los botones (en la parte inferior de la ventana)
        self.frame = tk.Frame(self.window)
        self.frame.pack(side=tk.BOTTOM, pady=20)

        # Campo de entrada para el valor del nodo
        self.entry_label = tk.Label(self.frame, text="Valor del Nodo:")
        self.entry_label.pack(side=tk.LEFT, padx=10)

        self.node_entry = tk.Entry(self.frame)
        self.node_entry.pack(side=tk.LEFT, padx=10)

        # Botón para insertar el nodo
        self.insert_button = tk.Button(self.frame, text="Insertar Nodo", command=self.insert_and_update)
        self.insert_button.pack(side=tk.LEFT, padx=10)

        # Botón para eliminar el nodo
        self.delete_button = tk.Button(self.frame, text="Eliminar Nodo", command=self.delete_and_update)
        self.delete_button.pack(side=tk.LEFT, padx=10)

    def insert_and_update(self):
        try:
            value = int(self.node_entry.get())
            self.tree.insert(value)  # Insertar en el árbol
            self.node_entry.delete(0, tk.END)  # Limpiar el campo de entrada
            self.update_visualization()  # Actualizar la visualización
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")
    
    def delete_and_update(self):
        try:
            value = int(self.node_entry.get())
            self.tree.delete(value)  # Eliminar el nodo
            self.node_entry.delete(0, tk.END)  # Limpiar el campo de entrada
            self.update_visualization()  # Actualizar la visualización
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")

    def get_level_widths(self, node, level=0, widths=None):
        """Calcula el número de nodos en cada nivel del árbol."""
        if node is None:
            return widths
        
        if widths is None:
            widths = []  # Asegurarse de que widths se inicialice correctamente
        
        if len(widths) <= level:
            widths.append(0)
        
        widths[level] += 1
        self.get_level_widths(node.left, level + 1, widths)
        self.get_level_widths(node.right, level + 1, widths)
        
        return widths

    def draw_tree(self, node, x, y, dx):
        """Dibuja el árbol de manera recursiva."""
        if node == self.tree.TNULL:  # Verificamos si es el nodo nulo
            return  # No dibujamos el nodo nulo
        
        # Dibuja las flechas de conexión con los nodos izquierdo y derecho primero (por debajo de los nodos)
            # Dibuja la línea con el nodo izquierdo si no es nulo
        if node.left != self.tree.TNULL:
            self.draw_arrow(x, y, x - dx, y + 60)  # Flecha izquierda
            self.draw_tree(node.left, x - dx, y + 60, dx // 2)

        # Dibuja la línea con el nodo derecho si no es nulo
        if node.right != self.tree.TNULL:
            self.draw_arrow(x, y, x + dx, y + 60)  # Flecha derecha
            self.draw_tree(node.right, x + dx, y + 60, dx // 2)

        # Dibuja el nodo actual después de las flechas
        color = 'black' if node.color == 'black' else '#BA0000'  # Usamos un rojo más suave (Tomato)
        node_size = 25  # Aumentamos el tamaño de los nodos
        self.canvas.create_oval(x - node_size, y - node_size, x + node_size, y + node_size, 
                                fill=color, outline='black', width=2)

        # Cambia el color del texto según el color del nodo
        text_color = "white"  # Blanco si el nodo es rojo
        self.canvas.create_text(x, y, text=str(node.data), fill=text_color, font=('Arial', 14, 'bold'))

    def draw_arrow(self, x1, y1, x2, y2):
        # Calculamos el ángulo de la flecha
        angle = atan2(y2 - y1, x2 - x1)
        arrow_length = 20  # Longitud de la flecha
        arrow_angle = pi / 8  # Ángulo de las puntas de la flecha

        # Coordenadas de la flecha
        x3 = x2 - arrow_length * cos(angle - arrow_angle)
        y3 = y2 - arrow_length * sin(angle - arrow_angle)
        x4 = x2 - arrow_length * cos(angle + arrow_angle)
        y4 = y2 - arrow_length * sin(angle + arrow_angle)

        # Dibuja la flecha
        self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, width=2, fill="black")
        self.canvas.create_line(x2, y2, x3, y3, width=2, fill="black")
        self.canvas.create_line(x2, y2, x4, y4, width=2, fill="black")

    def get_angle(self, x1, y1, x2, y2):
        """Devuelve el ángulo entre dos puntos (x1, y1) y (x2, y2)."""
        import math
        return math.atan2(y2 - y1, x2 - x1)

    def update_visualization(self):
        """Actualiza la visualización del árbol en el canvas."""
        self.canvas.delete("all")  # Limpiar la pantalla
        self.draw_tree(self.tree.root, self.canvas_width // 2, 50, self.canvas_width // 4)  # Usamos self.tree.root aquí

    def run(self):
        """Ejecuta el bucle principal de la ventana."""
        self.window.mainloop()
