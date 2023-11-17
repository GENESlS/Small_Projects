import sys
import math
#import keyboard
from PyQt6.QtCore import Qt
#from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import *

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")

        # create display label
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setMaxLength(15)
        self.display.setFixedHeight(50)

        # create buttons
        self.buttons = {}
        button_layouts = {}
        button_labels = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ".", "=", "+"),
            ("%", "^", "sqrt", "log"),
            ("mod", "exp", "C", "")
        ]
        for row, labels in enumerate(button_labels):
            button_layouts[row] = QHBoxLayout()
            for label in labels:
                self.buttons[label] = QPushButton(label)
                self.buttons[label].setFixedSize(50, 50)
                button_layouts[row].addWidget(self.buttons[label])
            button_layouts[row].addStretch()
        
        # create main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        for row in button_layouts.values():
            main_layout.addLayout(row)

        # set layout
        self.setLayout(main_layout)

        # connect buttons to functions
        for label, button in self.buttons.items():
            if label == "=":
                button.clicked.connect(self.calculate)
            elif label == "sqrt":
                button.clicked.connect(lambda label=label: self.square_root())
            elif label == "log":
                button.clicked.connect(lambda label=label: self.logarithm())
            elif label == "mod":
                button.clicked.connect(lambda label=label: self.modulus())
            elif label == "exp":
                button.clicked.connect(lambda label=label: self.exponential())
            elif label == "^":
                button.clicked.connect(lambda label=label: self.exponentiation())
            elif label == "C":
                button.clicked.connect(lambda label=label: self.clear())
            else:
                button.clicked.connect(lambda _, label=label: self.append(label))

    def append(self, text):
        self.display.setText(self.display.text() + text)

    def calculate(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except:
            self.display.setText("Error")

    def square_root(self):
        try:
            num = float(self.display.text())
            result = math.sqrt(num)
            self.display.setText(str(result))
        except:
            self.display.setText("Error")

    def logarithm(self):
        try:
            num = float(self.display.text())
            base, ok = QInputDialog.getDouble(self, "Logarithm", "Enter the base:")
            if ok:
                result = math.log(num, base)
                self.display.setText(str(result))
        except:
            self.display.setText("Error")

    def modulus(self):
        try:
            num1 = float(self.display.text())
            num2, ok = QInputDialog.getDouble(self, "Modulus", "Enter another number:")
            if ok:
                result = num1 % num2
                self.display.setText(str(result))
        except:
            self.display.setText("Error")

    def exponential(self):
        try:
            num = float(self.display.text())
            result = math.exp(num)
            self.display.setText(str(result))
        except:
            self.display.setText("Error")

    def exponentiation(self):
        try:
            num1 = float(self.display.text())
            num2, ok = QInputDialog.getDouble(self, "Exponentiation", "Enter another number:")
            if ok:
                result = num1 ** num2
                self.display.setText(str(result))
        except:
            self.display.setText("Error")
    
    def clear(self):
        self.display.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
