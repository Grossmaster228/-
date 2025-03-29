import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox
from PyQt5.QtCore import Qt  # Добавлено исправление

class BoyleMariotteApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("График давления")
        self.setGeometry(500, 500, 1000, 600)
        self.setStyleSheet("background-color: lightgray;")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        title = QLabel("График давления газа от объёма", self)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.temp_input = QLineEdit(self)
        self.temp_input.setPlaceholderText("Введи температуру (К)")
        self.temp_input.setStyleSheet("padding: 15px; font-size: 14px;")
        layout.addWidget(self.temp_input)

        self.moles_input = QLineEdit(self)
        self.moles_input.setPlaceholderText("Введи кол-во вещества (моли)")
        self.moles_input.setStyleSheet("padding: 15px; font-size: 14px;")
        layout.addWidget(self.moles_input)

        self.unit_combo = QComboBox(self)
        self.unit_combo.addItem("Па")
        self.unit_combo.addItem("Атм")
        layout.addWidget(self.unit_combo)

        self.plot_button = QPushButton("Построить график", self)
        self.plot_button.setStyleSheet("background-color: green; color: white; font-size: 14px; padding: 10px;")
        self.plot_button.clicked.connect(self.plot_graph)
        layout.addWidget(self.plot_button)

        self.setLayout(layout)

    def plot_graph(self):
        try:
            T = float(self.temp_input.text())
            n = float(self.moles_input.text())
            unit = self.unit_combo.currentText()

            if T <= 0 or n <= 0:
                raise ValueError("Температура и количество вещества должны быть положительными!")

            R = 8.314
            V = np.linspace(0.01, 10, 100)
            P = (n * R * T) / V

            if unit == "Атм":
                P = P / 101325

            plt.plot(V, P)
            plt.xlabel("Объём (м³)")
            plt.ylabel(f"Давление ({unit})")
            plt.title("Закон Бойля-Мариотта")
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
    window = BoyleMariotteApp()
    window.show()
    sys.exit(app.exec())
