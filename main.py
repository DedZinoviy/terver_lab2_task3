def negativeProbability(probability):
    return 1 - probability

machinesNumber = input()
machilneProbabilityList = list.append(input())

def atLeastOneMachineBreak(machinesNumber, machilneProbabilityList):
    resultProbability = 1
    for i in range(0, machinesNumber): #{Хотя бы один сломается} = {Не ни один не сломается} 
        resultProbability *= negativeProbability(machilneProbabilityList[i])
    return resultProbability

def allMachinesBreake(machinesNumber, machilneProbabilityList):
    resultProbability = 1
    for i in range(0, machinesNumber): # {Все станки сломаются} 
        resultProbability *= machilneProbabilityList[i]
    return resultProbability

def onlyChosenMachine(machineNumber, machineProbabilityList):
    resultProbability = machineProbabilityList[machineNumber] # {Только конкретный станок выйдет из строя}
    machineProbabilityList.remove(resultProbability)
    for value in machineProbabilityList: # и {не выйдут из строя остальные станки}
        resultProbability *= negativeProbability(value)
    return resultProbability

# A_i = {не работает iый станок}
# Тогда {не работает только один} = A_1 * !(A_2) * !(A_3) + !(A_1) * A_2 * !(A_3) + !(A_1) * !(A_2) * A_3 и т. д.
def onlyOneMachineBreakes(machinesNumber, machineProbabilityList):
    resultProbability = 0 
    for i in range(0, machinesNumber): # Для каждого элемента списка значений вероятностей
        tmp = machineProbabilityList[i] # Сохраняем текущий элемент во временную переменную
        machineProbabilityList.pop(i) # Извлекаем текущий элемент из списка
        tmpResult = 1 
        for value in machineProbabilityList: # Делаем произведение обратных вероятностей оставшихся элементов
            tmpResult *= negativeProbability(value) 
        tmpResult *= tmp # Домножаем на временную вероятность поломки рассматриваемого станка
        resultProbability += tmpResult # Суммируем получившиеся произведения, т. к. произведения несовместны
        machineProbabilityList.insert(i, tmp) # Возвращаем временный элемент на свою исходную позицию
    return resultProbability
