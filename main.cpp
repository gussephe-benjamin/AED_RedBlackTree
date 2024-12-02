#include <iostream>
#include <chrono>
#include <cstdlib>
#include <vector>
#include "AVL.h"
#include "Red-Black-Tree.h"

using namespace std;
using namespace std::chrono;


const vector<int> SIZES = {10000, 100000, 1000000, 10000000};


void benchmarkAVL(const vector<int>& valuesToInsert, const vector<int>& valuesToDelete) {
    AvlTree<int> avl;

    auto start = high_resolution_clock::now();
    for (int value : valuesToInsert) {
        avl.insert(value);
    }
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(end - start);
    cout << "AVL insert duration (" << valuesToInsert.size() << " elements): " << duration.count() << " ms" << endl;


    start = high_resolution_clock::now();
    for (int value : valuesToInsert) {
        avl.search(value);
    }
    end = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(end - start);
    cout << "AVL search duration (" << valuesToInsert.size() << " elements): " << duration.count() << " ms" << endl;


    start = high_resolution_clock::now();
    for (int value : valuesToDelete) {
        avl.deleteNode(value);
    }
    end = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(end - start);
    cout << "AVL delete duration (" << valuesToDelete.size() << " elements): " << duration.count() << " ms" << endl;
}

void benchmarkRBT(const vector<int>& valuesToInsert, const vector<int>& valuesToDelete) {
    RedBlackTree<int> rbt;

    auto start = high_resolution_clock::now();
    for (int value : valuesToInsert) {
        rbt.insert(value);
    }
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(end - start);
    cout << "RBT insert duration (" << valuesToInsert.size() << " elements): " << duration.count() << " ms" << endl;


    start = high_resolution_clock::now();
    for (int value : valuesToInsert) {
        rbt.search(value);
    }
    end = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(end - start);
    cout << "RBT search duration (" << valuesToInsert.size() << " elements): " << duration.count() << " ms" << endl;

   start = high_resolution_clock::now();
    for (int value : valuesToDelete) {
        rbt.remove(value);
    }
    end = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(end - start);
    cout << "RBT delete duration (" << valuesToDelete.size() << " elements): " << duration.count() << " ms" << endl;
}

int main() {
    srand(time(0));

    for (int size : SIZES) {
        vector<int> valuesToInsert;
        vector<int> valuesToDelete;


        for (int i = 0; i < size; ++i) {
            valuesToInsert.push_back(i);
        }


        for (int i = 0; i < size/3; ++i) {
            valuesToDelete.push_back(i);
        }

        cout << "Benchmarking with " << size << " elements..." << endl;
        cout << "--------------------------------------" << endl;

        cout << "Benchmarking AVL Tree..." << endl;
        benchmarkAVL(valuesToInsert, valuesToDelete);

        cout << "Benchmarking Red-Black Tree..." << endl;
        benchmarkRBT(valuesToInsert, valuesToDelete);

        cout << "--------------------------------------" << endl;
        cout << endl;
    }

    return 0;
}