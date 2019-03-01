import sys
from PyQt5.QtWidgets import QDialog, QApplication
from chuckNorrisEncoder import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonConvertir.clicked.connect(self.convertir)


    def convertir(self):
        message = self.ui.input.toPlainText()
        b = ''
        # convertimos c a binario
        # ord() retorna el codigo uncode
        for a in enumerate(message):
            print(a[1])
            #b += ''.join(format(ord(a[1]), 'b'))
            b += "{0:07b}".format(ord(a[1]))
        b = list(b)
        print(b, len(b))
        # reglas
        # 0 0 (the first series consists of only a single 1)
        # 00 0000 (the second series consists of four 0)
        # 0 00 (the third consists of two 1)
        # 1000011
        result = ''
        index = 0
        index_2 = 0
        count = 1
        while(True):
            index_2 = index + count
            if (index_2 < len(b)):
                if (b[index_2] == b[index]):
                    count += 1
                else:
                    if b[index] == '1':
                        result += '0 ' + ('0'*count)+' '
                        count = 1
                        index = index_2
                        index_2 = 0
                    else:
                        result += '00 ' + ('0'*count)+' '
                        count = 1
                        index = index_2
                        index_2 = 0
            else:
                if b[index] == '1':
                    result += '0 ' + ('0'*count)+' '
                else:
                    result += '00 ' + ('0'*count)+' '
                break
        self.ui.output.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())