from PyQt6 import QtCore, QtGui, QtWidgets
import os
from PIL import Image , ImageFilter , ImageQt

workdir = None

class ImageEditor:
    def __init__(self, filename):
        self.image = None
        self.filename = filename
        self.modified = "modified"
        self.original = None
        self.number = 1

    def load_image(self):
        path = os.path.join(workdir , self.filename)
        print(path)
        self.original = Image.open(path)
        self.image = self.original
    
    def showImage(self):
        ui.label.hide()
        #path = os.path.join(workdir , path)
        imageqt = ImageQt.ImageQt(self.image)
        pixmap = QtGui.QPixmap.fromImage(imageqt)
        w, h = ui.label.width(), ui.label.height()
        pixmap = pixmap.scaled(w, h, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        ui.label.setPixmap(pixmap)
        ui.label.show()
    
    def bwImage(self):
        self.image = self.image.convert("L")
        self.showImage()
    
    def mirrorImage(self):
        self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
        self.showImage()
    
    def leftImage(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.showImage()
    
    def rightImage(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.showImage()
    
    def sharpenImage(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.showImage()
    
    def save_image(self):
        path = os.path.join(workdir , self.modified)
        if not os.path.isdir(path):
            os.makedirs(path)
        path = os.path.join(path, str(self.number)+self.filename)
        self.image.save(path)
        self.number += 1
    
    def reset(self):
        self.image = self.original
        self.showImage()

imageeditor = ImageEditor("")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        MainWindow.setMinimumSize(QtCore.QSize(800, 700))
        MainWindow.setMaximumSize(QtCore.QSize(800, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.pushButton.setObjectName("foder_btn")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 201, 601))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 511, 481))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 590, 75, 23))
        self.pushButton_2.setObjectName("left_btn")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 590, 75, 23))
        self.pushButton_3.setObjectName("right_btn")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 590, 75, 23))
        self.pushButton_4.setObjectName("mirror_btn")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 590, 75, 23))
        self.pushButton_5.setObjectName("rizkist_btn")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(670, 590, 75, 23))
        self.pushButton_6.setObjectName("black-white_btn")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(260, 650, 242, 23))
        self.save_btn.setObjectName("save_btn")
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(503, 650, 242, 23))
        self.reset_btn.setObjectName("reset_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.open_folder)
        self.listWidget.clicked.connect(self.choose_image)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Папка"))
        self.label.setText(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", "Вліво"))
        self.pushButton_3.setText(_translate("MainWindow", "Вправо"))
        self.pushButton_4.setText(_translate("MainWindow", "Дзеркало"))
        self.pushButton_5.setText(_translate("MainWindow", "Різкість"))
        self.pushButton_6.setText(_translate("MainWindow", "Ч/Б"))
        self.save_btn.setText(_translate("MainWindow", "Зберегти"))
        self.reset_btn.setText(_translate("MainWindow", "Скинути"))
    
    def open_folder(self):
        global workdir
        self.listWidget.clear()
        workdir = QtWidgets.QFileDialog.getExistingDirectory()
        filenames = os.listdir(workdir)
        for file in filenames:
            if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.jfif'):
                self.listWidget.addItem(file)
    
    def choose_image(self):
        filename = self.listWidget.currentItem().text()
        imageeditor.filename = filename
        imageeditor.load_image()
        imageeditor.showImage()
        self.pushButton_6.clicked.connect(imageeditor.bwImage)
        self.pushButton_4.clicked.connect(imageeditor.mirrorImage)
        self.pushButton_2.clicked.connect(imageeditor.leftImage)
        self.pushButton_3.clicked.connect(imageeditor.rightImage)
        self.pushButton_5.clicked.connect(imageeditor.sharpenImage)
        self.save_btn.clicked.connect(imageeditor.save_image)
        self.reset_btn.clicked.connect(imageeditor.reset)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())