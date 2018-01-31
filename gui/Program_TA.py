#!/usr/bin/python3


from PyQt5 import QtWidgets
from kinnect import MainWindow
import freenect

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    print('a')
    sys.exit(app.exec_())
    



