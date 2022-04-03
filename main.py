from  PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from numpy import append
from ui import Ui_MainWindow
import sys
from probability import *

class mywindow(QtWidgets.QMainWindow):
    '''Конструктор гловного окна'''
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.amountSpinBox.editingFinished.connect(self.changeRowCount)
        self.ui.solveType.currentIndexChanged.connect(self.changeType)
        self.ui.solveButton.clicked.connect(self.countSomeElements)
        self.ui.img_lable.setPixmap(QPixmap("img/0.png"))

    '''Изменить количество строк в таблице вероятностей'''
    def changeRowCount(self):
        oldRowCount = self.ui.tableWidget.rowCount()
        rowAmount = self.ui.amountSpinBox.value()
        self.ui.tableWidget.setRowCount(rowAmount)
        for i in range(oldRowCount, rowAmount):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem("0.5"))
            self.ui.tableWidget.item(i, 0).setCheckState(QtCore.Qt.CheckState.Unchecked)

    '''Изменить интерфейс в зависимости от типа задачи'''
    def changeType(self):
        solveType = solveType = self.ui.solveType.currentIndex()
        self.ui.img_lable.setPixmap(QPixmap("img/" + str(solveType) + ".png"))
        if solveType < 2:
            self.ui.numbersSpinBox.setEnabled(True)
            self.ui.advice_label.setText("")
        else:
            self.ui.advice_label.setText("Отметьте нужные станки")
            self.ui.numbersSpinBox.setEnabled(False)

    '''Рассчитать выбранную задачу'''
    def countSomeElements(self):
        probabilities = []
        amountElements = self.ui.amountSpinBox.value()
        
        if amountElements <= 0:
            QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "Некорректное значение n \nКоличество элементов должно задаваться в диапазоне [1, 99]")
            return

        try:
            for i in range(self.ui.tableWidget.rowCount()):
                prob = float(self.ui.tableWidget.item(i, 0).text())
                if prob < 0 or prob > 1:
                    QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "Некорректное значение вероятности \"" + str(prob) +
                    "\"\nВероятности должна задаваться в диапазоне [0, 1]")
                    return
                else:
                    probabilities.append(negativeProbability(prob))
        except:
            QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "Некорректный формат ввода \"" + self.ui.tableWidget.item(i, 0).text()
            + "\"\nВероятность задается десятичной дробью, целая часть от дробной должна отделяться точкой \".\"")
            return
        
        solveType = self.ui.solveType.currentIndex()
        if solveType < 2:
            numbersElements = self.ui.numbersSpinBox.value()

            if numbersElements < 0 or numbersElements > len(probabilities):
                QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "k должно лежать в диапазоне [0, n]")
                return

            if solveType == 0:
                str_result = "{:01.8f}".format(round(someMachineBreakes(0, numbersElements, probabilities), 8))
            else:
                str_result = "{:01.8f}".format(round(atListSomeMachineBreakes(numbersElements, probabilities), 8))
        else:
            selectedElements = []
            for i, probability in enumerate(probabilities):
                probabilities[i] = negativeProbability(probability)
                if self.ui.tableWidget.item(i, 0).checkState() == QtCore.Qt.CheckState.Checked:
                    selectedElements.append(i)
            
            if len(selectedElements) < 1:
                QtWidgets.QMessageBox.warning(self, "Ошибка ввода", 
                "Не выбран ни однин станок\nЧтобы выбрать станок, отметьте его галочкой в таблице")
                return

            str_result = "{:01.8f}".format(round(onlyChosenMachinesBreakes(selectedElements, probabilities), 8))
        
        self.ui.resultLineEdit.setText(str_result)

if __name__ == '__main__': 
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    
    sys.exit(app.exec())