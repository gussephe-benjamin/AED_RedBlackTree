from red_black_tree import RedBlackTree
from tree_visualization import TreeVisualizer

def main():
    # Inicializamos el árbol Red-Black
    tree = RedBlackTree()

    # Creamos el visualizador con la raíz del árbol
    visualizer = TreeVisualizer(tree)

    # Mostrar la ventana de visualización
    visualizer.run()

if __name__ == "__main__":
    main()
