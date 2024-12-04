#ifndef AVL_H
#define AVL_H

#include <iostream>
#include <algorithm>

template<typename T>
class NodeALV {
public:
    T key;
    NodeALV* left;
    NodeALV* right;
    int height;

    NodeALV(T k) : key(k), left(nullptr), right(nullptr), height(1) {}
};

template<typename T>
class AvlTree {
public:
    NodeALV<T>* root;

    AvlTree() : root(nullptr) {}

    ~AvlTree() {
        destroyTree(root);
    }

    void destroyTree(NodeALV<T>* node) {
        if (node != nullptr) {
            destroyTree(node->left);
            destroyTree(node->right);
            delete node;
        }
    }

    int getHeight(NodeALV<T>* node) {
        return node ? node->height : 0;
    }

    int getBalanceFactor(NodeALV<T>* node) {
        return node ? getHeight(node->left) - getHeight(node->right) : 0;
    }

    NodeALV<T>* rotateRight(NodeALV<T>* y) {
        NodeALV<T>* x = y->left;
        NodeALV<T>* T2 = x->right;

        x->right = y;
        y->left = T2;

        y->height = std::max(getHeight(y->left), getHeight(y->right)) + 1;
        x->height = std::max(getHeight(x->left), getHeight(x->right)) + 1;

        return x;
    }

    NodeALV<T>* rotateLeft(NodeALV<T>* x) {
        NodeALV<T>* y = x->right;
        NodeALV<T>* T2 = y->left;

        y->left = x;
        x->right = T2;

        x->height = std::max(getHeight(x->left), getHeight(x->right)) + 1;
        y->height = std::max(getHeight(y->left), getHeight(y->right)) + 1;

        return y;
    }

    NodeALV<T>* insert(NodeALV<T>* node, T key) {
        if (!node) {
            return new NodeALV<T>(key);
        }

        if (key < node->key) {
            node->left = insert(node->left, key);
        } else if (key > node->key) {
            node->right = insert(node->right, key);
        } else {
            return node;
        }

        node->height = 1 + std::max(getHeight(node->left), getHeight(node->right));

        int balanceFactor = getBalanceFactor(node);

        if (balanceFactor > 1 && key < node->left->key) {
            return rotateRight(node);
        }

        if (balanceFactor > 1 && key > node->left->key) {
            node->left = rotateLeft(node->left);
            return rotateRight(node);
        }

        if (balanceFactor < -1 && key > node->right->key) {
            return rotateLeft(node);
        }

        if (balanceFactor < -1 && key < node->right->key) {
            node->right = rotateRight(node->right);
            return rotateLeft(node);
        }

        return node; // return node when balanceFactor == 0
    }

    NodeALV<T>* minValueNode(NodeALV<T>* node) {
        NodeALV<T>* current = node;
        while (current->left != nullptr)
            current = current->left;

        return current;
    }

    NodeALV<T>* deleteNode(NodeALV<T>* root, T key) {
        if (!root) return root;

        if (key < root->key) {
            root->left = deleteNode(root->left, key);
        } else if (key > root->key) {
            root->right = deleteNode(root->right, key);
        } else {
            if (!root->left || !root->right) {
                NodeALV<T>* temp = root->left ? root->left : root->right;

                if (!temp) {
                    temp = root;
                    root = nullptr;
                } else {
                    *root = *temp;
                }

                delete temp;
            } else {
                NodeALV<T>* temp = minValueNode(root->right);
                root->key = temp->key;
                root->right = deleteNode(root->right, temp->key);
            }
        }

        if (!root) return root;

        root->height = 1 + std::max(getHeight(root->left), getHeight(root->right));

        int balanceFactor = getBalanceFactor(root);

        if (balanceFactor > 1 && getBalanceFactor(root->left) >= 0) {
            return rotateRight(root);
        }

        if (balanceFactor > 1 && getBalanceFactor(root->left) < 0) {
            root->left = rotateLeft(root->left);
            return rotateRight(root);
        }

        if (balanceFactor < -1 && getBalanceFactor(root->right) <= 0) {
            return rotateLeft(root);
        }

        if (balanceFactor < -1 && getBalanceFactor(root->right) > 0) {
            root->right = rotateRight(root->right);
            return rotateLeft(root);
        }

        return root;
    }

    NodeALV<T>* search(NodeALV<T>* root, T key) {
        if (root == nullptr || root->key == key)
            return root;

        if (root->key < key)
            return search(root->right, key);

        return search(root->left, key);
    }

    void printInOrder(NodeALV<T>* root) {
        if (root != nullptr) {
            printInOrder(root->left);
            std::cout << root->key << " ";
            printInOrder(root->right);
        }
    }

    void insert(T key) {
        root = insert(root, key);
    }

    void deleteNode(T key) {
        root = deleteNode(root, key);
    }

    NodeALV<T>* search(T key) {
        return search(root, key);
    }

    void printInOrder() {
        std::cout << "In-order traversal: ";
        printInOrder(root);
        std::cout << std::endl;
    }
};

#endif // AVL_H