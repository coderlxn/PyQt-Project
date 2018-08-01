import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui import login

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_widget = QDialog()
    login_ui = login.Ui_Dialog()
    login_ui.setupUi(login_widget)
    login_widget.show()
    sys.exit(app.exec_())
