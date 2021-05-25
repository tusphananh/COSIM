from interpreter.interpreter.interpreter import Interpreter
import PyQt5.QtWidgets as qtw
class ExecuteFrame(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("COSIM-CODE AREA")
        self.resize(1000, 500)
        self.setLayout(qtw.QVBoxLayout())

        #run Button
        self.executeButtons = qtw.QWidget()
        self.executeButtons.setLayout(qtw.QVBoxLayout())
        self.runButton = qtw.QPushButton('Run')
        self.runButton.clicked.connect(self.onCicked)
        self.runButton.setMaximumWidth(100)
        self.runButton.setMaximumHeight(50)
        self.layout().addWidget(self.runButton)

        #Code area
        self.codeTextArea = qtw.QWidget()
        self.codeTextArea.setLayout(qtw.QVBoxLayout())
        self.codeArea = qtw.QPlainTextEdit()
        self.layout().addWidget(self.codeArea)

        self.show()

    def onCicked(self):
        Interpreter.run(self.codeArea.toPlainText())

if __name__=='__main__':
    app = qtw.QApplication([])
    exeFrame = ExecuteFrame()
    app.exec_()