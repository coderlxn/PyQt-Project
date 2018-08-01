import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.QtGui import QIcon
from login import LoginDialog
import resources

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_widget = LoginDialog()
    if login_widget.exec_() == QDialog.Accepted:
        main_window = QMainWindow()
        main_window.show()
        icon = QIcon("/Resources/bg.jpg")
        main_window.setWindowIcon(icon)
    else:
        sys.exit(0)
    sys.exit(app.exec_())
