import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QFormLayout, QPushButton, QLabel, QLineEdit, QComboBox, QStackedLayout
)

class Layout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wybór layout'u")

        self.layout_selector = QComboBox()
        self.layout_selector.addItems(["VBox", "HBox", "Grid", "Form"])
        self.layout_selector.currentIndexChanged.connect(self.switch_layout)

        self.main_layout = QVBoxLayout()
        self.stack_layout = QStackedLayout()

        self.vbox_layout = self.create_vbox_layout()
        self.hbox_layout = self.create_hbox_layout()
        self.grid_layout = self.create_grid_layout()
        self.form_layout = self.create_form_layout()

        self.stack_layout.addWidget(self.wrap_in_widget(self.vbox_layout))
        self.stack_layout.addWidget(self.wrap_in_widget(self.hbox_layout))
        self.stack_layout.addWidget(self.wrap_in_widget(self.grid_layout))
        self.stack_layout.addWidget(self.wrap_in_widget(self.form_layout))

        self.main_layout.addWidget(self.layout_selector)
        self.main_layout.addLayout(self.stack_layout)
        self.setLayout(self.main_layout)

    def wrap_in_widget(self, layout):
        widget = QWidget()
        widget.setLayout(layout)
        return widget

    def create_vbox_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Przycisk 1"))
        layout.addWidget(QPushButton("Przycisk 2"))
        layout.addWidget(QPushButton("Przycisk 3"))
        return layout

    def create_hbox_layout(self):
        layout = QHBoxLayout()
        layout.addWidget(QPushButton("Przycisk A"))
        layout.addWidget(QPushButton("Przycisk B"))
        layout.addWidget(QPushButton("Przycisk C"))
        return layout

    def create_grid_layout(self):
        layout = QGridLayout()
        layout.addWidget(QPushButton("1,1"), 0, 0)
        layout.addWidget(QPushButton("1,2"), 0, 1)
        layout.addWidget(QPushButton("2,1"), 1, 0)
        layout.addWidget(QPushButton("2,2"), 1, 1)
        return layout

    def create_form_layout(self):
        layout = QFormLayout()
        layout.addRow(QLabel("Imię:"), QLineEdit())
        layout.addRow(QLabel("Nazwisko:"), QLineEdit())
        layout.addRow(QLabel("Telefon:"), QLineEdit())
        return layout

    def switch_layout(self, index):
        self.stack_layout.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication([])
    window = Layout()
    window.show()
    app.exec()
