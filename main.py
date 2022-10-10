from PyQt6.QtWidgets import QApplication
from gui import FileDialog
import sys


app = QApplication([])
window_file = FileDialog()
sys.exit(app.exec())

