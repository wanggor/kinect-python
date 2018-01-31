#!/usr/bin/python3


from PyQt5 import QtWidgets
from kinnect import MainWindow
import freenect
import sys

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    
    ui = MainWindow()
    ui.show()
    
    sys.exit(app.exec_())
    



