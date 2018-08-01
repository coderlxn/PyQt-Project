import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from login import LoginDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_widget = LoginDialog()
    if login_widget.exec_() == QDialog.Accepted:
        main_window = QMainWindow()
        main_window.show()
    sys.exit(app.exec_())
