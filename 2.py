import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt  # Добавлено исправление

class HarmonicApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Гармоническое колебание")
        self.setGeometry(500, 500, 1000, 700)
        self.setStyleSheet("background-color: lightgray;")
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()

        title = QLabel("График гармонического колебания", self)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.amplitude_input = QLineEdit(self)
        self.amplitude_input.setPlaceholderText("Введи амплитуду (м)")
        self.amplitude_input.setStyleSheet("padding: 17px; font-size: 15px;")
        layout.addWidget(self.amplitude_input)

        self.frequency_input = QLineEdit(self)
        self.frequency_input.setPlaceholderText("Введи частоту (Гц)")
        self.frequency_input.setStyleSheet("padding: 17px; font-size: 15px;")
        layout.addWidget(self.frequency_input)

        self.phase_input = QLineEdit(self)
        self.phase_input.setPlaceholderText("Введи фазу (градусы)")
        self.phase_input.setStyleSheet("padding: 15px; font-size: 14px;")
        layout.addWidget(self.phase_input)

        self.plot_button = QPushButton("Построить график", self)
        self.plot_button.setStyleSheet("background-color: green; color: white; font-size: 14px; padding: 10px;")
        self.plot_button.clicked.connect(self.plot_graph)
        layout.addWidget(self.plot_button)

        self.setLayout(layout)

    def plot_graph(self):
        try:
            A = float(self.amplitude_input.text())
            f = float(self.frequency_input.text())
            phi = float(self.phase_input.text())

            if A <= 0 or f <= 0:
                raise ValueError("Амплитуда и частота должны быть положительными!")

            t = np.linspace(0, 10, 1000)
            x = A * np.cos(2 * np.pi * f * t + np.radians(phi))

            plt.plot(t, x)
            plt.xlabel("Время (с)")
            plt.ylabel("Смещение (м)")
            plt.title("Гармоническое колебание")
            plt.grid(True)
            plt.show()

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
    window = HarmonicApp()
    window.show()
    sys.exit(app.exec())
