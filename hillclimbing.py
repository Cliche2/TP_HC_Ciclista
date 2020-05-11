# data = [["Leche de Soya", 500, 0.50],
#         ["Galleta Integral", 300, 0.10],
#         ["Agua Mineral", 100, 0.50],
#         ["Pan con Pollo", 700, 0.25],
#         ["Huevo duro", 300, 0.15],
#         ["Nueces", 400, 0.15],
#         ["Yogurt", 500, 0.50],
#         ["Manzana", 400, 0.30]]


def evaluate(_data, maxWeight, cCalories, cWeight):
    nItem = ""
    nCalories = 0
    nWeight = 0
    nValue = -1

    if (len(_data) == 0):
        return [nItem, nCalories, nWeight], nValue

    toEvaluate = [row[:] for row in _data]
    for row in toEvaluate:
        del row[0]
    totalCalories, totalWeight = [round(sum(x), 2) for x in zip(*toEvaluate)]

    for element in _data:
        item = element[0]
        calories = element[1]
        weight = element[2]
        vCalories = calories / totalCalories * 100
        vWeight = weight / totalWeight * 100
        value = round(vCalories - vWeight, 2)

        if (cWeight + weight) <= maxWeight:
            if value > nValue:
                nValue = value
                nItem = item
                nCalories = calories
                nWeight = weight
    return [nItem, nCalories, nWeight], nValue


def hillClimbing(_data, minCalories = 2000, maxWeight = 2, solution=[], cCalories=0, cWeight=0):
    nElement, nValue = evaluate(_data, maxWeight, cCalories, cWeight)

    if nValue == -1:
        if cCalories < minCalories:
            print("No se encontró solución.")
            return [], 0, 0
        else:
            print("Solución", solution)
            print("Calorias Totales", cCalories)
            print("Peso Total", cWeight)
            return solution, cCalories, cWeight

    cCalories = cCalories + nElement[1]
    cWeight = cWeight + nElement[2]

    solution.append(nElement)

    _data.remove(nElement)
    return hillClimbing(_data, minCalories, maxWeight, solution, cCalories, cWeight)


def initAlgorithm(data, minCalories, maxWeight):
    data_ = [row[:] for row in data]
    return hillClimbing(data_, minCalories, maxWeight)
