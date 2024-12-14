from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PIL import Image , ImageFilter

workdir = None

class ImageEditor:
    def __init__(self, filename):
        self.image = None
        self.filename = filename
        self.modified = "modified"

    def load_image(self):
        path = os.path.join(workdir , self.filename)
        self.image = Image.open(path)
    
    def showImage(self , path):
        ui.label.hide()
        #path = os.path.join(workdir , path)
        pixmap = QtGui.QPixmap(path)
        w, h = ui.label.width(), ui.label.height()
        pixmap = pixmap.scaled(w, h, QtCore.Qt.KeepAspectRatio)
        ui.label.setPixmap(pixmap)
        ui.label.show()
    
    def bwImage(self):
        global workdir
        if not os.path.isdir(os.path.join(workdir , self.modified)):
            os.makedirs(os.path.join(workdir , self.modified))
        path = os.path.join(os.path.join(workdir , self.modified , "bw.jpg"))
        print(path)
        bw = self.image.convert("L")
        self.save_image(bw , path)
        self.showImage(path)
    
    def mirrorImage(self):
        global workdir
        if not os.path.isdir(os.path.join(workdir , self.modified)):
            os.makedirs(os.path.join(workdir , self.modified))
        path = os.path.join(os.path.join(workdir , self.modified , "mirror.jpg"))
        print(path)
        mirror = self.image.transpose(Image.FLIP_TOP_BOTTOM)
        self.save_image(mirror , path)
        self.showImage(path)
    
    def save_image(self , image , path):
        image.save(path)

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
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 111, 31))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.open_folder)
        self.listWidget.clicked.connect(self.choose_image)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Папка"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "Вліво"))
        self.pushButton_3.setText(_translate("MainWindow", "Вправо"))
        self.pushButton_4.setText(_translate("MainWindow", "Дзеркало"))
        self.pushButton_5.setText(_translate("MainWindow", "Різкість"))
        self.pushButton_6.setText(_translate("MainWindow", "Ч/Б"))
    
    def open_folder(self):
        global workdir
        self.listWidget.clear()
        workdir = QtWidgets.QFileDialog.getExistingDirectory()
        filenames = os.listdir(workdir)
        for file in filenames:
            if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.jfif'):
                self.listWidget.addItem(file)
    
    def choose_image(self):
        global imageeditor , workdir
        filename = self.listWidget.currentItem().text()
        path = os.path.join(workdir , filename)
        imageeditor = ImageEditor(filename)
        imageeditor.load_image()
        imageeditor.showImage(path)
        self.pushButton_6.clicked.connect(imageeditor.bwImage)
        self.pushButton_4.clicked.connect(imageeditor.mirrorImage)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())