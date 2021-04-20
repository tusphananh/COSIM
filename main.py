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

    # Execute Frame where contains the execute or debug features.
    def executeFrame(self):
        executeButtons = qtw.QWidget()
        executeButtons.setLayout(qtw.QVBoxLayout())
        runButton = qtw.QPushButton('Run')
        runButton.setMaximumWidth(100)
        runButton.setMaximumHeight(50)
        self.layout().addWidget(runButton)

    # This is coding Frame used to code our Language
    def codeFrame(self):
        codeTextArea = qtw.QWidget()
        codeTextArea.setLayout(qtw.QVBoxLayout())
        codeArea = qtw.QPlainTextEdit()
        self.layout().addWidget(codeArea)

    # This is the output and terminal section where print out results or error
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
