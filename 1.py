import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout, QComboBox
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class StylishApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Траектория полета")
        self.setGeometry(500, 500, 1000, 700)
        self.setStyleSheet("background-color: white;")
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()

        title = QLabel("Моделирование траектории полета тела", self)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; padding: 20px;")
        layout.addWidget(title)

        form_layout = QVBoxLayout()

        self.speed_input = QLineEdit(self)
        self.speed_input.setPlaceholderText("Скорость (м/с)")
        self.speed_input.setStyleSheet("padding: 17px; font-size: 15px;")
        form_layout.addWidget(self.speed_input)

        self.angle_input = QLineEdit(self)
        self.angle_input.setPlaceholderText("Угол (градусы)")
        self.angle_input.setStyleSheet("padding: 17px; font-size: 15px;")
        form_layout.addWidget(self.angle_input)

        self.plot_button = QPushButton("Построить траекторию", self)
        self.plot_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 14px; padding: 10px;")
        self.plot_button.clicked.connect(self.plot_trajectory)
        form_layout.addWidget(self.plot_button)

        layout.addLayout(form_layout)

        self.canvas = FigureCanvas(plt.figure())
        self.canvas.setFixedSize(600, 400)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def plot_trajectory(self):
        try:
            speed = float(self.speed_input.text())
            angle = float(self.angle_input.text())

            if speed <= 0 or angle < 0 or angle > 90:
                raise ValueError("Скорость должна быть положительной, угол от 0 до 90 градусов.")

            g = 9.81
            angle_rad = np.radians(angle)
            t_flight = 2 * speed * np.sin(angle_rad) / g
            t = np.linspace(0, t_flight, 500)
            x = speed * np.cos(angle_rad) * t
            y = speed * np.sin(angle_rad) * t - 0.5 * g * t ** 2

            self.canvas.figure.clear()
            ax = self.canvas.figure.add_subplot(111)
            ax.plot(x, y, color='b', linewidth=2)
            ax.set_xlabel("Расстояние (м)")
            ax.set_ylabel("Высота (м)")
            ax.set_title("Траектория полета")
            ax.grid(True)

            self.canvas.draw()

        except ValueError as e:
            self.show_error_message(str(e))

    def show_error_message(self, message):
        error_window = QWidget()
        error_window.setWindowTitle("Ошибка")
        error_label = QLabel(message, error_window)
        error_label.setStyleSheet("font-size: 14px; color: red; padding: 20px;")
        error_label.move(20, 20)
        error_window.resize(300, 100)
        error_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StylishApp()
    window.show()
    sys.exit(app.exec())
