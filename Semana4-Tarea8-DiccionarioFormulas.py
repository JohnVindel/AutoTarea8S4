#*****Examen, Ejercicio 6 - Diccionario de Formulas*****#

formulas = {
    "1": "Suma: 1 + 3 = 4",
    "2": "Resta: 2 - 3 = 1",
    "3": "Dividir: 2 / 6 = 3",
    "4": "Multiplicar: 2 * 5 = 10",
    "5": "Area de Circulo: 3.1416 * (7 * 2) = 43.9824"
}

try:
    intro = input("Ingrese del 1 al 5: ")
    print("La Formula {} es y se ejecuta asi {}.".format(intro, format(formulas[intro], )))
except KeyError:
    print ("La Formula que ingreso no existe")