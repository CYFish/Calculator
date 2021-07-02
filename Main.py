import sys

from PySide2 import QtWidgets
from PySide2.QtCore import QFile, QIODevice
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton

from Calculator import Calculator
from ui_Calculator import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        self.calculator = Calculator()

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_button()

        self.ui.labelExpression.clear()
        self.ui.labelResult.setText(self.calculator.get_value_text())

    def operator_button_click(self):
        self.calculator.input_operator(self.sender().text())
        self.ui.labelResult.setText(self.calculator.get_value_text())
        self.ui.labelExpression.setText(self.calculator.get_expression())

    def operand_button_click(self):
        self.calculator.input_number(self.sender().text())
        self.ui.labelResult.setText(self.calculator.get_value_text())
        self.ui.labelExpression.setText(self.calculator.get_expression())

    def setup_button(self):
        self.ui.pushButtonZero.clicked.connect(self.operand_button_click)
        self.ui.pushButtonOne.clicked.connect(self.operand_button_click)
        self.ui.pushButtonTwo.clicked.connect(self.operand_button_click)
        self.ui.pushButtonThree.clicked.connect(self.operand_button_click)
        self.ui.pushButtonFour.clicked.connect(self.operand_button_click)
        self.ui.pushButtonFive.clicked.connect(self.operand_button_click)
        self.ui.pushButtonSix.clicked.connect(self.operand_button_click)
        self.ui.pushButtonSeven.clicked.connect(self.operand_button_click)
        self.ui.pushButtonEight.clicked.connect(self.operand_button_click)
        self.ui.pushButtonNine.clicked.connect(self.operand_button_click)

        self.ui.pushButtonDot.clicked.connect(self.operand_button_click)

        self.ui.pushButtonAdd.clicked.connect(self.operator_button_click)
        self.ui.pushButtonSubstract.clicked.connect(self.operator_button_click)
        self.ui.pushButtonMultiply.clicked.connect(self.operator_button_click)
        self.ui.pushButtonDivide.clicked.connect(self.operator_button_click)
        self.ui.pushButtonAC.clicked.connect(self.operator_button_click)
        self.ui.pushButtonPlusMinus.clicked.connect(self.operator_button_click)
        self.ui.pushButtonPercent.clicked.connect(self.operator_button_click)
        self.ui.pushButtonBackSpace.clicked.connect(self.operator_button_click)
        self.ui.pushButtonEqual.clicked.connect(self.operator_button_click)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())