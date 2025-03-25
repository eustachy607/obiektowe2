import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QLabel,QVBoxLayout, QRadioButton, QCheckBox, QPushButton, QScrollArea, QButtonGroup, QMessageBox, QLineEdit
from PySide6.QtCore import Qt

def stylizuj_tekst(tekst):
    return f"<div style='background-color:white; color:black; padding:5px;'><b>{tekst}</b></div>"

class Quiz(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stolice Quiz")

        scroll_area = QScrollArea()
        centralny_widget = QWidget()
        scroll_area.setWidget(centralny_widget)
        scroll_area.setWidgetResizable(True)
        self.setCentralWidget(scroll_area)
        self.resize(800,500)

        layout = QVBoxLayout()

        self.tytul = QLabel("QUIZ STOLICE")
        self.tytul.setAlignment(Qt.AlignCenter)
        self.tytul.setStyleSheet("font-weight: bold")
        layout.addWidget(self.tytul)

        # Pytanie nr 1:
        self.pytanie1 = QLabel(stylizuj_tekst("1. Zaznacz stolicę Niemiec:"))
        self.radio_group1 = QButtonGroup(self)
        self.radio_button1_1 = QRadioButton("Berlin")
        self.radio_button1_2 = QRadioButton("Frankfurt")
        self.radio_button1_3 = QRadioButton("Monachium")

        self.radio_group1.addButton(self.radio_button1_1)
        self.radio_group1.addButton(self.radio_button1_2)
        self.radio_group1.addButton(self.radio_button1_3)

        layout.addWidget(self.pytanie1)
        layout.addWidget(self.radio_button1_1)
        layout.addWidget(self.radio_button1_2)
        layout.addWidget(self.radio_button1_3)

        # Pytanie nr 2:
        self.pytanie2 = QLabel(stylizuj_tekst("2. Zaznacz stolicę Polski:"))
        self.checkbox2_1 = QCheckBox("Warszawa")
        self.checkbox2_2 = QCheckBox("Poznań")
        self.checkbox2_3 = QCheckBox("Kraków")

        layout.addWidget(self.pytanie2)
        layout.addWidget(self.checkbox2_1)
        layout.addWidget(self.checkbox2_2)
        layout.addWidget(self.checkbox2_3)

        # Pytanie nr 3:
        self.pytanie3 = QLabel(stylizuj_tekst("3. Zaznacz stolicę Francji:"))
        self.radio_group3 = QButtonGroup(self)
        self.radio_button3_1 = QRadioButton("Marsylia")
        self.radio_button3_2 = QRadioButton("Paryż")
        self.radio_button3_3 = QRadioButton("Nicea")

        self.radio_group3.addButton(self.radio_button3_1)
        self.radio_group3.addButton(self.radio_button3_2)
        self.radio_group3.addButton(self.radio_button3_3)

        layout.addWidget(self.pytanie3)
        layout.addWidget(self.radio_button3_1)
        layout.addWidget(self.radio_button3_2)
        layout.addWidget(self.radio_button3_3)

        # Pytanie nr 4:
        self.pytanie4 = QLabel(stylizuj_tekst("4. Zaznacz stolicę Anglii:"))
        self.radio_group4 = QButtonGroup(self)
        self.radio_button4_1 = QRadioButton("Liverpool")
        self.radio_button4_2 = QRadioButton("Manchester")
        self.radio_button4_3 = QRadioButton("Londyn")

        self.radio_group4.addButton(self.radio_button4_1)
        self.radio_group4.addButton(self.radio_button4_2)
        self.radio_group4.addButton(self.radio_button4_3)

        layout.addWidget(self.pytanie4)
        layout.addWidget(self.radio_button4_1)
        layout.addWidget(self.radio_button4_2)
        layout.addWidget(self.radio_button4_3)

        # Pytanie nr 5:
        self.pytanie5 = QLabel(stylizuj_tekst("5. Zaznacz stolicę Belgii:"))
        self.checkbox5_1 = QCheckBox("Bruksela")
        self.checkbox5_2 = QCheckBox("Brugia")
        self.checkbox5_3 = QCheckBox("Antwerpia")

        layout.addWidget(self.pytanie5)
        layout.addWidget(self.checkbox5_1)
        layout.addWidget(self.checkbox5_2)
        layout.addWidget(self.checkbox5_3)

        centralny_widget.setLayout(layout)

        # Pytanie nr 6:
        self.pytanie6 = QLabel(stylizuj_tekst("6. Podaj nazwę stolicy Czech: "))
        self.odpowiedz = QLineEdit()
        layout.addWidget(self.pytanie6)
        layout.addWidget(self.odpowiedz)

        # Przycisk sprawdzający:

        self.check_button = QPushButton("Sprawdź")
        self.check_button.clicked.connect(self.sprawdzenie_odp)
        layout.addWidget(self.check_button)

    def sprawdzenie_odp(self):
            punkty = 0
            poprawne_odp = {"Praga", "praga"}
            odp_uzyt = self.odpowiedz.text().strip()

            if self.radio_button1_1.isChecked():
                punkty += 1

            # Pytanie 2: tylko Warszawa powinna być zaznaczona
            if self.checkbox2_1.isChecked() and not self.checkbox2_2.isChecked() and not self.checkbox2_3.isChecked():
                punkty += 1

            if self.radio_button3_2.isChecked():
                punkty += 1

            if self.radio_button4_3.isChecked():
                punkty += 1

            # Pytanie 5: tylko Bruksela powinna być zaznaczona
            if self.checkbox5_1.isChecked() and not self.checkbox5_2.isChecked() and not self.checkbox5_3.isChecked():
                punkty += 1

            if odp_uzyt in poprawne_odp:
                punkty += 1

            QMessageBox.information(self, "Wynik", f"Zdobyłeś {punkty} na 6 punktów!")




app = QApplication([])
quiz = Quiz()
quiz.show()
app.exec()
