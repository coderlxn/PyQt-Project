from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt
from ui.login_ui import Ui_Dialog


class LoginDialog(QDialog):

    def __init__(self):
        super().__init__()
        ui = Ui_Dialog()
        ui.setupUi(self)

        ui.pushButton.clicked.connect(self.accept)

    def keyPressEvent(self, ev):
        if ev.key() == Qt.Key_Escape:
            self.close()
