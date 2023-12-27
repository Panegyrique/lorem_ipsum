from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication
import sys

from lib.process import Core_Lorem_Ipsum

class app(Core_Lorem_Ipsum):

    def __init__(self,maximize=False):

        self.maximize = maximize
        self.app = QCoreApplication.instance()  

        if self.app is None:
            self.app = QApplication(sys.argv)
        
        super().__init__()
        self.run()

    def run(self):

        if self.maximize:
            self.showMaximized()
        else:
            self.show()    
        
        self.app.exec_() 


if __name__ == "__main__":

    lorem_ipsum = app(False)