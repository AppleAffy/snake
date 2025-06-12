
# By: <Affan.Q>
# Date: 2025-06-03
# Program Details: <Snakes & Ladders the game.>
#INTRO SCREEN
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import manager
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow
from gui.page_1_ui import Ui_MainWindow

if __name__ == "__main__":    
    manager.start()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        with manager.image_gui_path():
            self.setupUi(self)
        self.lbl_logo.setPixmap(QPixmap("images/snakes_ladders_logo.png"))
        self.setStyleSheet("background-color: rgb(255, 255, 255)")
        
    def start(self):
        if manager.screen3.dark == True:
            self.setStyleSheet("background-color: rgb(128, 128, 128)")
        elif manager.screen3.dark == False:
            self.setStyleSheet("background-color: rgb(255, 255, 255)")
            
    def btn_play_a(self):
        manager.widget.setCurrentWidget(manager.screen2)
        manager.screen2.start()
    
    def btn_quit_a(self):
        sys.exit()
    def btn_settings_a(self):
        manager.widget.setCurrentWidget(manager.screen3)