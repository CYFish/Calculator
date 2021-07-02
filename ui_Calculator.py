# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calculator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(403, 600)
        font = QFont()
        font.setFamily(u"Source Code Pro")
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutInput = QGridLayout()
        self.gridLayoutInput.setObjectName(u"gridLayoutInput")
        self.gridLayoutInput.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayoutInput.setHorizontalSpacing(7)
        self.gridLayoutInput.setContentsMargins(5, 5, 5, 5)
        self.pushButtonEqual = QPushButton(self.centralwidget)
        self.pushButtonEqual.setObjectName(u"pushButtonEqual")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEqual.sizePolicy().hasHeightForWidth())
        self.pushButtonEqual.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonEqual, 6, 3, 1, 1)

        self.pushButtonPlusMinus = QPushButton(self.centralwidget)
        self.pushButtonPlusMinus.setObjectName(u"pushButtonPlusMinus")
        sizePolicy.setHeightForWidth(self.pushButtonPlusMinus.sizePolicy().hasHeightForWidth())
        self.pushButtonPlusMinus.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonPlusMinus, 6, 0, 1, 1)

        self.pushButtonDot = QPushButton(self.centralwidget)
        self.pushButtonDot.setObjectName(u"pushButtonDot")
        sizePolicy.setHeightForWidth(self.pushButtonDot.sizePolicy().hasHeightForWidth())
        self.pushButtonDot.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonDot, 6, 2, 1, 1)

        self.pushButtonZero = QPushButton(self.centralwidget)
        self.pushButtonZero.setObjectName(u"pushButtonZero")
        sizePolicy.setHeightForWidth(self.pushButtonZero.sizePolicy().hasHeightForWidth())
        self.pushButtonZero.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonZero, 6, 1, 1, 1)

        self.pushButtonDivide = QPushButton(self.centralwidget)
        self.pushButtonDivide.setObjectName(u"pushButtonDivide")
        sizePolicy.setHeightForWidth(self.pushButtonDivide.sizePolicy().hasHeightForWidth())
        self.pushButtonDivide.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonDivide, 2, 3, 1, 1)

        self.pushButtonAC = QPushButton(self.centralwidget)
        self.pushButtonAC.setObjectName(u"pushButtonAC")
        sizePolicy.setHeightForWidth(self.pushButtonAC.sizePolicy().hasHeightForWidth())
        self.pushButtonAC.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonAC, 2, 0, 1, 1)

        self.pushButtonSeven = QPushButton(self.centralwidget)
        self.pushButtonSeven.setObjectName(u"pushButtonSeven")
        sizePolicy.setHeightForWidth(self.pushButtonSeven.sizePolicy().hasHeightForWidth())
        self.pushButtonSeven.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonSeven, 3, 0, 1, 1)

        self.pushButtonSubstract = QPushButton(self.centralwidget)
        self.pushButtonSubstract.setObjectName(u"pushButtonSubstract")
        sizePolicy.setHeightForWidth(self.pushButtonSubstract.sizePolicy().hasHeightForWidth())
        self.pushButtonSubstract.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonSubstract, 4, 3, 1, 1)

        self.pushButtonOne = QPushButton(self.centralwidget)
        self.pushButtonOne.setObjectName(u"pushButtonOne")
        sizePolicy.setHeightForWidth(self.pushButtonOne.sizePolicy().hasHeightForWidth())
        self.pushButtonOne.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonOne, 5, 0, 1, 1)

        self.pushButtonFour = QPushButton(self.centralwidget)
        self.pushButtonFour.setObjectName(u"pushButtonFour")
        sizePolicy.setHeightForWidth(self.pushButtonFour.sizePolicy().hasHeightForWidth())
        self.pushButtonFour.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonFour, 4, 0, 1, 1)

        self.pushButtonMultiply = QPushButton(self.centralwidget)
        self.pushButtonMultiply.setObjectName(u"pushButtonMultiply")
        sizePolicy.setHeightForWidth(self.pushButtonMultiply.sizePolicy().hasHeightForWidth())
        self.pushButtonMultiply.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonMultiply, 3, 3, 1, 1)

        self.pushButtonSix = QPushButton(self.centralwidget)
        self.pushButtonSix.setObjectName(u"pushButtonSix")
        sizePolicy.setHeightForWidth(self.pushButtonSix.sizePolicy().hasHeightForWidth())
        self.pushButtonSix.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonSix, 4, 2, 1, 1)

        self.pushButtonFive = QPushButton(self.centralwidget)
        self.pushButtonFive.setObjectName(u"pushButtonFive")
        sizePolicy.setHeightForWidth(self.pushButtonFive.sizePolicy().hasHeightForWidth())
        self.pushButtonFive.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonFive, 4, 1, 1, 1)

        self.pushButtonEight = QPushButton(self.centralwidget)
        self.pushButtonEight.setObjectName(u"pushButtonEight")
        sizePolicy.setHeightForWidth(self.pushButtonEight.sizePolicy().hasHeightForWidth())
        self.pushButtonEight.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonEight, 3, 1, 1, 1)

        self.pushButtonPercent = QPushButton(self.centralwidget)
        self.pushButtonPercent.setObjectName(u"pushButtonPercent")
        sizePolicy.setHeightForWidth(self.pushButtonPercent.sizePolicy().hasHeightForWidth())
        self.pushButtonPercent.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonPercent, 2, 1, 1, 1)

        self.pushButtonNine = QPushButton(self.centralwidget)
        self.pushButtonNine.setObjectName(u"pushButtonNine")
        sizePolicy.setHeightForWidth(self.pushButtonNine.sizePolicy().hasHeightForWidth())
        self.pushButtonNine.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonNine, 3, 2, 1, 1)

        self.pushButtonBackSpace = QPushButton(self.centralwidget)
        self.pushButtonBackSpace.setObjectName(u"pushButtonBackSpace")
        sizePolicy.setHeightForWidth(self.pushButtonBackSpace.sizePolicy().hasHeightForWidth())
        self.pushButtonBackSpace.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonBackSpace, 2, 2, 1, 1)

        self.pushButtonAdd = QPushButton(self.centralwidget)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        sizePolicy.setHeightForWidth(self.pushButtonAdd.sizePolicy().hasHeightForWidth())
        self.pushButtonAdd.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonAdd, 5, 3, 1, 1)

        self.pushButtonTwo = QPushButton(self.centralwidget)
        self.pushButtonTwo.setObjectName(u"pushButtonTwo")
        sizePolicy.setHeightForWidth(self.pushButtonTwo.sizePolicy().hasHeightForWidth())
        self.pushButtonTwo.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonTwo, 5, 1, 1, 1)

        self.pushButtonThree = QPushButton(self.centralwidget)
        self.pushButtonThree.setObjectName(u"pushButtonThree")
        sizePolicy.setHeightForWidth(self.pushButtonThree.sizePolicy().hasHeightForWidth())
        self.pushButtonThree.setSizePolicy(sizePolicy)

        self.gridLayoutInput.addWidget(self.pushButtonThree, 5, 2, 1, 1)

        self.labelExpression = QLabel(self.centralwidget)
        self.labelExpression.setObjectName(u"labelExpression")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelExpression.sizePolicy().hasHeightForWidth())
        self.labelExpression.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(16)
        self.labelExpression.setFont(font1)
        self.labelExpression.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayoutInput.addWidget(self.labelExpression, 0, 0, 1, 4)

        self.labelResult = QLabel(self.centralwidget)
        self.labelResult.setObjectName(u"labelResult")
        sizePolicy1.setHeightForWidth(self.labelResult.sizePolicy().hasHeightForWidth())
        self.labelResult.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(32)
        self.labelResult.setFont(font2)
        self.labelResult.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayoutInput.addWidget(self.labelResult, 1, 0, 1, 4)


        self.gridLayout.addLayout(self.gridLayoutInput, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.pushButtonEqual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButtonPlusMinus.setText(QCoreApplication.translate("MainWindow", u"\u00b1", None))
        self.pushButtonDot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButtonZero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButtonDivide.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.pushButtonAC.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.pushButtonSeven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButtonSubstract.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButtonOne.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButtonFour.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButtonMultiply.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.pushButtonSix.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButtonFive.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButtonEight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButtonPercent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.pushButtonNine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButtonBackSpace.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.pushButtonAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButtonTwo.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButtonThree.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.labelExpression.setText("")
        self.labelResult.setText("")
    # retranslateUi

