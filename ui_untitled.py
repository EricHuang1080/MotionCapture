# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledSfcTEo.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 388)
        Form.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.CamID = QLineEdit(Form)
        self.CamID.setObjectName(u"CamID")

        self.verticalLayout.addWidget(self.CamID)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.height = QLineEdit(Form)
        self.height.setObjectName(u"height")

        self.verticalLayout.addWidget(self.height)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.x_range = QLineEdit(Form)
        self.x_range.setObjectName(u"x_range")

        self.verticalLayout.addWidget(self.x_range)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.y_range = QLineEdit(Form)
        self.y_range.setObjectName(u"y_range")

        self.verticalLayout.addWidget(self.y_range)

        self.OK = QPushButton(Form)
        self.OK.setObjectName(u"OK")
        self.OK.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.OK)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.file_select_btn = QPushButton(Form)
        self.file_select_btn.setObjectName(u"file_select_btn")
        self.file_select_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.file_select_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Camera Calibration", None))
        self.label.setText(QCoreApplication.translate("Form", u"camera ID", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"height", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"X range", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Y range", None))
        self.OK.setText(QCoreApplication.translate("Form", u"OK", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Calibration picture", None))
        self.file_select_btn.setText(QCoreApplication.translate("Form", u"select file", None))
    # retranslateUi

