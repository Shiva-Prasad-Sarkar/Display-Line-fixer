import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

class BlackBar(QWidget):
    def __init__(self, height=30, opacity=1.0, position="bottom", click_through=False):
        super().__init__()

        # Get primary screen dimensions
        screen = QApplication.primaryScreen().geometry()
        screen_width = screen.width()
        screen_height = screen.height()

        # Decide where to place the bar
        if position == "bottom":
            x = 0
            y = screen_height - height
        elif position == "top":
            x = 0
            y = 0
        else:
            x = 0
            y = screen_height - height  # fallback

        # Set size and position
        self.setGeometry(x, y, screen_width, height)

        # Window settings:
        # - No border
        # - Always on top
        # - Hidden from taskbar
        flags = Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool

        # Optional: allow clicks to pass through
        if click_through:
            flags |= Qt.WindowTransparentForInput

        self.setWindowFlags(flags)

        # Style (you can change color if needed)
        self.setStyleSheet("background-color: black;")

        # Opacity control (0.0 → transparent, 1.0 → solid)
        self.setWindowOpacity(opacity)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 🔧 Customize here
    bar_height = 30         # Adjust to match the damaged line
    bar_opacity = 1.0       # Transparency level
    bar_position = "bottom" # "bottom" or "top"
    click_through = False   # True = doesn't block mouse

    bar = BlackBar(
        height=bar_height,
        opacity=bar_opacity,
        position=bar_position,
        click_through=click_through
    )

    bar.show()
    sys.exit(app.exec_())
