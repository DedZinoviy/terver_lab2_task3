from unittest import result
import numpy as np

def negativeProbability(probability):
    return 1 - probability

#machinesNumber = input()
#machilneProbabilityList = list.append(input())

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
def onlyOneMachineBreakes(machineProbabilityList):
    resultProbability = 0
    negativeProbabilityList = []
    for probability in machineProbabilityList: # Для каждого элемента списка значений вероятностей
        negativeProbabilityList.append(negativeProbability(probability))
    for i in range(len(negativeProbabilityList)):
        negativeProbabilityList[i] = negativeProbability(negativeProbabilityList[i])
        resultProbability += np.prod(negativeProbabilityList)
        negativeProbabilityList[i] = negativeProbability(negativeProbabilityList[i])
    return resultProbability

def onlyTwoMachineBreakes(machineProbabilityList):
    resultProbability = 0
    negativeProbabilityList = []
    for probability in machineProbabilityList: # Для каждого элемента списка значений вероятностей
        negativeProbabilityList.append(negativeProbability(probability))
    for i in range(len(negativeProbabilityList) - 1):
        negativeProbabilityList[i] = negativeProbability(negativeProbabilityList[i])
        for j in range(i + 1, len(negativeProbabilityList)):
            negativeProbabilityList[j] = negativeProbability(negativeProbabilityList[j])
            resultProbability += np.prod(negativeProbabilityList)
            negativeProbabilityList[j] = negativeProbability(negativeProbabilityList[j])
        negativeProbabilityList[i] = negativeProbability(negativeProbabilityList[i])
    return resultProbability

def someMachineBreakes(first, amount, negativeProbabilityList):
    resultProbability = 0
    if amount == 1:
        for i in range(first, len(negativeProbabilityList)):
            negativeProbabilityList[i] = negativeProbability(negativeProbabilityList[i])
            resultProbability += np.prod(negativeProbabilityList)
            negativeProbabilityList[i] = negativeProbability(negativeProbabilityList[i])
    else:
        for i in range(first, len(negativeProbabilityList) - amount + 1):
            negativeProbabilityList[i] = negativeProbability(negativeProbabilityList[i])
            resultProbability += someMachineBreakes(i + 1, amount - 1, negativeProbabilityList)
            negativeProbabilityList[i] = negativeProbability(negativeProbabilityList[i])
    return resultProbability


def atListSomeMachineBreakes(amount, negativeProbabilityList):
    resultProbability = 0
    for i in range(amount, len(negativeProbabilityList) + 1):
        resultProbability += someMachineBreakes(0, i, negativeProbabilityList)
    return resultProbability

def onlyChosenMachinesBreakes(machinNumbers, probabilityList):
    chosenMachines = []
    notChosenMachines = []
    for i in range(len(probabilityList)):
        if i in machinNumbers:
            chosenMachines.append(probabilityList[i])
        else:
            notChosenMachines.append(negativeProbability(probabilityList[i]))
    resultProbability = np.prod(chosenMachines) * np.prod(notChosenMachines)
    return resultProbability
