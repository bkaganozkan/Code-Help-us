import sys
from PyQt5.QtGui import QPainter, QColor, QSyntaxHighlighter, QTextCharFormat
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip, QWidget,QLabel
from PyQt5.QtWidgets import QFileDialog, QTextEdit,QPlainTextEdit
from PyQt5.QtCore import Qt, pyqtSignal
from highlighter import Highlighter


#                   SubWindow Class

class Widget(QTextEdit):
    def __init__(self, left, top, width, height, parent=None):
        super().__init__(parent)

        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.setParent(parent)
        self.initWidget()

        self.highLighter = Highlighter(self.document())
     #    self.setStyleSheet("""QTextEdit{
	# font-family:'Consolas';
	# color: #ccc;
	# background-color: #2b2b2b;}""")

    def initWidget(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


    def setText(self, text):
        super().setText(text)



    #                   Main Program Window

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.Wid = Widget(25, 25, 400, 450, self)
        self.Wid1 = Widget(450, 25, 400, 450, self)

        self.first_path_label = QLabel(self)
        self.first_path_label.setWordWrap(True)
        self.second_path_label = QLabel(self)
        self.second_path_label.setWordWrap(True)

        self.title = "PyQt 5 Application"
        self.left = 100
        self.top = 100
        self.width = 1024
        self.height = 500
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #    First OpenFile Button
        openFileButton_1 = QPushButton("First File", self)
        openFileButton_1.setGeometry(860, 75, 75, 25)
        openFileButton_1.clicked.connect(self.buttonClick)

        self.first_path_label.setGeometry(860,105,125,25)

        # Second OpenFile Button
        openFileButton_2 = QPushButton("Second File", self)
        openFileButton_2.setGeometry(860, 150, 75, 25)
        openFileButton_2.clicked.connect(self.buttonClick_1)

        self.second_path_label.setGeometry(860,180,125,25)

        # Save Button
        saveButton = QPushButton("Save", self)
        saveButton.setGeometry(900, 450, 75, 25)


        self.show()

    def buttonClick(self):
        data,path = self.openFile()
        self.first_path_label.setText(path)
        self.Wid.setText(data)
        # print(self.Wid.getText())


    def buttonClick_1(self):
        data,path = self.openFile()
        self.second_path_label.setText(path)
        self.Wid1.setText(data)



    def openFile(self):
        fileName = QFileDialog.getOpenFileName(self, "Open File")
        if fileName[0]:

            f = open(fileName[0], 'r')

            with f:
                data = f.read()
            path = fileName[0]
        else:
            data = "Sie uzağa git karşim"
            path = "None"

        return data,path



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
