import os
import sys
from tkinter import Label
from PyQt5.QtWidgets import (QApplication, QWidget,
QPushButton, QGridLayout, QLabel, QLineEdit,QMessageBox)
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

class Create_Account(QWidget):
    switch_window = QtCore.pyqtSignal()
    
    

    def __init__(self,i):
        QWidget.__init__(self)
        self.setWindowTitle('Create Account '+str(i))
        self.resize(500,120)

        layout = QGridLayout()
        
        label_name= QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)
		
        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password= QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_create = QPushButton('Create Account')
        button_create.clicked.connect(self.add_account)
        layout.addWidget(button_create, 2, 0, 1, 2)
        layout.setRowMinimumHeight (2,75)

        self.setLayout(layout)
    
    def add_account(self):
        msg= QMessageBox()
        print(self.lineEdit_password,self.lineEdit_username)
        name = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        file1 = open("credentials.txt", "r")
        flag = 0
        index = 0
        for line in file1:  
            if "("+name+" ," in line:
                flag = 1
                break 
        file1.close()
        if flag == 1: 
            msg.setText('Username Already exists')
            msg.exec_()
        else: 
            file1 = open("credentials.txt", "a")
            file1.write("\n("+name+" , "+password+")" )
            file1.close()
            self.switch_window.emit()
            msg.setText('Success')
            msg.exec() 
             
        

class Login(QWidget):

    switch_window = QtCore.pyqtSignal()
    switch_create = QtCore.pyqtSignal()
    

    def __init__(self,i):
        QWidget.__init__(self)
        self.setWindowTitle('Login User '+str(i))
        self.resize(500,120)

        layout = QGridLayout()
        
        label_name= QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)
		
        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password= QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight (2,75)

        button_create = QPushButton('Create Account')
        button_create.clicked.connect(self.create)
        layout.addWidget(button_create, 3, 0)

        self.setLayout(layout)
    
    def create(self):
        self.switch_create.emit()
    
    def check_password(self):
        msg= QMessageBox()
        print(self.lineEdit_password,self.lineEdit_username)
        name = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        file1 = open("credentials.txt", "r")
        flag = 0
        index = 0
        for line in file1:  
            if "("+name+" ," in line:
                flag = 1
                break 
        if flag == 0: 
            msg.setText('Incorrect Username')
            msg.exec_()
        elif "("+name+" , "+password+")" in line:  
            self.switch_window.emit()
            msg.setText('Success')
            msg.exec() 
            file1.close() 
        else:
            msg.setText('Incorrect Password')
            msg.exec_()
        



class Controller:

    def __init__(self):
        self.login = Login(1)
        self.create = Create_Account(1)
        self.login_2 = Login(2)
        

    def show_login(self):
        self.login = Login(1)
        self.login.switch_window.connect(self.show_login_2)
        self.login.switch_create.connect(self.show_create_account)
        self.login.show()
        self.create.close()

    def show_create_account(self):
        self.create = Create_Account(1)
        self.create.switch_window.connect(self.login.show)
        self.create.show()
        self.login.close()
        self.login_2.close()

    
    def show_login_2(self):
        self.login_2 = Login(2)
        self.login_2.switch_window.connect(self.show_tictactoe)
        self.login_2.switch_create.connect(self.show_create_account)
        self.login_2.show()
        self.create.close()
        self.login.close()

    def show_tictactoe(self):
        self.tictactoe = TicTacToe()
        self.login_2.close()
        self.tictactoe.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())  