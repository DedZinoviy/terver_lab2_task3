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

if __name__ == "__main__":
    list2 = [0.1, 0.2, 0.3]
    print(onlyTwoMachineBreakes(list2))
