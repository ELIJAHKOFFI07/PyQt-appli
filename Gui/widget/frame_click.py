from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Signal


class ClickableFrame(QFrame):
    clicked = Signal()

    def mousePressEvent(self, event):
        self.clicked.emit()
