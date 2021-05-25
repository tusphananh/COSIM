import sys

import PyQt5.QtWidgets as qtw


# Install these libs in terminal
# pip install pyqt5
# MainFrame here
from PyQt5 import QtCore

from compiler import interpreter
from compiler.interpreter import interpreter
from compiler.interpreter.interpreter.interpreter import Interpreter



class MainFrame(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.process = QtCore.QProcess(self)
        self.process.setProgram(sys.executable)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self.process.readyReadStandardError.connect(self.on_readyReadStandardError)
        self.setWindowTitle("INPUT-OUTPUT")
        self.resize(1000, 500)
        self.setLayout(qtw.QVBoxLayout())
        self.resultFrame()

    # This is the output and terminal section where print out results or error
    def resultFrame(self):
        #input output label
        self.inLabel = qtw.QLabel()
        self.inLabel.setText('Input')
        self.outLabel = qtw.QLabel()
        self.outLabel.setText('Output')
        #output text area
        self.outText = qtw.QPlainTextEdit()
        self.outText.setReadOnly(True)
        #input text line
        self.inText = qtw.QLineEdit()
        #add widget to layout
        self.layout().addWidget(self.inLabel)
        self.layout().addWidget(self.inText)
        self.layout().addWidget(self.outLabel)
        self.layout().addWidget(self.outText)
        self.inText.editingFinished.connect(self.on_editingFinished)


    @QtCore.pyqtSlot()
    def on_readyReadStandardOutput(self):
        self.outText.clear()
        out = self.process.readAllStandardOutput().data().decode()
        self.outText.insertPlainText(out)

    @QtCore.pyqtSlot()
    def on_readyReadStandardError(self):
        err = self.process.readAllStandardError().data().decode()
        self.outText.insertPlainText("\n" + err)

    @QtCore.pyqtSlot()
    def on_editingFinished(self):
        self.process.write(self.inText.text().encode() + b'\n')
        self.inText.clear()

    def runFile(self, url):
        self.process.setArguments([url])
        self.process.start()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mainFrame = MainFrame()
    mainFrame.runFile(r"C:\Users\admin\PycharmProjects\COSIM\compiler\run.py")
    mainFrame.show()
    app.exec_()
