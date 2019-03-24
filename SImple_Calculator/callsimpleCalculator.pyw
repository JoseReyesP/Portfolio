import sys
from PyQt5.QtWidgets import QDialog, QApplication
from simpleCalculator import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_0.clicked.connect(self.input)
        self.ui.pushButton_1.clicked.connect(self.input)
        self.ui.pushButton_2.clicked.connect(self.input)
        self.ui.pushButton_3.clicked.connect(self.input)
        self.ui.pushButton_4.clicked.connect(self.input)
        self.ui.pushButton_5.clicked.connect(self.input)
        self.ui.pushButton_6.clicked.connect(self.input)
        self.ui.pushButton_7.clicked.connect(self.input)
        self.ui.pushButton_8.clicked.connect(self.input)
        self.ui.pushButton_9.clicked.connect(self.input)
        self.ui.pushButton_result.clicked.connect(self.input)
        self.ui.pushButton_modulo.clicked.connect(self.input)
        self.ui.pushButton_divide.clicked.connect(self.input)
        self.ui.pushButton_mult.clicked.connect(self.input)
        self.ui.pushButton_square.clicked.connect(self.input)
        self.ui.pushButton_root.clicked.connect(self.input)
        self.ui.pushButton_add.clicked.connect(self.input)
        self.ui.pushButton_sub.clicked.connect(self.input)
        self.ui.pushButton_comma.clicked.connect(self.input)
        self.ui.pushButton_undo.clicked.connect(self.input)
        self.ui.pushButton_leftParenthesis.clicked.connect(self.input)
        self.ui.pushButton_rightParenthesis.clicked.connect(self.input)
        self.ui.pushButton_clear.clicked.connect(self.input)

    def input(self):
        sending_button = self.sender()
        if sending_button.objectName()=="pushButton_0":
            self.ui.lineEditInput.setText("0")
        if sending_button.objectName() == "pushButton_1":
            self.ui.lineEditInput.setText("1")
        if sending_button.objectName() == "pushButton_2":
            self.ui.lineEditInput.setText("2")
        if sending_button.objectName() == "pushButton_3":
            self.ui.lineEditInput.setText("3")
        if sending_button.objectName() == "pushButton_4":
            self.ui.lineEditInput.setText("4")
        if sending_button.objectName() == "pushButton_5":
            self.ui.lineEditInput.setText("5")
        if sending_button.objectName() == "pushButton_6":
            self.ui.lineEditInput.setText("6")
        if sending_button.objectName() == "pushButton_7":
            self.ui.lineEditInput.setText("7")
        if sending_button.objectName() == "pushButton_8":
            self.ui.lineEditInput.setText("8")
        if sending_button.objectName() == "pushButton_9":
            self.ui.lineEditInput.setText("9")
        if sending_button.objectName() == "pushButton_add":
            self.ui.lineEditInput.setText("add")
        if sending_button.objectName() == "pushButton_sub":
            self.ui.lineEditInput.setText("subs")
        if sending_button.objectName() == "pushButton_divide":
            self.ui.lineEditInput.setText("divide")
        if sending_button.objectName() == "pushButton_mult":
            self.ui.lineEditInput.setText("multiply")
        if sending_button.objectName() == "pushButton_comma":
            self.ui.lineEditInput.setText("comma")
        if sending_button.objectName() == "pushButton_square":
            self.ui.lineEditInput.setText("square")
        if sending_button.objectName() == "pushButton_root":
            self.ui.lineEditInput.setText("root")
        if sending_button.objectName() == "pushButton_leftParenthesis":
            self.ui.lineEditInput.setText("(")
        if sending_button.objectName() == "pushButton_rightParenthesis":
            self.ui.lineEditInput.setText(")")
        if sending_button.objectName() == "pushButton_result":
            self.ui.lineEditInput.setText("result")
        if sending_button.objectName() == "pushButton_clear":
            self.ui.lineEditInput.setText("clear")
        if sending_button.objectName() == "pushButton_undo":
            self.ui.lineEditInput.setText("undo")
        if sending_button.objectName() == "pushButton_modulo":
            self.ui.lineEditInput.setText("modulo")


        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
