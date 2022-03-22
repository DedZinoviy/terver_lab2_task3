from  PyQt5 import QtWidgets
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
        self.ui.solveButton.clicked.connect(self.countSomeElements)

    def changeRowCount(self):
        oldRowCount = self.ui.tableWidget.rowCount()
        rowAmount = self.ui.amountSpinBox.value()
        self.ui.tableWidget.setRowCount(rowAmount)
        for i in range(oldRowCount, rowAmount):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem("0.5"))

    def countSomeElements(self):
        probabilities = []
        for i in range(self.ui.tableWidget.rowCount()):
            probabilities.append(negativeProbability(float(self.ui.tableWidget.item(i, 0).text())))
        amountElements = self.ui.numbersSpinBox.value()
        self.ui.resultLineEdit.setText(str(round(someMachineBreakes(0, amountElements, probabilities), 8)))

if __name__ == '__main__': 
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    
    sys.exit(app.exec())