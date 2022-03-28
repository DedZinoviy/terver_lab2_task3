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
        if solveType < 2:
            self.ui.numbersSpinBox.setEnabled(True)
            self.ui.advice_label.setText("")
        else:
            self.ui.advice_label.setText("Отметьте нужные станки")
            self.ui.numbersSpinBox.setEnabled(False)

    '''Рассчитать выбранную задачу'''
    def countSomeElements(self):
        probabilities = []
        
        try:
            for i in range(self.ui.tableWidget.rowCount()):
                prob = float(self.ui.tableWidget.item(i, 0).text())
                if prob < 0 or prob > 1:
                    QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "Некорректное значеник вероятности \"" + str(prob) +
                    "\"\nВероятности должна задаваться в диапазоне [0, 1]")
                    return
                else:
                    probabilities.append(negativeProbability(float(self.ui.tableWidget.item(i, 0).text())))
        except:
            QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "Некорректный формат ввода \"" + self.ui.tableWidget.item(i, 0).text()
            + "\"\nВероятность задается десятичной дробью, целая часть от дробной должна отделяться точкой \".\"")
            return
        
        solveType = self.ui.solveType.currentIndex()
        if solveType < 2:
            amountElements = self.ui.numbersSpinBox.value()

            if amountElements == 0 or amountElements > len(probabilities):
                QtWidgets.QMessageBox.warning(self, "Ошибка ввода", "k должно лежать в диапазоне [1, n]")
                return

            if solveType == 0:
                self.ui.resultLineEdit.setText(str(round(someMachineBreakes(0, amountElements, probabilities), 8)))
            else:
                self.ui.resultLineEdit.setText(str(round(atListSomeMachineBreakes(amountElements, probabilities), 8)))
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

            self.ui.resultLineEdit.setText(str(round(onlyChosenMachinesBreakes(selectedElements, probabilities), 8)))

if __name__ == '__main__': 
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    
    sys.exit(app.exec())