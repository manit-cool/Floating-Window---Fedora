import sys
from PySide6.QtCore import Qt, QTimer, QTime

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)


class DragHeader(QWidget):
    """A custom header that lets us move the window."""

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            window = self.window().windowHandle()

            if window:
                window.startSystemMove()


class FloatingWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Window configuration
        self.setWindowFlags(
            Qt.WindowType.Window
            | Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        self.setMinimumWidth(280)

        self.build_ui()
        self.start_clock()

    def build_ui(self):

        # Main panel
        self.panel = QFrame()
        self.panel.setObjectName("panel")

        layout = QVBoxLayout(self.panel)
        layout.setContentsMargins(14, 12, 14, 14)

        # Header
        header = DragHeader()
        header_layout = QHBoxLayout(header)

        title = QLabel("MINI HUD")
        title.setObjectName("heading")

        close_button = QPushButton("×")
        close_button.setFixedSize(28, 28)
        close_button.clicked.connect(self.close)

        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(close_button)

        layout.addWidget(header)

        # Clock
        self.clock = QLabel()
        self.clock.setObjectName("clock")
        self.clock.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.clock)

        # Root layout
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.addWidget(self.panel)

        # Styling
        self.setStyleSheet("""
            QWidget {
                color: white;
                font-family: 'Inter';
            }

            QFrame#panel {
                background-color: rgba(10, 29, 40, 235);
                border: 1px solid rgba(255, 255, 255, 35);
                border-radius: 16px;
            }

            QLabel#heading {
                font-size: 13px;
                font-weight: bold;
            }

            QLabel#clock {
                font-size: 32px;
                font-weight: bold;
                padding: 18px;
            }

            QPushButton {
                background: transparent;
                border: none;
                font-size: 20px;
                border-radius: 6px;
            }

            QPushButton:hover {
                background-color: rgba(255, 255, 255, 30);
            }
        """)

    def start_clock(self):

        timer = QTimer(self)
        timer.timeout.connect(self.update_clock)
        timer.start(1000)

        self.update_clock()

    def update_clock(self):
        self.clock.setText(QTime.currentTime().toString("hh:mm:ss AP"))


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = FloatingWindow()
    window.show()
    window.raise_()
    
    sys.exit(app.exec())
