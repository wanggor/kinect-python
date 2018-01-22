# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/Achmadi/gak_jelas/test/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 552)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btnStart = QtWidgets.QPushButton(self.centralWidget)
        self.btnStart.setGeometry(QtCore.QRect(30, 10, 85, 27))
        self.btnStart.setObjectName("btnStart")
        self.btnStop = QtWidgets.QPushButton(self.centralWidget)
        self.btnStop.setGeometry(QtCore.QRect(130, 10, 85, 27))
        self.btnStop.setObjectName("btnStop")
        self.grphKnct = QtWidgets.QGraphicsView(self.centralWidget)
        self.grphKnct.setGeometry(QtCore.QRect(20, 50, 551, 471))
        self.grphKnct.setObjectName("grphKnct")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnStop.setText(_translate("MainWindow", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

