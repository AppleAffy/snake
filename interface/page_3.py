# SETTINGS



import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import manager
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow
from gui.page_3_ui import Ui_MainWindow

if __name__ == "__main__":    
    manager.start()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        with manager.image_gui_path():
            self.setupUi(self)
            self.dark = False
            
        
    def btn_return_a(self):
        manager.widget.setCurrentWidget(manager.screen1)
        if self.chk_dark.isChecked():
            self.dark = True
        elif self.chk_dark.isChecked() == False:
            self.dark = False
        manager.screen1.start()
        
    def btn_color(self):
        self.color = (self.sender().objectName()[4:])
        print(self.color)
        
    def debug(self):
        manager.screen2.debug()