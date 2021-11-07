# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 404)
        self.slider = QSlider(Form)
        self.slider.setObjectName(u"slider")
        self.slider.setGeometry(QRect(120, 340, 160, 22))
        self.slider.setMaximum(100)
        self.slider.setSingleStep(5)
        self.slider.setValue(50)
        self.slider.setOrientation(Qt.Horizontal)
        self.btn_up = QPushButton(Form)
        self.btn_up.setObjectName(u"btn_up")
        self.btn_up.setGeometry(QRect(90, 370, 75, 24))
        self.btn_down = QPushButton(Form)
        self.btn_down.setObjectName(u"btn_down")
        self.btn_down.setGeometry(QRect(230, 370, 75, 24))
        self.pb = QProgressBar(Form)
        self.pb.setObjectName(u"pb")
        self.pb.setGeometry(QRect(17, 12, 371, 321))
        self.pb.setValue(24)
        self.pb.setTextVisible(False)
        self.pb.setOrientation(Qt.Vertical)
        self.pb.setInvertedAppearance(True)
        self.pb.setTextDirection(QProgressBar.TopToBottom)

        self.retranslateUi(Form)
        self.btn_up.pressed.connect(Form.up)
        self.btn_up.released.connect(Form.stop)
        self.btn_down.pressed.connect(Form.down)
        self.btn_down.released.connect(Form.stop)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_up.setText(QCoreApplication.translate("Form", u"up", None))
        self.btn_down.setText(QCoreApplication.translate("Form", u"down", None))
    # retranslateUi

