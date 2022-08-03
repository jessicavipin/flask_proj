import os
import sys
from tkinter import Label
from PyQt5.QtWidgets import (QApplication, QWidget,
QPushButton, QGridLayout, QLabel)
from PyQt5 import QtCore

class TicTacToe(QWidget):

    def __init__(self):
        super().__init__()
        self.button= [] #contains all the buttons which were clicked
        self.play="X" #previous player's name
        self.count=9 #Number of empty buttons

        #Making an empty grid of buttons 
        grid = QGridLayout()  
        self.setLayout(grid)
        names = [" "]*9 
        positions = [(i, j) for i in range(3) for j in range(3)]
        k=-1
        for position, name in zip(positions, names):
            k=k+1
            button = QPushButton(name,self)
            self.button.append(button)
            button.clicked.connect(lambda _, kay=k: self.on_click(kay))
            grid.addWidget(button, *position)
        
        clear = QPushButton("Clear",self)
        grid.addWidget(clear,4,0)
        clear.clicked.connect(restart)

        self.move(300, 150)
        self.setWindowTitle('Tic Tac Toe')  
        self.show()

    #display the player name on the button
    def on_click(self,k):
        if self.button[k].text()==" ":
            self.count=self.count-1 #reducing the number of available buttons
            if self.play=="X" :
                self.button[k].setText("O")
                self.play="O"
            else:
                self.button[k].setText("X")
                self.play="X"
        self.check(k)

    #checking if the game has to end
    def check(self,k):
        #checking the row
        l=(k//3)*3
        if (self.button[l].text()==self.button[l+1].text()) and (self.button[l].text()==self.button[l+2].text()):
            self.end(self.play)
            return
        #checking the column
        if (self.button[(k+3)%9].text()==self.button[k].text()) and (self.button[k].text()==self.button[(k+6)%9].text()):
            self.end(self.play)
            return
        #checking the diagonals
        if k%2==0 and self.button[4].text()!=" ":
            if (self.button[2].text()==self.button[4].text()) and (self.button[2].text()==self.button[6].text()):
                self.end(self.play)
                return
            if (self.button[0].text()==self.button[4].text()) and (self.button[4].text()==self.button[8].text()):
                self.end(self.play)
                return
        #checking if its a draw
        if self.count==0:
            self.end("Draw")
        return

    #giving the result 
    def end(self,winner):
        for i in range(1,9):
            self.button[i].hide()
        if winner=="Draw":
            self.button[0].setText("~~~   Nobody Wins   ~~~ ")
        else:
            self.button[0].setText(winner +" wins!!!!")
    
        
    
#clear button 
def restart():
        QtCore.QCoreApplication.quit()
        status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
        print(status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TicTacToe()
    sys.exit(app.exec_())  