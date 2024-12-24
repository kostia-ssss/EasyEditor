from PyQt6 import QtCore, QtGui, QtWidgets
import os
from PIL import Image , ImageFilter , ImageQt
from style import style

workdir = None
endings = ['.png' , '.jpg' , '.jpeg' , '.jfif' , '.webp' , '.svg']

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
    
    def smoothImage(self):
        self.image = self.image.filter(ImageFilter.SMOOTH)
        self.showImage()
    
    def embossImage(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)
        self.showImage()
    
    def save_image(self):
        path = os.path.join(workdir , self.modified)
        if not os.path.isdir(path):
            os.makedirs(path)
        if ui.line.text() != "":
            path = os.path.join(path, ui.line.text()+'.jpg')
            print(path)
            self.image.save(path)
        else:
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Введіть назву зображення")

            error.exec()
    
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
        self.pushButton_2.setGeometry(QtCore.QRect(260, 590, 69, 23))
        self.pushButton_2.setObjectName("left_btn")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(329, 590, 69, 23))
        self.pushButton_3.setObjectName("right_btn")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(398, 590, 69, 23))
        self.pushButton_4.setObjectName("mirror_btn")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(467, 590, 69, 23))
        self.pushButton_5.setObjectName("rizkist_btn")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(536, 590, 69, 23))
        self.pushButton_6.setObjectName("black-white_btn")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(605, 590, 69, 23))
        self.pushButton_7.setObjectName("smooth_btn")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(674, 590, 69, 23))
        self.pushButton_8.setObjectName("emboss_btn")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(260, 613, 242, 23))
        self.save_btn.setObjectName("save_btn")
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(503, 613, 242, 23))
        self.reset_btn.setObjectName("reset_btn")
        self.line = QtWidgets.QLineEdit(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(260, 637, 484, 23))
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.open_folder)
        self.listWidget.clicked.connect(self.choose_image)
        
        app.setStyleSheet(style)
        self.SEF()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Easy Editor"))
        self.pushButton.setText(_translate("MainWindow", "Папка"))
        self.label.setText(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", "Вліво"))
        self.pushButton_3.setText(_translate("MainWindow", "Вправо"))
        self.pushButton_4.setText(_translate("MainWindow", "Дзеркало"))
        self.pushButton_5.setText(_translate("MainWindow", "Різкість"))
        self.pushButton_6.setText(_translate("MainWindow", "Ч/Б"))
        self.save_btn.setText(_translate("MainWindow", "Зберегти"))
        self.reset_btn.setText(_translate("MainWindow", "Скинути"))
        self.pushButton_7.setText(_translate("MainWindow", "Розмиття"))
        self.pushButton_8.setText(_translate("MainWindow", "Вибити"))
        self.line.setPlaceholderText(_translate("MainWindow", "Назва зображення"))
    
    def open_folder(self):
        global workdir
        self.listWidget.clear()
        workdir = QtWidgets.QFileDialog.getExistingDirectory()
        filenames = os.listdir(workdir)
        for file in filenames:
            for ending in endings:
                if file.endswith(ending):
                    self.listWidget.addItem(file)
    
    def choose_image(self):
        filename = self.listWidget.currentItem().text()
        imageeditor.filename = filename
        imageeditor.load_image()
        imageeditor.showImage()
        self.SET()
        self.pushButton_6.clicked.connect(imageeditor.bwImage)
        self.pushButton_4.clicked.connect(imageeditor.mirrorImage)
        self.pushButton_2.clicked.connect(imageeditor.leftImage)
        self.pushButton_3.clicked.connect(imageeditor.rightImage)
        self.pushButton_5.clicked.connect(imageeditor.sharpenImage)
        self.save_btn.clicked.connect(imageeditor.save_image)
        self.reset_btn.clicked.connect(imageeditor.reset)
        self.pushButton_7.clicked.connect(imageeditor.smoothImage)
        self.pushButton_8.clicked.connect(imageeditor.embossImage)

    def SET(self):
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.save_btn.setEnabled(True)
        self.reset_btn.setEnabled(True)
    
    def SEF(self):
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.save_btn.setEnabled(False)
        self.reset_btn.setEnabled(False)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())