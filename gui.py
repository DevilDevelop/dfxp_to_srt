from typing import Callable
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QFileDialog
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from dfxp import DFXP
from srt import SRT


class Window(QWidget):
    def __init__(self, title: str, width: int, height: int) -> None:
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(width, height)


class Layout(QGridLayout):
    def __init__(self, window: Window) -> None:
        super().__init__(window)

    def add_widget(self, widget: QWidget, row: int, column: int, alignment: Qt.AlignmentFlag) -> None:
        self.addWidget(widget, row, column, alignment)


class Label(QLabel):
    def __init__(self, window: Window, text: str, font_size: int) -> None:
        super().__init__(window)
        self.setFont(QFont('Arial', font_size))
        self.setText(text)


class Button(QPushButton):
    def __init__(self, window: Window, text: str, function: Callable) -> None:
        super().__init__(window)
        self.setText(text)
        self.clicked.connect(function)


class FileDialog(Window):
    def __init__(self) -> None:
        super().__init__('DFXP to STR', 300, 150)
        self.file_path = None
        layout = Layout(self)
        open_label = Label(self, 'Select DFXP File:', 11)
        open_button = Button(self, 'Browse', self.open_file)
        continue_button = Button(self, 'Continue', self.convert_file)
        layout.add_widget(open_label, row=0, column=0, alignment=Qt.AlignmentFlag.AlignBottom)
        layout.add_widget(open_button, row=1, column=0, alignment=Qt.AlignmentFlag.AlignTop)
        layout.add_widget(continue_button, row=3, column=2, alignment=Qt.AlignmentFlag.AlignBottom)
        self.show()

    def open_file(self) -> None:
        file_path = QFileDialog.getOpenFileName(self)
        self.file_path = file_path[0]

    def convert_file(self) -> None:
        if self.file_path:
            dfxp = DFXP(self.file_path)
            srt = SRT(dfxp.file_name)
            subtitles = dfxp.get_subtitles()
            srt.add_subtitles(subtitles)
            srt.save()
            self.close()

            