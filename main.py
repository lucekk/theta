import sys
from PySide6.QtWidgets import QApplication
from src.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())