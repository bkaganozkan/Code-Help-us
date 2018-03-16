from PyQt5 import QtWidgets
import high

app = QtWidgets.QApplication([])
editor = QtWidgets.QPlainTextEdit()
editor.setStyleSheet("""QPlainTextEdit{
	font-family:'Consolas';
	color: #ccc;
	background-color: #2b2b2b;}""")
highlight = high.PythonHighlighter(editor.document())
editor.show()

# Load syntax.py into the editor for demo purposes
infile = open('test1.txt', 'r')
editor.setPlainText(infile.read())

app.exec_()
