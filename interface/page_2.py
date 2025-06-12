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
        self. roll = False
        self.turn = True
        self.backwards = False
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
            
    def btn_dice_a(self): 
        if self.turn:
            self.roll = not self.roll # toggle boolean value
            if self.roll == True:
                self.timer.start(50)
            elif self.roll == False:
                self.timer.stop()
                if self.debug_roll == True:
                    print(f"You Got {self.move}")
                if self.lbl_player.x() >= 795:
                    move_y += 90
                    move_x += 200
                    move_x = int(self.move) * -85 
                move_x = int(self.move) * 85
                move_y = 0
       
                self.lbl_player.move(self.lbl_player.x()+move_x,self.lbl_player.y()+move_y)
            else:
                print("ERROR in self.roll (boolean)")
                
        elif self.turn == False:
            pass # AI TURN
        else:
            print("ERRORS in self.turn")
            
        
    
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
            print(f"lbl_player position is ({self.lbl_player.x()},{self.lbl_player.y()}) ")
        elif request == "debug_roll":
            self.debug_roll = not self.debug_roll
            print(f"debug_roll is {self.debug_roll}")
        elif request == "help":
            print("List of Commands:\n position - provides self.lbl_player x location vlaue\n debug_roll - toggle show dice rolls and output of roll")
        else:
            print("THAT IS NOT A VALID COMMAND: TYPE 'help' TO SEE LIST OF COMMANDS")