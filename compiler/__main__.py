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
        self.setWindowTitle("COSIM")
        self.resize(1000, 500)
        self.setLayout(qtw.QVBoxLayout())
        self.executeFrame()
        self.codeFrame()
        self.resultFrame()

    # Execute Frame where contains the execute or debug features.
    def executeFrame(self):
        self.executeButtons = qtw.QWidget()
        self.executeButtons.setLayout(qtw.QVBoxLayout())
        self.runButton = qtw.QPushButton('Run')
        self.runButton.clicked.connect(self.onCicked)
        self.runButton.setMaximumWidth(100)
        self.runButton.setMaximumHeight(50)
        self.layout().addWidget(self.runButton)

    # This is coding Frame used to code our Language
    def codeFrame(self):
        self.codeTextArea = qtw.QWidget()
        self.codeTextArea.setLayout(qtw.QVBoxLayout())
        self.codeArea = qtw.QPlainTextEdit()
        self.layout().addWidget(self.codeArea)

    # This is the output and terminal section where print out results or error
    def resultFrame(self):
        self.outText = qtw.QPlainTextEdit()
        self.outText.setReadOnly(True)
        self.inText = qtw.QLineEdit()
        self.layout().addWidget(self.inText)
        self.layout().addWidget(self.outText)
        self.inText.editingFinished.connect(self.on_editingFinished)



    def onCicked(self):
        self.outText.clear()
        code= self.codeArea.toPlainText()
        self.process.start()

    @QtCore.pyqtSlot()
    def on_readyReadStandardOutput(self):
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


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mainFrame = MainFrame()
    mainFrame.runFile(r"C:\Users\admin\PycharmProjects\COSIM\compiler\run.py")
    mainFrame.show()
    app.exec_()
