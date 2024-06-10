import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from ui_form import Ui_MainWindow
from analyzer import Analyzer  

imagePath = ""

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        global imagePath
        imagePath = ""
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.importButton.clicked.connect(self.import_image)
        self.ui.resetButton.clicked.connect(self.reset_ui)
        self.ui.exit.clicked.connect(self.exit_app)
        self.ui.analyzeButton.clicked.connect(self.analyze_image)

    def reset_ui(self):
        imagePath=""
        self.ui.importImage.clear()
        self.ui.analyzeImage.clear()
        self.ui.textBrowser.clear()
        self.ui.importImage.setText("")
        self.ui.analyzeImage.setText("")

    def exit_app(self):
        QApplication.instance().quit()
        
    def analyze_image(self):
        global imagePath
        analyzer = Analyzer()
        if not imagePath:
            self.ui.analyzeImage.setText("Image file path is not correct")
            return None
        imgData = analyzer.modify_image(imagePath)
        pixmap, info = analyzer.prediction(imgData)

        if pixmap:
            self.ui.analyzeImage.setPixmap(pixmap.scaled(self.ui.analyzeImage.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
            self.ui.analyzeImage.setScaledContents(True)

        self.ui.textBrowser.setText(info)

        print(imagePath)

    def import_image(self):
        global imagePath
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp *.gif *.jfif)")
        if file_path:
            imagePath = file_path
            pixmap = QPixmap(file_path)
            self.ui.importImage.setPixmap(pixmap)
            self.ui.importImage.setScaledContents(True)  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
