from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1158, 657)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 40, 331, 531))
        self.importButton = QPushButton(self.groupBox)
        self.importButton.setObjectName(u"importButton")
        self.importButton.setGeometry(QRect(20, 40, 281, 71))
        self.analyzeButton = QPushButton(self.groupBox)
        self.analyzeButton.setObjectName(u"analyzeButton")
        self.analyzeButton.setGeometry(QRect(20, 120, 281, 71))
        self.resetButton = QPushButton(self.groupBox)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setGeometry(QRect(20, 200, 281, 71))
        self.exit = QPushButton(self.groupBox)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(20, 280, 281, 71))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(370, 40, 751, 331))
        self.importImage = QLabel(self.groupBox_2)
        self.importImage.setObjectName(u"importImage")
        self.importImage.setGeometry(QRect(20, 30, 321, 291))
        self.analyzeImage = QLabel(self.groupBox_2)
        self.analyzeImage.setObjectName(u"analyzeImage")
        self.analyzeImage.setGeometry(QRect(380, 30, 351, 291))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(370, 390, 751, 181))
        self.textBrowser = QTextBrowser(self.groupBox_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 30, 731, 141))
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(20, 10, 1101, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1158, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.importButton.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.analyzeButton.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.groupBox_2.setTitle("")
        self.importImage.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.analyzeImage.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.groupBox_3.setTitle("")
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Fruit Classification", None))
    # retranslateUi

