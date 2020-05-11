from tkinter import *
from time import *
from hillclimbing import *
import csv
import os

try:
    from tkinter import ttk
except:
    import ttk

root = Tk()
root.title("Hill Climbing: Problema del Ciclista")

_buttonCalculate = None


def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def readData():
    _data = []
    with open("knapsack.csv", "r") as document:
        reader = csv.reader(document, delimiter=';')
        for element in reader:
            name, calories, weight = element
            _data.append([name, float(calories), float(weight)])
    return _data


def loadData():
    _data = readData()
    lenData = len(_data)
    for i in range(lenData):
        element = _data[i]
        name, calories, weight = element

        # Añadir s si la cantidda de calorías es diferente de 1
        cExtra = "s"
        if calories == 1.0:
            cExtra = ""

        text = "{}: {} caloría{}, {} kg".format(name, calories, cExtra, weight)
        labelElement = Label(root, text=text)
        labelElement.grid(row=(4 + i), column=0, columnspan=2)

    return _data


labelInstruction = Label(root, text="Si desea ingrese la cantidad de calorías mínimas y el peso máximo.")
labelInstruction.grid(row=0, column=0, columnspan=2)

labelCalories = Label(root, text="Calorías mínimas:")
labelCalories.grid(row=1, column=0)

entryCalories = Entry(root)
entryCalories.grid(row=1, column=1)

labelWeight = Label(root, text="Peso máximo:")
labelWeight.grid(row=2, column=0)

entryWeight = Entry(root)
entryWeight.grid(row=2, column=1)

labelData = Label(root, text="Datos del CSV:")
labelData.grid(row=3, column=0)


def calculate():
    global data, entryCalories, entryWeight, _buttonCalculate

    _buttonCalculate.config(state=DISABLED)

    minCalories = 2000.0
    maxWeight = 2.0

    calories = entryCalories.get()
    weight = entryWeight.get()

    if len(calories) != 0:
        minCalories = float(calories)
    if len(weight) != 0:
        maxWeight = float(weight)

    rowIndex = len(data) + 5

    labelData_ = Label(root, text="Datos:")
    labelData_.grid(row=(rowIndex + 1), column=0)

    labelMinCalories = Label(root, text="Calorías mínimas: {}".format(minCalories))
    labelMinCalories.grid(row=(rowIndex + 2), column=0)

    labelMaxWeight = Label(root, text="Peso máximo: {}".format(maxWeight))
    labelMaxWeight.grid(row=(rowIndex + 3), column=0)

    labelSolution = Label(root, text="Solución:")
    labelSolution.grid(row=(rowIndex + 4), column=0)

    solution, tCalories, tWeight = hillClimbing(data, minCalories, maxWeight)
    if len(solution) == 0:
        labelError = Label(root, text="No se encontró solución.")
        labelError.grid(row=(rowIndex + 5), column=0, columnspan=2)

        buttonRestart = ttk.Button(root, text="Reiniciar", command=restart)
        buttonRestart.grid(row=(rowIndex + 6), column=0, columnspan=2)
    else:
        labelSteps = Label(root, text="Pasos:")
        labelSteps.grid(row=(rowIndex + 5), column=0)

        rowIndex = rowIndex + 6

        for i in range(len(solution)):
            element = solution[i]

            name, calories, weight = element
            # Añadir s si la cantidda de calorías es diferente de 1
            cExtra = "s"
            if calories == 1.0:
                cExtra = ""

            text = "{}. {} , {} caloría{}, {} kg.".format((i + 1), name, calories, cExtra, weight)
            labelElement = Label(root, text=text)
            labelElement.grid(row=(rowIndex + i), column=0, columnspan=2)

        rowIndex = rowIndex + len(solution)

        labelTotalCalories = Label(root, text="Calorías totales: {}".format(tCalories))
        labelTotalCalories.grid(row=(rowIndex + 1), column=0)

        labelTotalWeight = Label(root, text="Peso total: {}".format(tWeight))
        labelTotalWeight.grid(row=(rowIndex + 2), column=0)

        buttonRestart = ttk.Button(root, text="Reiniciar", command=restart)
        buttonRestart.grid(row=(rowIndex + 3), column=0, columnspan=2)


data = loadData()

buttonCalculate = ttk.Button(root, text="Calcular", command=calculate)
buttonCalculate.grid(row=(len(data) + 4), column=1)

_buttonCalculate = buttonCalculate

root.mainloop()
