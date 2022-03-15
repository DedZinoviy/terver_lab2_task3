def negativeProbability(probability):
    return 1 - probability

machinesNumber = input()
machilneProbabilityList = list.append(input())

def atLeastOneMachineBreak(machinesNumber, machilneProbabilityList):
    for i in range(machinesNumber): #{Хотя бы один сломается} = {Не ни один не сломается} 
        resultProbability *= negativeProbability(machilneProbabilityList[i])
    return resultProbability

def allMachinesBreake(machinesNumber, machilneProbabilityList):
    for i in range(machinesNumber): # {Все станки сломаются} 
        resultProbability *= machilneProbabilityList[i]
    return resultProbability

def onlyChosenMachine(machineNumber, machineProbabilityList):
    resultProbability = machineProbabilityList[machineNumber] # {Только конкретный станок выйдет из строя}
    machineProbabilityList.remove(resultProbability)
    for value in machineProbabilityList: # и {не выйдут из строя остальные станки}
        resultProbability *= negativeProbability(value)
    return reusltProbability
