from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 365)
        MainWindow.setMinimumSize(QSize(400, 275))
        MainWindow.setMaximumSize(QSize(400, 365))
        self.history = QAction(MainWindow)
        self.history.setObjectName(u"history")
        self.save = QAction(MainWindow)
        self.save.setObjectName(u"save")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.surname_label = QLabel(self.centralwidget)
        self.surname_label.setObjectName(u"surname_label")

        self.gridLayout.addWidget(self.surname_label, 0, 0, 1, 1)

        self.name_radioButton = QRadioButton(self.centralwidget)
        self.name_radioButton.setObjectName(u"name_radioButton")
        self.name_radioButton.setAutoExclusive(False)

        self.gridLayout.addWidget(self.name_radioButton, 0, 1, 1, 1)

        self.surname_plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.surname_plainTextEdit.setObjectName(u"surname_plainTextEdit")
        self.surname_plainTextEdit.setMaximumSize(QSize(16777215, 28))
        self.surname_plainTextEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.surname_plainTextEdit, 1, 0, 1, 1)

        self.name_plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.name_plainTextEdit.setObjectName(u"name_plainTextEdit")
        self.name_plainTextEdit.setMaximumSize(QSize(16777215, 28))
        self.name_plainTextEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.name_plainTextEdit, 1, 1, 1, 2)

        self.birth_date_radioButton = QRadioButton(self.centralwidget)
        self.birth_date_radioButton.setObjectName(u"birth_date_radioButton")
        self.birth_date_radioButton.setAutoExclusive(False)

        self.gridLayout.addWidget(self.birth_date_radioButton, 2, 0, 1, 1)

        self.birth_date_plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.birth_date_plainTextEdit.setObjectName(u"birth_date_plainTextEdit")
        self.birth_date_plainTextEdit.setMaximumSize(QSize(16777215, 28))
        self.birth_date_plainTextEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.birth_date_plainTextEdit, 3, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 51, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 3)

        self.key_plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.key_plainTextEdit.setObjectName(u"key_plainTextEdit")
        self.key_plainTextEdit.setMaximumSize(QSize(16777215, 28))
        self.key_plainTextEdit.setReadOnly(False)

        self.gridLayout.addWidget(self.key_plainTextEdit, 8, 0, 1, 3)

        self.ok_pushButton = QPushButton(self.centralwidget)
        self.ok_pushButton.setObjectName(u"ok_pushButton")

        self.gridLayout.addWidget(self.ok_pushButton, 9, 1, 1, 1)

        self.cancel_pushButton = QPushButton(self.centralwidget)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")

        self.gridLayout.addWidget(self.cancel_pushButton, 9, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 10, 0, 1, 3)

        self.generate_pushButton = QPushButton(self.centralwidget)
        self.generate_pushButton.setObjectName(u"generate_pushButton")

        self.gridLayout.addWidget(self.generate_pushButton, 5, 0, 1, 3)

        self.copy_pushButton = QPushButton(self.centralwidget)
        self.copy_pushButton.setObjectName(u"copy_pushButton")

        self.gridLayout.addWidget(self.copy_pushButton, 6, 0, 1, 3)

        self.key_label = QLabel(self.centralwidget)
        self.key_label.setObjectName(u"key_label")

        self.gridLayout.addWidget(self.key_label, 7, 0, 1, 1)

        self.state_key_label = QLabel(self.centralwidget)
        self.state_key_label.setObjectName(u"state_key_label")
        font = QFont()
        font.setItalic(True)
        self.state_key_label.setFont(font)
        self.state_key_label.setLayoutDirection(Qt.LeftToRight)
        self.state_key_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.state_key_label, 7, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 26))
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTools.menuAction())
        self.menuTools.addAction(self.history)
        self.menuTools.addAction(self.save)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.history.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.surname_label.setText(QCoreApplication.translate("MainWindow", u"Surname", None))
        self.name_radioButton.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.birth_date_radioButton.setText(QCoreApplication.translate("MainWindow", u"Birth date", None))
        self.ok_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.generate_pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.copy_pushButton.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.key_label.setText(QCoreApplication.translate("MainWindow", u"Key", None))
        self.state_key_label.setText(QCoreApplication.translate("MainWindow", u"state", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi