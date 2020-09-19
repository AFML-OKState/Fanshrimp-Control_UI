
import sys
import serial
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from UI.window import Ui_Dialog
from Classes.jrk import JrkG2Serial

class main_window(QDialog):
    def __init__(self):
        
        super(main_window,self).__init__()

        #back to standard code
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.assign_widgets()
        self.show()

    def assign_widgets(self):
        self.ui.con_but.clicked.connect(self.connect)
        self.ui.set_but.clicked.connect(self.SP)
        self.ui.stop_but.clicked.connect(self.stop)

    def connect(self):
        com = self.ui.com_in.text()
        try:
            port = serial.Serial(com, 9600, timeout=0.1, write_timeout=0.1)
            self.jrk = JrkG2Serial(port,None)
            print("Connected")
        except:
            print("Could not connect to port:" + com)

    def SP(self):
        try:
            f = int(self.ui.SP_in.value())
            self.jrk.set_target(f)
        except:
            print("Jrk not initialized")

    def stop(self):
        try:
            self.jrk.stop()
        except:
            print("Jrk not initialized")

    def ExitApp(self):
        app.exit()

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())