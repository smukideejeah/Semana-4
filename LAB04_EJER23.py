#Programa: LAB04_EJER23
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 7/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
tabla_switch = {
        '0': '000' ,
        '1': '001' ,
        '2': '010' ,
        '3': '011' ,
        '4': '100' ,
        '5': '101' ,
        '6': '110' ,
        '7': '111' ,   
    }
def usa_switch(decimal):
    return tabla_switch.get(decimal, "NA")