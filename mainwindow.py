# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(702, 553)
        self.button_load_image = QtWidgets.QPushButton(Form)
        self.button_load_image.setGeometry(QtCore.QRect(80, 420, 93, 28))
        self.button_load_image.setObjectName("button_load_image")
        self.button_equalizeHist = QtWidgets.QPushButton(Form)
        self.button_equalizeHist.setGeometry(QtCore.QRect(280, 380, 131, 28))
        self.button_equalizeHist.setObjectName("button_equalizeHist")
        self.button_save_image = QtWidgets.QPushButton(Form)
        self.button_save_image.setGeometry(QtCore.QRect(500, 420, 93, 28))
        self.button_save_image.setObjectName("button_save_image")
        self.graphicsView_left = QtWidgets.QGraphicsView(Form)
        self.graphicsView_left.setGeometry(QtCore.QRect(25, 100, 301, 251))
        self.graphicsView_left.setObjectName("graphicsView_left")
        self.graphicsView_right = QtWidgets.QGraphicsView(Form)
        self.graphicsView_right.setGeometry(QtCore.QRect(370, 100, 301, 251))
        self.graphicsView_right.setObjectName("graphicsView_right")
        self.button_average_filtering = QtWidgets.QPushButton(Form)
        self.button_average_filtering.setGeometry(QtCore.QRect(280, 430, 131, 28))
        self.button_average_filtering.setObjectName("button_average_filtering")
        self.button_mid_filtering = QtWidgets.QPushButton(Form)
        self.button_mid_filtering.setGeometry(QtCore.QRect(280, 480, 131, 28))
        self.button_mid_filtering.setObjectName("button_mid_filtering")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 20, 311, 51))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_load_image.setText(_translate("Form", "读取图像"))
        self.button_equalizeHist.setText(_translate("Form", "直方图均衡化"))
        self.button_save_image.setText(_translate("Form", "保存图像"))
        self.button_average_filtering.setText(_translate("Form", "均值滤波"))
        self.button_mid_filtering.setText(_translate("Form", "中值滤波"))
        self.label.setText(_translate("Form", "数字图像处理demo"))

