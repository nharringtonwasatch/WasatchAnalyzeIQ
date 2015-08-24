# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wasatchanalyzeiq/ui/AnalyzeIQLayout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(622, 302)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.toolButtonAcquire = QtGui.QToolButton(self.tab)
        self.toolButtonAcquire.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButtonAcquire.setIconSize(QtCore.QSize(96, 96))
        self.toolButtonAcquire.setObjectName(_fromUtf8("toolButtonAcquire"))
        self.gridLayout.addWidget(self.toolButtonAcquire, 4, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.checkBoxLaserEnable = QtGui.QCheckBox(self.tab)
        self.checkBoxLaserEnable.setObjectName(_fromUtf8("checkBoxLaserEnable"))
        self.gridLayout.addWidget(self.checkBoxLaserEnable, 1, 1, 1, 1)
        self.labelDeviceText = QtGui.QLabel(self.tab)
        self.labelDeviceText.setMinimumSize(QtCore.QSize(0, 0))
        self.labelDeviceText.setObjectName(_fromUtf8("labelDeviceText"))
        self.gridLayout.addWidget(self.labelDeviceText, 0, 2, 1, 1)
        self.labelLogo = QtGui.QLabel(self.tab)
        self.labelLogo.setText(_fromUtf8(""))
        self.labelLogo.setPixmap(QtGui.QPixmap(_fromUtf8("imagery/wasatch_name.png")))
        self.labelLogo.setObjectName(_fromUtf8("labelLogo"))
        self.gridLayout.addWidget(self.labelLogo, 0, 1, 1, 1)
        self.toolButtonCancel = QtGui.QToolButton(self.tab)
        self.toolButtonCancel.setMinimumSize(QtCore.QSize(150, 40))
        self.toolButtonCancel.setObjectName(_fromUtf8("toolButtonCancel"))
        self.gridLayout.addWidget(self.toolButtonCancel, 4, 3, 1, 1)
        self.lcdNumber = QtGui.QLCDNumber(self.tab)
        self.lcdNumber.setProperty("value", 60000.0)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.gridLayout.addWidget(self.lcdNumber, 0, 3, 1, 1)
        self.spinBoxIntegrationTime = QtGui.QSpinBox(self.tab)
        self.spinBoxIntegrationTime.setMinimumSize(QtCore.QSize(200, 0))
        self.spinBoxIntegrationTime.setMinimum(10)
        self.spinBoxIntegrationTime.setMaximum(60000)
        self.spinBoxIntegrationTime.setProperty("value", 100)
        self.spinBoxIntegrationTime.setObjectName(_fromUtf8("spinBoxIntegrationTime"))
        self.gridLayout.addWidget(self.spinBoxIntegrationTime, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.layoutWidget = QtGui.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 161))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditCoeff0 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditCoeff0.setObjectName(_fromUtf8("lineEditCoeff0"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditCoeff0)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditCoeff1 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditCoeff1.setObjectName(_fromUtf8("lineEditCoeff1"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditCoeff1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEditCoeff2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditCoeff2.setObjectName(_fromUtf8("lineEditCoeff2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditCoeff2)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEditCoeff3 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditCoeff3.setObjectName(_fromUtf8("lineEditCoeff3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditCoeff3)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.toolButtonAcquire.setText(_translate("MainWindow", "Acquire", None))
        self.checkBoxLaserEnable.setText(_translate("MainWindow", "Laser Enable", None))
        self.labelDeviceText.setText(_translate("MainWindow", "Searching for device...", None))
        self.toolButtonCancel.setText(_translate("MainWindow", "Cancel", None))
        self.spinBoxIntegrationTime.setSuffix(_translate("MainWindow", " ms", None))
        self.spinBoxIntegrationTime.setPrefix(_translate("MainWindow", "Integration time: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main Settings", None))
        self.label_2.setText(_translate("MainWindow", "Coefficient C0:", None))
        self.lineEditCoeff0.setText(_translate("MainWindow", "778.267", None))
        self.label_3.setText(_translate("MainWindow", "Coefficient C1:", None))
        self.lineEditCoeff1.setText(_translate("MainWindow", "0.189334", None))
        self.label_4.setText(_translate("MainWindow", "Coefficient C2:", None))
        self.lineEditCoeff2.setText(_translate("MainWindow", "1.24617e-05", None))
        self.label_5.setText(_translate("MainWindow", "Coefficient C3:", None))
        self.lineEditCoeff3.setText(_translate("MainWindow", "-3.17627e-08", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Calibration", None))

