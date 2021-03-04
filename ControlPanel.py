
import sys
import serial
import time
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt

from UI.window_2 import Ui_Dialog
from Classes.jrk import JrkG2Serial

class main_window(QDialog):
    def __init__(self):
        self.jrks = {}
        self.selected = None

        super(main_window,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.assign_widgets()
        self.show()
        
    def assign_widgets(self):
        self.ui.con_but.clicked.connect(self.connect)
        self.ui.set_but.clicked.connect(self.SP)
        self.ui.stop_but.clicked.connect(self.stop)
        self.ui.Boards.itemClicked.connect(self.select)

    def connect(self):
        com = self.ui.com_in.text()
        try:
            port = serial.Serial(com, 9600, timeout=0.1, write_timeout=0.1)
            jrk = JrkG2Serial(port,None)
            if com not in self.jrks.keys():
                self.jrks[com]=jrk
                self.ui.Boards.addItem(com)
            self.ui.status_out.setText("Added port: " + com)
        except:
            self.ui.status_out.setText("Could not connect to port: " + com)

    def select(self,item):
        self.selected = item.text()

    def SP(self):
        try:
            ω = self.ui.SP_in.value()
            self.jrks[self.selected].set_target_RPM(ω)
            self.ui.status_out.setText("Motor setpoint: {:.2f} [RPM]".format(ω))
        except:
            self.ui.status_out.setText("Setpoint was not set")

    def stop(self):
        try:
            for i in self.jrks:
                self.jrks[i].stop()
            self.ui.status_out.setText("Motors are stopped")
        except:
            self.ui.status_out.setText("Jrk not initialized")

    def ExitApp(self):
        self.stop()
        app.exit()

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())