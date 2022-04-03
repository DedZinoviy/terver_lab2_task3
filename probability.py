from unittest import result
import numpy as np

def negativeProbability(probability):
    return 1 - probability


def someMachineBreakes(first, amount, negativeProbabilityList):
    resultProbability = 0
    if amount == 0:
        resultProbability = np.prod(negativeProbabilityList)
    elif amount == 1:
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
