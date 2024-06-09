import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QIntValidator, QDoubleValidator, QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression

class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculadora de IMC')
        
        layout = QVBoxLayout()

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText('Nombre')
        name_validator = QRegularExpressionValidator(QRegularExpression("[A-Za-záéíóúÁÉÍÓÚñÑ ]{4,}"))
        self.name_input.setValidator(name_validator)
        layout.addWidget(self.name_input)

        self.surname1_input = QLineEdit(self)
        self.surname1_input.setPlaceholderText('Primer Apellido')
        self.surname1_input.setValidator(name_validator)
        layout.addWidget(self.surname1_input)

        self.surname2_input = QLineEdit(self)
        self.surname2_input.setPlaceholderText('Segundo Apellido')
        self.surname2_input.setValidator(name_validator)
        layout.addWidget(self.surname2_input)

        self.age_input = QLineEdit(self)
        self.age_input.setPlaceholderText('Edad')
        self.age_input.setValidator(QIntValidator(0, 130, self))  # Edad entre 0 y 130
        layout.addWidget(self.age_input)

        self.weight_input = QLineEdit(self)
        self.weight_input.setPlaceholderText('Peso (kg)')
        self.weight_input.setValidator(QDoubleValidator(0.0, 700.0, 2, self))  # Peso entre 0.0 y 700.0 kg
        layout.addWidget(self.weight_input)

        self.height_input = QLineEdit(self)
        self.height_input.setPlaceholderText('Altura (m)')
        self.height_input.setValidator(QDoubleValidator(0.0, 2.80, 2, self))  # Altura entre 0.0 y 2.80 m
        layout.addWidget(self.height_input)

        self.calculate_button = QPushButton('Calcular IMC', self)
        self.calculate_button.clicked.connect(self.calculate_bmi)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel('', self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_bmi(self):
        # Obtener y validar datos de entrada
        name = self.name_input.text().strip()
        surname1 = self.surname1_input.text().strip()
        surname2 = self.surname2_input.text().strip()
        age_text = self.age_input.text().strip()
        weight_text = self.weight_input.text().strip()
        height_text = self.height_input.text().strip()

        if not name or not surname1 or not surname2 or not age_text or not weight_text or not height_text:
            QMessageBox.warning(self, 'Error de Entrada', 'Por favor, completa todos los campos.')
            return

        if len(name) < 4 or len(surname1) < 4 or len(surname2) < 4:
            QMessageBox.warning(self, 'Error de Entrada', 'Nombre y apellidos deben tener al menos 4 caracteres.')
            return

        try:
            age = int(age_text)
            weight = float(weight_text)
            height = float(height_text)

            if age > 130:
                QMessageBox.warning(self, 'Error de Entrada', 'La edad no puede exceder los 130 años.')
                return

            if weight > 700:
                QMessageBox.warning(self, 'Error de Entrada', 'El peso no puede exceder los 700 kg.')
                return

            if height > 2.80:
                QMessageBox.warning(self, 'Error de Entrada', 'La altura no puede exceder los 2.80 m.')
                return

            bmi = weight / (height ** 2)
            self.result_label.setText(f'Tu IMC es {bmi:.2f}')
        except ValueError:
            QMessageBox.warning(self, 'Error de Entrada', 'Por favor, introduce valores válidos para peso y altura.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BMICalculator()
    ex.show()
    sys.exit(app.exec())
