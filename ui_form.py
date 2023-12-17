# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QDir)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget,QFileDialog)
from panorama import Panaroma
import imutils
import cv2
class Ui_MainWindow(object):
    def __init__(self):
        self.image_file_paths = []
        self.images = []
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"PROJECT DIP")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 130, 101, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 101, 101))
        self.label.setStyleSheet(u"background-color: rgb(61, 64, 255)")
        self.label.setScaledContents(True)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(30, 220, 171, 71))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(280, 170, 411, 301))
        self.label_6.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.label_6.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 20, 101, 101))
        self.label_2.setStyleSheet(u"background-color: rgb(61, 64, 255)")
        self.label_2.setScaledContents(True)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(150, 130, 101, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 20, 101, 101))
        self.label_3.setStyleSheet(u"background-color: rgb(61, 64, 255)")
        self.label_3.setScaledContents(True)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(280, 130, 101, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(420, 20, 101, 101))
        self.label_4.setStyleSheet(u"background-color: rgb(61, 64, 255)")
        self.label_4.setScaledContents(True)
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(420, 130, 101, 21))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(570, 20, 101, 101))
        self.label_5.setStyleSheet(u"background-color: rgb(61, 64, 255)")
        self.label_5.setScaledContents(True)
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(570, 130, 101, 21))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 310, 171, 71))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 17))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #upload image buttons
        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(lambda: self.open_file_dialog(MainWindow,self.label))
        self.pushButton_4.clicked.connect(lambda: self.open_file_dialog(MainWindow,self.label_2))
        self.pushButton_5.clicked.connect(lambda: self.open_file_dialog(MainWindow,self.label_3))
        self.pushButton_7.clicked.connect(lambda: self.open_file_dialog(MainWindow,self.label_4))
        self.pushButton_8.clicked.connect(lambda: self.open_file_dialog(MainWindow,self.label_5))
        # generate image button
        self.pushButton_6.clicked.connect(lambda: self.upload_generate_image(MainWindow,self.generate_panorama_image(MainWindow)))
        self.pushButton.clicked.connect(self.clear_images)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Upload image 1", None))
        self.label.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Generate image", None))
        self.label_6.setText("")
        self.label_2.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Upload image 2", None))
        self.label_3.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Upload image 3", None))
        self.label_4.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Upload image 4", None))
        self.label_5.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Upload image 5", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear Image", None))
    # retranslateUi

    def open_file_dialog(self, MainWindow,label):
            file_path, _ = QFileDialog.getOpenFileName(MainWindow, "Open Image File", QDir.homePath())
            if file_path:
                pixmap = QPixmap(file_path)
                label.setPixmap(pixmap)
                label.repaint()
                self.statusbar.showMessage(f"Selected Image: {file_path}")
                self.image_file_paths.append(file_path)
    def generate_panorama_image(self,MainWindow):
        number_of_images=len(self.image_file_paths)
        images=[]
        for file_path in self.image_file_paths:
            image = cv2.imread(file_path)
            image = imutils.resize(image, width=600)
            image = imutils.resize(image, height=600)
            images.append(image)
        panaroma=Panaroma()
        if number_of_images < 2:
            self.statusbar.showMessage("Please upload at least two images for panorama generation.")
            return None  
        if number_of_images==2:
            (result, matched_points) = panaroma.image_stitch([images[0], images[1]], match_status=True)
        else:
            (result,matched_points)= panaroma.image_stitch([images[number_of_images-2],images[number_of_images-1]], match_status=True)
            for i in range(number_of_images-2):
                (result, matched_points) = panaroma.image_stitch([images[number_of_images-i-3],result], match_status=True)
        return result 
    
    def upload_generate_image(self,MainWindow,image):
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setPixmap(pixmap.scaled(self.label_6.size(), Qt.KeepAspectRatio))
        self.label_6.repaint()
    def clear_images(self):
        self.images.clear()
        self.image_file_paths.clear()
        self.label.clear()
        self.label_2.clear()
        self.label_3.clear()
        self.label_4.clear()
        self.label_5.clear()
        self.label_6.clear()   