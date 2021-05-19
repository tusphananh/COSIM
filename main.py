import PyQt5.QtWidgets as qtw


# Install these libs in terminal
# pip install pyqt5
# MainFrame here
from compiler import interpreter
from compiler.interpreter import interpreter
from compiler.interpreter.interpreter.interpreter import Interpreter



class MainFrame(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("COSIM")
        self.resize(1000, 500)
        self.setLayout(qtw.QVBoxLayout())
        self.executeFrame()
        self.codeFrame()
        self.resultFrame()

        self.show()

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
        self.terminal = qtw.QLabel("Terminal")
        self.output = qtw.QLabel("Output")
        self.tabwidget = qtw.QTabWidget()
        self.tabwidget.addTab(self.terminal, "Terminal")
        self.tabwidget.addTab(self.output, "Output")
        self.layout().addWidget(self.tabwidget)

    def onCicked(self):
        Interpreter.run(self.codeArea.toPlainText())
        #self.output.setText(self.codeArea.toPlainText())


if __name__ == '__main__':
    app = qtw.QApplication([])
    mainFrame = MainFrame()
    app.exec_()
