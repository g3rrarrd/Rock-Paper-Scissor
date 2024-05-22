from Game import process, elements

class main:

    options = {1: "Paper", 2:"Rock", 3:"Scissor"}

    while True:
        try:
            print("what do you choose:\n 1.Paper \n 2.Rock \n 3.Scissor \n 4.Salir\n")
            value = int(input())
                
            if(value == 4):
                print("\n Adios")
                break
            elif(value > 3 or value < 1):
                print("Valor fuera del limite \n")
            else:
                pr = process.process()
                el = elements.elements()

                pr.result(options[value], el.element())
                pr.print_result()
        except ValueError as ve:
            print("Error en el valor ingresado, ingrese un numero \n")
        