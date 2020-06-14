# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designGUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

# default
import sys
from PyQt5 import QtCore, QtWidgets

# dari tutorial
from PyQt5.QtWidgets import (QFileDialog)
from PyQt5.QtGui import QPixmap, QImage

# kodingan sendiri
import cv2
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gBox_rightButton = QtWidgets.QGroupBox(self.centralwidget)
        self.gBox_rightButton.setGeometry(QtCore.QRect(610, 60, 111, 261))
        self.gBox_rightButton.setTitle("")
        self.gBox_rightButton.setObjectName("gBox_rightButton")
        self.pBtn_save = QtWidgets.QPushButton(self.gBox_rightButton)
        self.pBtn_save.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.pBtn_save.setObjectName("pBtn_save")
        self.pBtn_getRGB = QtWidgets.QPushButton(self.gBox_rightButton)
        self.pBtn_getRGB.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.pBtn_getRGB.setObjectName("pBtn_getRGB")
        self.pBtn_getFitur = QtWidgets.QPushButton(self.gBox_rightButton)
        self.pBtn_getFitur.setGeometry(QtCore.QRect(10, 80, 75, 23))
        self.pBtn_getFitur.setObjectName("pBtn_getFitur")
        self.gBox_images = QtWidgets.QGroupBox(self.centralwidget)
        self.gBox_images.setGeometry(QtCore.QRect(10, 60, 591, 261))
        self.gBox_images.setTitle("")
        self.gBox_images.setObjectName("gBox_images")
        self.lbl_imgOriginal = QtWidgets.QLabel(self.gBox_images)
        self.lbl_imgOriginal.setGeometry(QtCore.QRect(10, 9, 281, 241))
        self.lbl_imgOriginal.setStyleSheet("background-color:rgb(85, 255, 255)")
        self.lbl_imgOriginal.setScaledContents(True)
        self.lbl_imgOriginal.setObjectName("lbl_imgOriginal")
        self.lbl_imgResult = QtWidgets.QLabel(self.gBox_images)
        self.lbl_imgResult.setGeometry(QtCore.QRect(299, 9, 281, 241))
        self.lbl_imgResult.setStyleSheet("background-color:rgb(85, 255, 255)")
        self.lbl_imgResult.setScaledContents(True)
        self.lbl_imgResult.setObjectName("lbl_imgResult")
        self.gBox_mainMenu = QtWidgets.QGroupBox(self.centralwidget)
        self.gBox_mainMenu.setGeometry(QtCore.QRect(10, 0, 211, 51))
        self.gBox_mainMenu.setObjectName("gBox_mainMenu")
        self.cb_file = QtWidgets.QComboBox(self.gBox_mainMenu)
        self.cb_file.setGeometry(QtCore.QRect(10, 20, 91, 22))
        self.cb_file.setObjectName("cb_file")
        self.cb_file.addItem("")
        self.cb_file.addItem("")
        self.cb_edit = QtWidgets.QComboBox(self.gBox_mainMenu)
        self.cb_edit.setGeometry(QtCore.QRect(108, 20, 91, 22))
        self.cb_edit.setObjectName("cb_edit")
        self.cb_edit.addItem("")
        self.cb_edit.addItem("")
        self.cb_edit.addItem("")
        self.cb_edit.addItem("")
        self.gBox_result = QtWidgets.QGroupBox(self.centralwidget)
        self.gBox_result.setGeometry(QtCore.QRect(10, 330, 591, 151))
        self.gBox_result.setTitle("")
        self.gBox_result.setObjectName("gBox_result")
        self.gBox_RGB = QtWidgets.QGroupBox(self.gBox_result)
        self.gBox_RGB.setGeometry(QtCore.QRect(10, 10, 281, 131))
        self.gBox_RGB.setTitle("")
        self.gBox_RGB.setObjectName("gBox_RGB")
        self.lbl_r = QtWidgets.QLabel(self.gBox_RGB)
        self.lbl_r.setGeometry(QtCore.QRect(10, 20, 21, 16))
        self.lbl_r.setObjectName("lbl_r")
        self.lbl_valueR = QtWidgets.QLabel(self.gBox_RGB)
        self.lbl_valueR.setGeometry(QtCore.QRect(40, 20, 221, 16))
        self.lbl_valueR.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lbl_valueR.setText("")
        self.lbl_valueR.setObjectName("lbl_valueR")
        self.lbl_g = QtWidgets.QLabel(self.gBox_RGB)
        self.lbl_g.setGeometry(QtCore.QRect(10, 50, 16, 16))
        self.lbl_g.setObjectName("lbl_g")
        self.lbl_b = QtWidgets.QLabel(self.gBox_RGB)
        self.lbl_b.setGeometry(QtCore.QRect(10, 80, 16, 16))
        self.lbl_b.setObjectName("lbl_b")
        self.lbl_valueG = QtWidgets.QLabel(self.gBox_RGB)
        self.lbl_valueG.setGeometry(QtCore.QRect(40, 50, 221, 16))
        self.lbl_valueG.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lbl_valueG.setText("")
        self.lbl_valueG.setObjectName("lbl_valueG")
        self.lbl_valueB = QtWidgets.QLabel(self.gBox_RGB)
        self.lbl_valueB.setGeometry(QtCore.QRect(40, 80, 221, 16))
        self.lbl_valueB.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lbl_valueB.setText("")
        self.lbl_valueB.setObjectName("lbl_valueB")
        self.gBox_fitur = QtWidgets.QGroupBox(self.gBox_result)
        self.gBox_fitur.setGeometry(QtCore.QRect(300, 10, 281, 131))
        self.gBox_fitur.setTitle("")
        self.gBox_fitur.setObjectName("gBox_fitur")
        self.lbl_fitur1 = QtWidgets.QLabel(self.gBox_fitur)
        self.lbl_fitur1.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.lbl_fitur1.setObjectName("lbl_fitur1")
        self.lbl_fitur2 = QtWidgets.QLabel(self.gBox_fitur)
        self.lbl_fitur2.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.lbl_fitur2.setObjectName("lbl_fitur2")
        self.lbl_fitur3 = QtWidgets.QLabel(self.gBox_fitur)
        self.lbl_fitur3.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.lbl_fitur3.setObjectName("lbl_fitur3")
        self.lbl_valueFitur1 = QtWidgets.QLabel(self.gBox_fitur)
        self.lbl_valueFitur1.setGeometry(QtCore.QRect(90, 20, 181, 20))
        self.lbl_valueFitur1.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lbl_valueFitur1.setText("")
        self.lbl_valueFitur1.setObjectName("lbl_valueFitur1")
        self.lbl_valueFitur2 = QtWidgets.QLabel(self.gBox_fitur)
        self.lbl_valueFitur2.setGeometry(QtCore.QRect(90, 50, 181, 20))
        self.lbl_valueFitur2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lbl_valueFitur2.setText("")
        self.lbl_valueFitur2.setObjectName("lbl_valueFitur2")
        self.lbl_valueFitur3 = QtWidgets.QLabel(self.gBox_fitur)
        self.lbl_valueFitur3.setGeometry(QtCore.QRect(90, 80, 181, 20))
        self.lbl_valueFitur3.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lbl_valueFitur3.setText("")
        self.lbl_valueFitur3.setObjectName("lbl_valueFitur3")
        self.pBtn_zoom = QtWidgets.QPushButton(self.centralwidget)
        self.pBtn_zoom.setGeometry(QtCore.QRect(530, 30, 61, 21))
        self.pBtn_zoom.setObjectName("pBtn_zoom")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # coding logic
        self.window = MainWindow
        self.mainProgram()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pBtn_save.setText(_translate("MainWindow", "Save"))
        self.pBtn_getRGB.setText(_translate("MainWindow", "Get RGB"))
        self.pBtn_getFitur.setText(_translate("MainWindow", "Get Fitur"))
        self.lbl_imgOriginal.setText(_translate("MainWindow", "Original Image"))
        self.lbl_imgResult.setText(_translate("MainWindow", "Final Result"))
        self.gBox_mainMenu.setTitle(_translate("MainWindow", "Main Menu"))
        self.cb_file.setItemText(0, _translate("MainWindow", "File"))
        self.cb_file.setItemText(1, _translate("MainWindow", "Open Image"))
        self.cb_edit.setItemText(0, _translate("MainWindow", "Edit"))
        self.cb_edit.setItemText(1, _translate("MainWindow", "Grayscale"))
        self.cb_edit.setItemText(2, _translate("MainWindow", "Binarization"))
        self.cb_edit.setItemText(3, _translate("MainWindow", "Edge Detection"))
        self.lbl_r.setText(_translate("MainWindow", "R"))
        self.lbl_g.setText(_translate("MainWindow", "G"))
        self.lbl_b.setText(_translate("MainWindow", "B"))
        self.lbl_fitur1.setText(_translate("MainWindow", "Total Objek"))
        self.lbl_fitur2.setText(_translate("MainWindow", "Total Point"))
        self.lbl_fitur3.setText(_translate("MainWindow", "Total Area"))
        self.pBtn_zoom.setText(_translate("MainWindow", "Zoom"))

    # ------------------- logic utama program  start --------------------

    def mainProgram(self):
        self.cek_gambar = False

        self.cb_file.currentIndexChanged.connect(self.onChange_cb_file)
        self.cb_edit.currentIndexChanged.connect(self.onChange_cb_edit)

        self.pBtn_getRGB.clicked.connect(self.getRGB)
        self.pBtn_getFitur.clicked.connect(self.getFitur)

        self.pBtn_zoom.clicked.connect(self.zoom)

    def onChange_cb_file(self, i):
        cb_file_val = self.cb_file.currentText()

        if cb_file_val == 'File':
            self.resetButtonMainMenu()

        elif cb_file_val == 'Open Image':
            self.openImage()
            self.resetButtonMainMenu()
            self.resetValueFitur()

    def onChange_cb_edit(self):
        cb_edit_val = self.cb_edit.currentText()

        if cb_edit_val == 'Edit':
            self.resetButtonMainMenu()

        elif cb_edit_val == 'Grayscale':
            if self.cek_gambar == True:
                img = self.img
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                self.final_image = img_gray
                img_gray = self.displayImage(img_gray)
                self.lbl_imgResult.setPixmap(QPixmap.fromImage(img_gray))
                self.resetValueFitur()
            else:
                print('Tidak Ada Gambar')
            self.resetButtonMainMenu()

        elif cb_edit_val == 'Binarization':
            if self.cek_gambar == True:
                img = self.img
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                _, img_biner = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
                self.final_image = img_biner
                img_biner = self.displayImage(img_biner)
                self.lbl_imgResult.setPixmap(QPixmap.fromImage(img_biner))
                self.resetValueFitur()
            else:
                print('Tidak Ada Gambar')
            self.resetButtonMainMenu()

        elif cb_edit_val == 'Edge Detection':

            if self.cek_gambar == True:
                img = self.img
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                sobelX = cv2.Sobel(img_gray, cv2.CV_64F, 1,
                                   0)  # (gradient) perubahan arah intensitas warna ada di arah x
                sobelY = cv2.Sobel(img_gray, cv2.CV_64F, 0,
                                   1)  # (gradient) perubahan arah intensitas warna ada di arah y

                sobelX = np.uint8(np.absolute(sobelX))  # konversi nilai menjadi unsigned 8 bit interger
                sobelY = np.uint8(np.absolute(sobelY))  # konversi nilai menjadi unsigned 8 bit interger

                sobelCombined = cv2.bitwise_or(sobelX, sobelY)  # kombinasi sobel x dan

                self.final_image = sobelCombined
                sobelCombined = self.displayImage(sobelCombined)
                self.lbl_imgResult.setPixmap(QPixmap.fromImage(sobelCombined))

                self.resetValueFitur()

            else:
                print('Tidak Ada Gambar')
            self.resetButtonMainMenu()

    def openImage(self):
        file_name, _ = QFileDialog.getOpenFileName(self.window, 'Open Image File', r"",
                                                   "Image files (*.jpg *.jpeg *.png)")
        if file_name != '':
            self.img = cv2.imread(file_name, 1)
            self.final_image = self.img
            self.lbl_imgOriginal.setPixmap(QPixmap(file_name))
            self.cek_gambar = True
            self.resetValueRGB()
            self.resetValueFitur()
        else:
            print('Load image failed')

    def resetButtonMainMenu(self):
        index = 0
        self.cb_file.setCurrentIndex(index)
        self.cb_edit.setCurrentIndex(index)

    def getRGB(self):
        if self.cek_gambar == True:
            img = self.img
            channels = cv2.mean(img)  # Calculate the mean of each channel
            R = channels[2]
            G = channels[1]
            B = channels[0]
            self.lbl_valueR.setText(str(R))
            self.lbl_valueG.setText(str(G))
            self.lbl_valueB.setText(str(B))
        else:
            print('Tidak Ada Gambar')

    def resetValueRGB(self):
        self.lbl_valueR.setText('')
        self.lbl_valueG.setText('')
        self.lbl_valueB.setText('')

    def getFitur(self):
        if self.cek_gambar == True:
            self.pBtn_getFitur.setEnabled(False)
            self.objectDetection()
        else:
            print('Tidak Ada Gambar')

    def objectDetection(self):
        def empty(a):
            pass

        windowsNamed = 'Parameters'
        cv2.namedWindow(windowsNamed)
        cv2.resizeWindow(windowsNamed, 640, 240)
        cv2.createTrackbar("Threshold1", windowsNamed, 23, 255, empty)
        cv2.createTrackbar("Threshold2", windowsNamed, 20, 255, empty)
        cv2.createTrackbar("Min Area", windowsNamed, 5000, 30000, empty)

        def stackImages(scale, imgArray):
            rows = len(imgArray)
            cols = len(imgArray[0])
            rowsAvailable = isinstance(imgArray[0], list)
            width = imgArray[0][0].shape[1]
            height = imgArray[0][0].shape[0]
            if rowsAvailable:
                for x in range(0, rows):
                    for y in range(0, cols):
                        if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                            imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                        else:
                            imgArray[x][y] = cv2.resize(imgArray[x][y],
                                                        (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale,
                                                        scale)
                        if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y],
                                                                                         cv2.COLOR_GRAY2BGR)
                imageBlank = np.zeros((height, width, 3), np.uint8)
                hor = [imageBlank] * rows
                hor_con = [imageBlank] * rows
                for x in range(0, rows):
                    hor[x] = np.hstack(imgArray[x])
                ver = np.vstack(hor)
            else:
                for x in range(0, rows):
                    if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                        imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
                    else:
                        imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale,
                                                 scale)
                    if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
                hor = np.hstack(imgArray)
                ver = hor
            return ver

        def getContours(img, imgContour):
            contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            total_objek = 0
            total_point = 0
            total_area = 0
            # print(len(contours))
            for cnt in contours:
                area = cv2.contourArea(cnt)
                areaMin = cv2.getTrackbarPos("Min Area", windowsNamed)
                if area > areaMin:
                    cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
                    peri = cv2.arcLength(cnt, True)
                    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
                    # print(len(approx))
                    x, y, w, h = cv2.boundingRect(approx)
                    cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)

                    total_objek = total_objek + 1
                    total_point = total_point + len(approx)
                    total_area = total_area + int(area)

                    cv2.putText(imgContour, "Points: " + str(len(approx)), (x + 20, y + 20),
                                cv2.FONT_HERSHEY_COMPLEX, .7,
                                (255, 0, 0), 2)
                    cv2.putText(imgContour, "Area: " + str(int(area)), (x + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX,
                                0.7,
                                (0, 0, 255), 2)

            self.setFiturValue(total_objek, total_point, total_area)

        # print("ssss")
        while cv2.getWindowProperty(windowsNamed, cv2.WND_PROP_VISIBLE) >= 1:
            img = self.img
            imgContour = img.copy()
            imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
            imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
            threshold1 = cv2.getTrackbarPos("Threshold1", windowsNamed)
            threshold2 = cv2.getTrackbarPos("Threshold2", windowsNamed)
            imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
            kernel = np.ones((5, 5))
            imgDil = cv2.dilate(imgCanny, kernel, iterations=1)
            getContours(imgDil, imgContour)
            imgStack = stackImages(0.8, ([img, imgCanny],
                                         [imgDil, imgContour]))
            self.final_image = imgContour
            imgStack = self.displayImage(imgStack)
            self.lbl_imgResult.setPixmap(QPixmap.fromImage(imgStack))
            if cv2.waitKey(1) == 27:  # jika mendeteksi input keyboard tertentu
                break  # keluar dari fungsi loop

        cv2.destroyAllWindows()
        self.pBtn_getFitur.setEnabled(True)

    def setFiturValue(self, fitur1, fitur2, fitur3):
        self.lbl_valueFitur1.setText(str(fitur1))
        self.lbl_valueFitur2.setText(str(fitur2))
        self.lbl_valueFitur3.setText(str(fitur3))

    def resetValueFitur(self):
        self.lbl_valueFitur1.setText('')
        self.lbl_valueFitur2.setText('')
        self.lbl_valueFitur3.setText('')

    def zoom(self):
        if self.cek_gambar == True:
            cv2.imshow('Zoom', self.final_image)
        else:
            print('Tidak Ada Gambar')

    def displayImage(self, img):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:  # [0]=rows, [1]=cols, [2]=channels
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        # BGR to RGB
        outImage = outImage.rgbSwapped()
        return outImage

    def nothing(self):
        pass

    # ------------------- logic utama program  end --------------------


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
