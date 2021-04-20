import PyQt5.QtWidgets as qtw


# Install these libs in terminal
# pip install pyqt5
# MainFrame here
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

    def executeFrame(self):
        executeButtons = qtw.QWidget()
        executeButtons.setLayout(qtw.QVBoxLayout())
        runButton = qtw.QPushButton('Run')
        runButton.setMaximumWidth(100)
        runButton.setMaximumHeight(50)
        self.layout().addWidget(runButton)

    def codeFrame(self):
        codeTextArea = qtw.QWidget()
        codeTextArea.setLayout(qtw.QVBoxLayout())
        codeArea = qtw.QPlainTextEdit()
        self.layout().addWidget(codeArea)

    def resultFrame(self):
        terminal = qtw.QLabel("Terminal")
        output = qtw.QLabel("Output")
        tabwidget = qtw.QTabWidget()
        tabwidget.addTab(terminal, "Terminal")
        tabwidget.addTab(output, "Output")
        self.layout().addWidget(tabwidget)


if __name__ == '__main__':
    app = qtw.QApplication([])
    mainFrame = MainFrame()
    app.exec_()
