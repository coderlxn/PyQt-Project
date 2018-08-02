from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt
from ui.login_ui import Ui_LoginDialog
import resources


class LoginDialog(QDialog):

    def __init__(self):
        super().__init__()
        ui = Ui_LoginDialog()
        ui.setupUi(self)

        self.setStyleSheet("#LoginDialog{background-image:url(:/Resources/bg.jpg)}")
        ui.pushButton.setObjectName("pushButton_global_accept")

        ui.pushButton.clicked.connect(self.accept)

    def keyPressEvent(self, ev):
        if ev.key() == Qt.Key_Escape:
            self.close()
