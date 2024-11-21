from clases import *
matriz= []

#Input de matriz 
def ingresarADN():
 for i in range(6):
    while True:
        fila = input(f"Ingrese la fila {i + 1} de la matriz (6 caracteres)> ").strip().upper()
        if len(fila) == 6 and all(base in 'ATCG' for base in fila):
            matriz.append(list(fila))  
            break 
        else:
            print("--ERROR--")

def menu():
    print("Ingrese un ADN que contenga las 4 bases nitrogenadas (una fila a la vez)
    print("Adenina (A), Timina (T), Citosina (C) y Guanina (G)")
    ingresarADN()
    
    #Menu
    print(f"La matriz ingresada es: ")
    for x in matriz:
        print(x)
    while True: 
        print("¿Que desea hacer?")
        print("1.Detectar mutaciones-2.Mutar-3.Sanar")
        opcionU = int(input("Seleccione una opción: "))
        
        match opcionU:
            case 1: 
                print("--Se llama a la funcion para detectar mutaciones--")
                ADNU=Detector(matriz)
                TipoM = ADNU.detectar_mutantes()
                print(TipoM)
                
            case 2: 
                    mutacion = input("Elija la base Nitrogenada que desae insertar: (A,T,C,G)>").upper()
    
                    #Evaluación de que la base ingresada sea correcta.
                    while True:
                        if not re.match("^([ATGC]*)$",mutacion):
                            print("El dato ingresado es incorrecto, vuelva a intentarlo")
                            mutacion = input("Elija la base Nitrogenada que desae insertar: (A,T,C,G)>").upper()
                                
                        else:
                            base_nitrogenada = mutacion * 4
                            print(f"La base nitrogenada ingresada es {base_nitrogenada}.")
                            print("Mutación ingresada correctamente")
                            break
            case 3: 
                ADNU = Sanador(matriz)
                print("--Se llama a la funcion para sanar mutaciones--")
               
            case 4: 
                print("--Se imprime el ADN ingresado--")
                print(matriz)
menu()

