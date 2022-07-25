import os
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
QPushButton, QGridLayout)

class Example(QWidget):

    def __init__(self):
        super().__init__()
        grid = QGridLayout()  
        self.setLayout(grid)
        self.button= []
        self.play="X"

        names = [" "]*9

        positions = [(i, j) for i in range(3) for j in range(3)]
        k=-1

        for position, name in zip(positions, names):
            k=k+1
            button = QPushButton(name,self)
            self.button.append(button)
            

            button.clicked.connect(lambda _, kay=k: self.on_click(kay))
            # print(k, fn())
            grid.addWidget(button, *position)
        print(grid.itemAtPosition(0,0))
        self.move(300, 150)
        self.setWindowTitle('PyQt window')  
        self.show()

    # def create_on_click_fn(pos):
    #     return lambda x: _onclick(x, pos)

    def on_click(self,k):
        print(k)
        if self.button[k].text()==" ":
            if self.play=="X" :
                self.button[k].setText("O")
                self.play="O"
            else:
                self.button[k].setText("X")
                self.play="X"
        l=(k//3)*3
        if (self.button[l].text()==self.button[l+1].text()) and (self.button[l].text()==self.button[l+2].text()):
            self.end(self.play)
            print(1)
            return
        if (self.button[(k+3)%9].text()==self.button[k].text()) and (self.button[k].text()==self.button[(k+6)%9].text()):
            self.end(self.play)
            print(2)
            return
        if k%2==0 and self.button[4].text()!=" ":
            if (self.button[2].text()==self.button[4].text()) and (self.button[2].text()==self.button[6].text()):
                self.end(self.play)
                print(3)
                return
            if (self.button[0].text()==self.button[4].text()) and (self.button[4].text()==self.button[8].text()):
                self.end(self.play)
                print(4)
                return
        return

    def end(self,winner):
        for i in range(1,9):
            self.button[i].hide()
        self.button[0].setText(winner +" wins!!!!")
        #self.button[1].clicked.connect(self.restart())
    
    #def restart(self):

        #os.execl(sys.executable, sys.executable, *sys.argv)
    

        

    # def _onclick(button, var):
    #     button.hide()
    #     return var



    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())  