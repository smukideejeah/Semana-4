#Nombre del programa: Programacion II 
#Número de grupo de Trabajo: Grupo 1
#Nombre del Programador: Elmer / Rafael / Joseph / Elvis 
#Fecha de elaboración del programa: 07/10/2024
#Versión del PYTHON: 3.12.3
#Nombre del IDE donde se trabajó el código: Visual Studio Code


def opera2(operador, a, b):
    return {
        'suma': lambda: a + b,
        'resta': lambda: a - b,
        'multiplica': lambda: a * b,
        'divide': lambda: a / b
    }.get(operador, lambda: None)