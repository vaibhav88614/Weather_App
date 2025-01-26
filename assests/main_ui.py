# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(768, 651)
        MainWindow.setMinimumSize(QtCore.QSize(768, 651))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.info = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.info.setFont(font)
        self.info.setObjectName("info")
        self.verticalLayout_2.addWidget(self.info)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.entertheLocation = QtWidgets.QLabel(self.centralwidget)
        self.entertheLocation.setMinimumSize(QtCore.QSize(141, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.entertheLocation.setFont(font)
        self.entertheLocation.setObjectName("entertheLocation")
        self.horizontalLayout.addWidget(self.entertheLocation)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cityData = QtWidgets.QLineEdit(self.centralwidget)
        self.cityData.setMinimumSize(QtCore.QSize(211, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cityData.setFont(font)
        self.cityData.setStyleSheet("QLineEdit{\n"
"    border:None;\n"
"    border-radius:10px;\n"
"    padding:15px;\n"
"}")
        self.cityData.setObjectName("cityData")
        self.horizontalLayout.addWidget(self.cityData)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.getWeatherPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.getWeatherPushButton.setMinimumSize(QtCore.QSize(175, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.getWeatherPushButton.setFont(font)
        self.getWeatherPushButton.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    background-color:#7cce1f;\n"
"    color:black;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color:#2c4311;\n"
"    color:white;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.getcwd()+"\\assests\\cloudy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getWeatherPushButton.setIcon(icon)
        self.getWeatherPushButton.setIconSize(QtCore.QSize(30, 30))
        self.getWeatherPushButton.setObjectName("getWeatherPushButton")
        self.horizontalLayout.addWidget(self.getWeatherPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"        border: 2px solid #7cce1f;\n"
"        border-radius: 10px;\n"
"        gridline-color: #2c4311;\n"
"        background-color: #f9f9f9;\n"
"        font: 12pt \"Times New Roman\";\n"
"    }\n"
"    QHeaderView::section {\n"
"        background-color: #7cce1f;\n"
"        color: white;\n"
"        padding: 5px;\n"
"        border: 1px solid #2c4311;\n"
"        font: bold 12pt \"Times New Roman\";\n"
"    }\n"
"    QTableWidget::item {\n"
"        padding: 10px;\n"
"        border: none;\n"
"    }\n"
"    QTableWidget::item:selected {\n"
"        background-color: #bdecb6;\n"
"        color: black;\n"
"    }\n"
"    QTableWidget::item:focus {\n"
"        outline: none;\n"
"    }\n"
"    QTableCornerButton::section {\n"
"        background-color: #7cce1f;\n"
"        border: 1px solid #2c4311;\n"
"    }\n"
"    QTableWidget::item {\n"
"        border-bottom: 1px solid #d3d3d3;\n"
"    }\n"
"    QTableWidget::item:!selected {\n"
"        background-color: #ffffff;\n"
"    }\n"
"    QTableWidget::item:nth-child(even):!selected {\n"
"        background-color: #f3f3f3;\n"
"    }")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.info.setText(_translate("MainWindow", "Enter the city, if there are multiple cities\n"
"separate the by commas(Ex:Bengaluru,Kolkatta)"))
        self.entertheLocation.setText(_translate("MainWindow", "Enter the Location"))
        self.getWeatherPushButton.setText(_translate("MainWindow", "Get Weather"))
        self.getWeatherPushButton.setShortcut(_translate("MainWindow", "Return"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "00:00:00"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "06:00:00"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "12:00:00"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "18:00:00"))
