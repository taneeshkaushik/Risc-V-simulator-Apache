# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.label = QtWidgets.QLabel(MainWindow)
        MainWindow.label.setPixmap(QtGui.QPixmap('wallpaper.jpg'))   # Background image
        MainWindow.label.setGeometry(0, -200, 2560, 1440)
        FONT = QtGui.QFont()
        FONT.setPointSize(14)
        font2 = QtGui.QFont()
        font2.setPointSize(12)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1535, 858)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.editor_code = QtWidgets.QPlainTextEdit(self.tab)
        self.editor_code.setObjectName("editor_code")
        self.editor_code.setFont(FONT)
        self.gridLayout_2.addWidget(self.editor_code, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.pc_edit = QtWidgets.QLineEdit(self.tab_2)
        self.pc_edit.setObjectName("pc_edit")
        self.pc_edit.setFont(FONT)
        self.gridLayout_6.addWidget(self.pc_edit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_6.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_6.addWidget(self.pushButton_3, 0, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_6.addWidget(self.pushButton_4, 0, 5, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_6.addWidget(self.pushButton_5, 0, 6, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_6.addWidget(self.pushButton_6, 0, 7, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setUsesScrollButtons(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 337, 1007))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.x0 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x0.setObjectName("x0")
        self.x0.setFont(font2)
        self.gridLayout_5.addWidget(self.x0, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 1, 0, 1, 1)
        self.x1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x1.setObjectName("x1")
        self.x1.setFont(font2)
        self.gridLayout_5.addWidget(self.x1, 1, 1, 1, 1)
        self.x9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x9.setObjectName("x9")
        self.x9.setFont(font2)
        self.gridLayout_5.addWidget(self.x9, 9, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 10, 0, 1, 1)
        self.x10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x10.setObjectName("x10")
        self.x10.setFont(font2)
        self.gridLayout_5.addWidget(self.x10, 10, 1, 1, 1)
        self.x4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x4.setObjectName("x4")
        self.x4.setFont(font2)
        self.gridLayout_5.addWidget(self.x4, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 7, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 4, 0, 1, 1)
        self.x6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x6.setObjectName("x6")
        self.x6.setFont(font2)
        self.gridLayout_5.addWidget(self.x6, 6, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 6, 0, 1, 1)
        self.x2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x2.setObjectName("x2")
        self.x2.setFont(font2)
        self.gridLayout_5.addWidget(self.x2, 2, 1, 1, 1)
        self.x5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x5.setObjectName("x5")
        self.x5.setFont(font2)
        self.gridLayout_5.addWidget(self.x5, 5, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 3, 0, 1, 1)
        self.x3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x3.setObjectName("x3")
        self.x3.setFont(font2)
        self.gridLayout_5.addWidget(self.x3, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 5, 0, 1, 1)
        self.x7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x7.setText("")
        self.x7.setObjectName("x7")
        self.x7.setFont(font2)
        self.gridLayout_5.addWidget(self.x7, 7, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 8, 0, 1, 1)
        self.x8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x8.setObjectName("x8")
        self.x8.setFont(font2)
        self.gridLayout_5.addWidget(self.x8, 8, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 9, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 11, 0, 1, 1)
        self.x11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x11.setObjectName("x11")
        self.x11.setFont(font2)
        self.gridLayout_5.addWidget(self.x11, 11, 1, 1, 1)
        self.x12 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x12.setObjectName("x12")
        self.x12.setFont(font2)
        self.gridLayout_5.addWidget(self.x12, 12, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 13, 0, 1, 1)
        self.x13 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x13.setObjectName("x13")
        self.x13.setFont(font2)
        self.gridLayout_5.addWidget(self.x13, 13, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 12, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 14, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 22, 0, 1, 1)
        self.x17 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x17.setObjectName("x17")
        self.x17.setFont(font2)
        self.gridLayout_5.addWidget(self.x17, 17, 1, 1, 1)
        self.x22 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x22.setObjectName("x22")
        self.x22.setFont(font2)
        self.gridLayout_5.addWidget(self.x22, 22, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 23, 0, 1, 1)
        self.x24 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x24.setObjectName("x24")
        self.x24.setFont(font2)
        self.gridLayout_5.addWidget(self.x24, 24, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 25, 0, 1, 1)
        self.x25 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x25.setObjectName("x25")
        self.x25.setFont(font2)
        self.gridLayout_5.addWidget(self.x25, 25, 1, 1, 1)
        self.x15 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x15.setObjectName("x15")
        self.x15.setFont(font2)
        self.gridLayout_5.addWidget(self.x15, 15, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 24, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 18, 0, 1, 1)
        self.x23 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x23.setObjectName("x23")
        self.x23.setFont(font2)
        self.gridLayout_5.addWidget(self.x23, 23, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 26, 0, 1, 1)
        self.x18 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x18.setObjectName("x18")
        self.x18.setFont(font2)
        self.gridLayout_5.addWidget(self.x18, 18, 1, 1, 1)
        self.x20 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x20.setObjectName("x20")
        self.x20.setFont(font2)
        self.gridLayout_5.addWidget(self.x20, 20, 1, 1, 1)
        self.x19 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x19.setObjectName("x19")
        self.x19.setFont(font2)
        self.gridLayout_5.addWidget(self.x19, 19, 1, 1, 1)
        self.x26 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x26.setObjectName("x26")
        self.x26.setFont(font2)
        self.gridLayout_5.addWidget(self.x26, 26, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_32.setObjectName("label_32")
        self.gridLayout_5.addWidget(self.label_32, 17, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 15, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 16, 0, 1, 1)
        self.x16 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x16.setObjectName("x16")
        self.x16.setFont(font2)
        self.gridLayout_5.addWidget(self.x16, 16, 1, 1, 1)
        self.x14 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x14.setObjectName("x14")
        self.x14.setFont(font2)
        self.gridLayout_5.addWidget(self.x14, 14, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 20, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 21, 0, 1, 1)
        self.x21 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x21.setObjectName("x21")
        self.x21.setFont(font2)
        self.gridLayout_5.addWidget(self.x21, 21, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 19, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_33.setObjectName("label_33")
        self.gridLayout_5.addWidget(self.label_33, 30, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_30.setObjectName("label_30")
        self.gridLayout_5.addWidget(self.label_30, 28, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_34.setObjectName("label_34")
        self.gridLayout_5.addWidget(self.label_34, 31, 0, 1, 1)
        self.x30 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x30.setObjectName("x30")
        self.x30.setFont(font2)
        self.gridLayout_5.addWidget(self.x30, 30, 1, 1, 1)
        self.x29 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x29.setObjectName("x29")
        self.x29.setFont(font2)
        self.gridLayout_5.addWidget(self.x29, 29, 1, 1, 1)
        self.x28 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x28.setObjectName("x28")
        self.x28.setFont(font2)
        self.gridLayout_5.addWidget(self.x28, 28, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_29.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_29, 27, 0, 1, 1)
        self.x27 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x27.setObjectName("x27")
        self.x27.setFont(font2)
        self.gridLayout_5.addWidget(self.x27, 27, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_31.setObjectName("label_31")
        self.gridLayout_5.addWidget(self.label_31, 29, 0, 1, 1)
        self.x31 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x31.setObjectName("x31")
        self.x31.setFont(font2)
        self.gridLayout_5.addWidget(self.x31, 31, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 358, 681))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_35.setObjectName("label_35")
        self.gridLayout_8.addWidget(self.label_35, 0, 1, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_36.setObjectName("label_36")
        self.gridLayout_8.addWidget(self.label_36, 0, 2, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_37.setObjectName("label_37")
        self.gridLayout_8.addWidget(self.label_37, 0, 3, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_38.setObjectName("label_38")
        self.gridLayout_8.addWidget(self.label_38, 0, 4, 1, 1)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_8.addWidget(self.line, 1, 0, 1, 5)
        self.address_code = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.address_code.setObjectName("address_code")
        self.address_code.setFont(font2)
        self.gridLayout_8.addWidget(self.address_code, 2, 0, 1, 5)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.addWidget(self.scrollArea_2, 0, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.gridLayout_6.addWidget(self.tabWidget_2, 0, 8, 2, 1)
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout.setObjectName("gridLayout")
        self.basic_code = QtWidgets.QPlainTextEdit(self.tab_5)
        self.basic_code.setObjectName("basic_code")
        self.basic_code.setFont(FONT)
        self.gridLayout.addWidget(self.basic_code, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_5, "")
        self.gridLayout_6.addWidget(self.tabWidget_3, 1, 0, 1, 3)
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.machine_code = QtWidgets.QTextEdit(self.tab_6)
        self.machine_code.setObjectName("machine_code")
        self.machine_code.setFont(FONT)
        self.gridLayout_3.addWidget(self.machine_code, 0, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_6, "")
        self.gridLayout_6.addWidget(self.tabWidget_4, 1, 3, 1, 5)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1535, 26))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_New_Project = QtWidgets.QAction(MainWindow)
        self.action_New_Project.setObjectName("action_New_Project")
        self.action_Open_Project = QtWidgets.QAction(MainWindow)
        self.action_Open_Project.setObjectName("action_Open_Project")
        self.action_Save_Project = QtWidgets.QAction(MainWindow)
        self.action_Save_Project.setObjectName("action_Save_Project")
        self.action_Close_Project = QtWidgets.QAction(MainWindow)
        self.action_Close_Project.setObjectName("action_Close_Project")
        self.action_Undo = QtWidgets.QAction(MainWindow)
        self.action_Undo.setObjectName("action_Undo")
        self.action_Redo = QtWidgets.QAction(MainWindow)
        self.action_Redo.setObjectName("action_Redo")
        self.action_Cut = QtWidgets.QAction(MainWindow)
        self.action_Cut.setObjectName("action_Cut")
        self.action_Copy = QtWidgets.QAction(MainWindow)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Paste = QtWidgets.QAction(MainWindow)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Select_All = QtWidgets.QAction(MainWindow)
        self.action_Select_All.setObjectName("action_Select_All")
        self.menu_File.addAction(self.action_New_Project)
        self.menu_File.addAction(self.action_Close_Project)
        self.menu_Edit.addAction(self.action_Undo)
        self.menu_Edit.addAction(self.action_Redo)
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addAction(self.action_Select_All)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.action_Close_Project.triggered.connect(MainWindow.close)
        self.action_Select_All.triggered.connect(self.editor_code.selectAll)
        self.action_Paste.triggered.connect(self.editor_code.paste)
        self.action_Undo.triggered.connect(self.basic_code.undo)
        self.action_Cut.triggered.connect(self.basic_code.cut)
        self.action_Redo.triggered.connect(self.basic_code.redo)
        self.action_Paste.triggered.connect(self.basic_code.paste)
        self.action_Select_All.triggered.connect(self.basic_code.selectAll)
        self.action_Copy.triggered.connect(self.basic_code.copy)
        self.action_Copy.triggered.connect(self.editor_code.copy)
        self.action_Undo.triggered.connect(self.editor_code.undo)
        self.action_Redo.triggered.connect(self.editor_code.redo)
        self.action_Cut.triggered.connect(self.editor_code.cut)
        self.editor_code.textChanged.connect(self.save_testcode)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def save_testcode(self):
        text = self.editor_code.toPlainText()
        with open('testcode.asm', 'w') as f:
            f.write(text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Apache 1.0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Editor"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">PC VALUE:</span></p></body></html>"))
        self.pc_edit.setText(_translate("MainWindow", "(Current PC value)"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.pushButton_2.setText(_translate("MainWindow", "Step"))
        self.pushButton_3.setText(_translate("MainWindow", "Previous"))
        self.pushButton_4.setText(_translate("MainWindow", "Reset"))
        self.pushButton_5.setText(_translate("MainWindow", "Breakpoint"))
        self.pushButton_6.setText(_translate("MainWindow", "Stop"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">sp(x2)</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">zero</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">ra(x1)</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a0(x10)</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">t2(x7)</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">tp(x4)</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">t1(x6)</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">gp(x3)</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">t0(x5)</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s0(x8)</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s1(x9)</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a1(x11)</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a3(x13)</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a2(x12)</span></p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a4(x14)</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s6(x22)</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s7(x23)</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s9(x25)</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s8(x24)</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s2(x18)</span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">s10(x26)</span></p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a7(x17)</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a5(x15)</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a6(x16)</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s4(x20)</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s5(x21)</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s3(x19)</span></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">t5(x30)</span></p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">t3(x28)</span></p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">t6(x31)</span></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">s11(x27)</span></p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">t4(x29)</span></p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "REGISTERS"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt;\">Address</span></p></body></html>"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">+0</span></p></body></html>"))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">+1</span></p></body></html>"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">+2</span></p></body></html>"))
        self.label_38.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">+3</span></p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "MEMORY"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("MainWindow", "Basic Code"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_6), _translate("MainWindow", "Machine Code"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Simulator"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit"))
        self.action_New_Project.setText(_translate("MainWindow", "&New Project"))
        self.action_New_Project.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_Open_Project.setText(_translate("MainWindow", "&Open Project"))
        self.action_Save_Project.setText(_translate("MainWindow", "&Save Project"))
        self.action_Save_Project.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_Close_Project.setText(_translate("MainWindow", "&Close Project"))
        self.action_Undo.setText(_translate("MainWindow", "&Undo"))
        self.action_Undo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.action_Redo.setText(_translate("MainWindow", "&Redo"))
        self.action_Redo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.action_Cut.setText(_translate("MainWindow", "&Cut"))
        self.action_Cut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.action_Copy.setText(_translate("MainWindow", "&Copy"))
        self.action_Copy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.action_Paste.setText(_translate("MainWindow", "&Paste"))
        self.action_Paste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.action_Select_All.setText(_translate("MainWindow", "&Select All"))
        self.action_Select_All.setShortcut(_translate("MainWindow", "Ctrl+A"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
