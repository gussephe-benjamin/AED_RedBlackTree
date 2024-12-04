# Establecer la versión mínima de CMake
cmake_minimum_required(VERSION 3.10)

# Definir el nombre del proyecto
project(MiProyecto)

# Definir el estándar C++ que se usará (por ejemplo, C++17)
set(CMAKE_CXX_STANDARD 17)

# Especificar los archivos fuente
set(SOURCES
    main.cpp
    AvlTree.h
    RedBlackTree.h
)

# Crear el ejecutable
add_executable(mi_programa ${SOURCES})
