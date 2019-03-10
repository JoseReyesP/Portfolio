import sys
from PyQt5.QtWidgets import QDialog, QApplication
from chuckNorrisEncoder import *
import numpy as np



class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonEncode.clicked.connect(self.encode)
        self.ui.pushButtonDecode.clicked.connect(self.decode)
    def encode(self):
        message = self.ui.input.toPlainText()
        b = ''
        for a in enumerate(message):
            print(a[1])
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
        self.ui.output.setText(result[:-1])
    
    def decode(self):
        s = self.ui.input.toPlainText()
        print('revisando cadena')
        for char in s:
            if(char != '0' and char != ' '):
                self.ui.output.setText('There is something wrong with the code, please verify')
        print('separando cadena')
        a = s.split(' ')
        index = 0
        count = 0
        res = ''
        arrayLen = len(a)
        print('iniciando ciclo',a)
        while(True):
            if (index < arrayLen):
                if(a[index] == '0'):
                    count = len(a[index + 1])
                    res += '1'*count
                    index += 2
                elif(a[index] == '00'):
                    count = len(a[index + 1])
                    res += '0'*count
                    index += 2
                print('res',res)
                
            else:
                break
        a = np.array([x for x in res])
        print(a)
        a = a.reshape(-1, 7)
        res2 = ''
        s2 = ''
        for i in a:
            for j in i:
                s2 += j
            res2 += chr(int(s2, 2))
            s2 = ''
        self.ui.output.setText(res2)
        print('res: ',res2)
        


if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
