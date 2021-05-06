import sys
from PyQt5.QtWidgets import QDialog, QApplication
from menu import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.check_vanilla.stateChanged.connect(self.display_amount)
        self.ui.check_chocolate.stateChanged.connect(self.display_amount)
        self.ui.check_mint.stateChanged.connect(self.display_amount)
        self.ui.check_banana.stateChanged.connect(self.display_amount)
        self.ui.check_coffee.stateChanged.connect(self.display_amount)
        self.ui.check_soda.stateChanged.connect(self.display_amount)
        self.ui.check_milkshake.stateChanged.connect(self.display_amount)
        self.ui.check_tea.stateChanged.connect(self.display_amount)
        self.show()

    def display_amount(self):
        ice_cream = 0
        drinks = 0
        total = 0.0
        if self.ui.check_chocolate.isChecked():
            ice_cream += 1
            total += 27
        if self.ui.check_vanilla.isChecked():
            ice_cream += 1
            total += 22.5
        if self.ui.check_mint.isChecked():
            ice_cream += 1
            total += 34.99
        if self.ui.check_banana.isChecked():
            ice_cream += 1
            total += 28.99
        if self.ui.check_coffee.isChecked():
            drinks += 1
            total += 12.5
        if self.ui.check_soda.isChecked():
            drinks += 1
            total += 15
        if self.ui.check_milkshake.isChecked():
            drinks += 1
            total += 25.99
        if self.ui.check_tea.isChecked():
            drinks += 1
            total += 9.99
        self.ui.label_total_ice_cream.setText("# Ice Creams: %d" % ice_cream)
        self.ui.label_total_drinks.setText("# Drinks: %d" % drinks)
        self.ui.label_total_amount.setText("Total Price: R%.2f" % total)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())