import tkinter as tk
from tkinter import messagebox

class RedBlackTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.color = "red"  # Nuevo nodo es rojo
            self.left = None
            self.right = None
            self.parent = None
            self.x_offset = 0
            self.y_offset = 0

    def __init__(self):
        self.TNULL = self.Node(0)
        self.TNULL.color = "black"
        self.root = self.TNULL

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.TNULL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.TNULL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k.parent.color == "red":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.rotate_right(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rotate_right(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.rotate_left(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "black"

    def insert(self, key):
        node = self.Node(key)
        node.parent = self.TNULL
        node.left = self.TNULL
        node.right = self.TNULL

        y = self.TNULL
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == self.TNULL:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        self.fix_insert(node)

    def get_tree_structure(self):
        def traverse(node, x, y, level):
            if node == self.TNULL:
                return []
            node.x_offset = x
            node.y_offset = y
            nodes = [(node, x, y, level)]
            nodes += traverse(node.left, x - 80, y + 60, level + 1)
            nodes += traverse(node.right, x + 80, y + 60, level + 1)
            return nodes

        return traverse(self.root, 500, 40, 0)

class RedBlackTreeGUI(tk.Tk):
    def __init__(self, tree):
        super().__init__()
        self.tree = tree
        self.title("Red-Black Tree Visualization")
        self.geometry("1000x800")
        
        self.canvas = tk.Canvas(self, width=1000, height=800, bg="white")
        self.canvas.pack()

        self.node_label = tk.Label(self, text="Introduce el valor del nodo:")
        self.node_label.pack(pady=10)

        self.node_entry = tk.Entry(self)
        self.node_entry.pack(pady=10)

        self.insert_button = tk.Button(self, text="Insertar Nodo", command=self.insert_node)
        self.insert_button.pack(pady=10)

    def insert_node(self):
        try:
            value = int(self.node_entry.get())
            self.tree.insert(value)
            self.node_entry.delete(0, tk.END)
            messagebox.showinfo("Éxito", f"Valor {value} insertado.")
            self.draw_tree()  # Dibujar el árbol actualizado
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico.")

    def draw_tree(self):
        # Limpiar el lienzo antes de dibujar
        self.canvas.delete("all")
        
        # Obtener la estructura del árbol (nodos y posiciones)
        nodes = self.tree.get_tree_structure()

        # Dibujar los nodos y sus conexiones
        for node, x, y, level in nodes:
            color = "red" if node.color == "red" else "black"
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=color, outline="black")
            self.canvas.create_text(x, y, text=str(node.data), fill="white")
            
            if node.parent != self.tree.TNULL:
                parent_x = node.parent.x_offset
                parent_y = node.parent.y_offset
                self.canvas.create_line(x, y, parent_x, parent_y, fill="black")

            node.x_offset = x
            node.y_offset = y

if __name__ == "__main__":
    tree = RedBlackTree()
    app = RedBlackTreeGUI(tree)
    app.mainloop()
