# GAME

from PySide6.QtCore import QTimer
import random
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import manager
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow
from gui.page_2_ui import Ui_MainWindow

if __name__ == "__main__":    
    manager.start()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        with manager.image_gui_path():
            self.setupUi(self)    
        self.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.timer=QTimer()
        self.timer.timeout.connect(self.do_stuff)
        self. roll = False # rolling function of dice
        self.turn = True #decided [player turn vs AI turn]
        self.backwards = False #move backwards after going up a level
        self.roll_values = 1 #all previos rolls added up to calculate the spot it shoudl be on. 1 is initial spot its on.
        self.moving_up = False
        #-----------------------------DEBUG---------------------------------
        self.debug_roll = False
        

        
    
    
    def start(self):
        
        #----------------------------SETTINGS--------------------------------
        if manager.screen3.dark == True:
            self.setStyleSheet("background-color: rgb(128, 128, 128)")
        elif manager.screen3.dark == False:
            self.setStyleSheet("background-color: rgb(255, 255, 255)")
        try:
            if manager.screen3.color == "red":
                self.lbl_player.setPixmap(QPixmap("images/pieces_red.png"))
                
            elif manager.screen3.color == "yellow":
                self.lbl_player.setPixmap(QPixmap("images/pieces_yellow.png"))
            elif manager.screen3.color == "pink":
                self.lbl_player.setPixmap(QPixmap("images/pieces_pink.png"))
            elif manager.screen3.color == "green":
                self.lbl_player.setPixmap(QPixmap("images/pieces_green.png"))
            elif manager.screen3.color == "black":
                self.lbl_player.setPixmap(QPixmap("images/pieces_black.png"))
        except:
            self.lbl_player.setPixmap(QPixmap("images/pieces_red.png"))
        #---------------------------------------------------------------------
    
    def btn_reset_a(self):
        self.lbl_player.move(30,500) # 30, 500 is default position
        self.roll_values = 1
        self.backwards = False
        self.moving_up = False
        
    def line_move(self):
        if self.roll_values == 65:
            self.lbl_player.move(540, 335)
            self.roll_values = 34
        if self.roll_values == 3 and self.lbl_player.y() == 500:
            self.lbl_player.move(200,170)
            self.roll_values = 78
        if self.roll_values > 10 and self.lbl_player.y() == 500:
            self.moving_up = True
            self.lbl_player.move(800, 445)
            self.backwards = True
            move_x = int(self.roll_values - 11) * -85
            move_y = 0
            self.lbl_player.move(self.lbl_player.x()+move_x,self.lbl_player.y()+move_y)
            self.moving_up = True
        elif self.roll_values > 20 and self.lbl_player.y() == 445:
            self.moving_up = True
            self.lbl_player.move(30, 390)
            self.backwards = False
            move_x = int(self.roll_values - 21) * 85
            move_y = 0
            self.lbl_player.move(self.lbl_player.x()+move_x,self.lbl_player.y()+move_y)
            self.moving_up = True
        elif self.roll_values > 30 and self.lbl_player.y() == 390:
            self.moving_up = True
            self.lbl_player.move(800, 335)
            self.backwards = True
            move_x = int(self.roll_values - 31) * -85
            move_y = 0
            self.lbl_player.move(self.lbl_player.x()+move_x,self.lbl_player.y()+move_y)
            self.moving_up = True
        elif self.roll_values > 40 and self.lbl_player.y() == 335:
            self.moving_up = True
            self.lbl_player.move(30, 280)
            self.backwards = False
            move_x = int(self.roll_values - 41) * 85
            move_y = 0
            self.lbl_player.move(self.lbl_player.x()+move_x,self.lbl_player.y()+move_y)
            self.moving_up = True 
        elif self.roll_values > 50 and self.lbl_player.y() == 280:
            self.moving_up = True
            self.lbl_player.move(800, 225)
            self.backwards = True
            move_x = int(self.roll_values - 51) * -85
            move_y = 0
            self.lbl_player.move(self.lbl_player.x()+move_x,self.lbl_player.y()+move_y)
            self.moving_up = True
        elif self.roll_values > 60 and self.lbl_player.y() == 225:
            self.moving_up = True
            self.lbl_player.move(30, 170)
            self.backwards = False
            move_x = int(self.roll_values - 61) * 85
            move_y = 0
            self.lbl_player.move(self.lbl_player.x()+move_x,self.lbl_player.y()+move_y)
            self.moving_up = True
        elif self.roll_values > 70 and self.lbl_player.y() == 170:
            self.moving_up = True
            self.lbl_player.move(800, 115)
            self.backwards = True
            move_x = int(self.roll_values - 71) * -85
            move_y = 0
            self.lbl_player.move(self.lbl_player.x()+move_x,self.lbl_player.y()+move_y)
            self.moving_up = True
        elif self.roll_values > 80 and self.lbl_player.y() == 115:
            self.moving_up = True
            self.lbl_player.move(30, 60)
            self.backwards = False
            move_x = int(self.roll_values - 81) * 85
            move_y = 0
            self.lbl_player.move(self.lbl_player.x()+move_x,self.lbl_player.y()+move_y)
            self.moving_up = True
        elif self.roll_values > 90 and self.lbl_player.y() == 60:
            self.moving_up = True
            self.lbl_player.move(800, 5)
            self.backwards = True
            move_x = int(self.roll_values - 91) * -85
            move_y = 0
            self.lbl_player.move(self.lbl_player.x()+move_x,self.lbl_player.y()+move_y)
            self.moving_up = True      
    def btn_dice_a(self): 
        self.moving_up = False
        if self.turn:
            self.roll = not self.roll # toggle boolean value
            if self.roll == True:
                self.timer.start(50)
            elif self.roll == False:
                self.timer.stop()
                if self.debug_roll == True:
                    print(self.move)
                self.roll_values += self.move
                if self.debug_roll == True:
                    print(f"roll value = {self.roll_values}")
                    print(f"You Got {self.move}")
                self.line_move()
                if self.moving_up == False:
                    self.move_piece()
            
                
        elif self.turn == False:
            pass # AI TURN
        else:
            print("ERROR in self.turn")
            
        
    def move_piece(self,):
        if self.backwards == True:
            if self.debug_roll == True:
                print("False")
                print("MOVING BACKWARDS") # checking
            move_x = int(self.move) * -85
            move_y = 0
            self.lbl_player.move(self.lbl_player.x()+move_x,self.lbl_player.y()+move_y)
        elif self.backwards == False:
            if self.debug_roll == True:
                print("MOVING FORWARDS")
            move_x = int(self.move) * 85
            move_y = 0
            self.lbl_player.move(self.lbl_player.x()+move_x,self.lbl_player.y()+move_y)
        
        
    def do_stuff(self):
        self.move = random.randint(1,6)
        self.lbl_dice_show.setText(str(self.move))
        if self.debug_roll == True:
            print(self.move)
        

    def btn_return_a(self):
        manager.widget.setCurrentWidget(manager.screen1)
        
        
    def debug(self):  #------------------------DEBUG-----------------------------
        request = input("Command: ")
        if request == "position":
            self.roll_values = int(input("roll_values(one number): "))
            temp_x = int(input("X: "))
            temp_y = int(input("Y: "))
            self.lbl_player.move(temp_x, temp_y)
        elif request == "pos?":
            print(f"lbl_player position is ({self.lbl_player.x()},{self.lbl_player.y()}) ")
        elif request == "debug":
            self.debug_roll = not self.debug_roll
            print(f"debug_roll is {self.debug_roll}")
        elif request == "help":
            print("List of Commands:\n pos? - provides self.lbl_player x and y location values\n debug_roll - toggle show dice rolls and output of roll as well as other debug info\n position - lets you set the position of the piece")
        else:
            print("THAT IS NOT A VALID COMMAND: TYPE 'help' TO SEE LIST OF COMMANDS")