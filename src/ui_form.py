# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frameTableWeather = QFrame(Widget)
        self.frameTableWeather.setObjectName(u"frameTableWeather")
        self.frameTableWeather.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTableWeather.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frameTableWeather)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frameTableWeather)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.tableWeather = QTableWidget(self.frameTableWeather)
        self.tableWeather.setObjectName(u"tableWeather")

        self.verticalLayout.addWidget(self.tableWeather)

        self.widget_3 = QWidget(self.frameTableWeather)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_rafraichir = QPushButton(self.widget_3)
        self.btn_rafraichir.setObjectName(u"btn_rafraichir")

        self.horizontalLayout_2.addWidget(self.btn_rafraichir)

        self.btn_ajouter = QPushButton(self.widget_3)
        self.btn_ajouter.setObjectName(u"btn_ajouter")

        self.horizontalLayout_2.addWidget(self.btn_ajouter)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.frameTableWeather)

        self.widget_2 = QWidget(Widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frameInput = QFrame(self.widget_2)
        self.frameInput.setObjectName(u"frameInput")
        self.frameInput.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameInput.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frameInput)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_6 = QWidget(self.frameInput)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout = QGridLayout(self.widget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)

        self.lineEdit_ville = QLineEdit(self.widget_6)
        self.lineEdit_ville.setObjectName(u"lineEdit_ville")
        self.lineEdit_ville.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.lineEdit_ville, 0, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.frameInput)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_obtenir = QPushButton(self.widget_7)
        self.btn_obtenir.setObjectName(u"btn_obtenir")

        self.horizontalLayout_3.addWidget(self.btn_obtenir)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.widget_7)


        self.verticalLayout_2.addWidget(self.frameInput)

        self.frameHistory = QFrame(self.widget_2)
        self.frameHistory.setObjectName(u"frameHistory")
        self.frameHistory.setMaximumSize(QSize(16777215, 300))
        self.frameHistory.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameHistory.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameHistory)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frameHistory)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.table_historique = QTableWidget(self.frameHistory)
        self.table_historique.setObjectName(u"table_historique")

        self.verticalLayout_3.addWidget(self.table_historique)


        self.verticalLayout_2.addWidget(self.frameHistory)


        self.horizontalLayout.addWidget(self.widget_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Weather", None))
        self.btn_rafraichir.setText(QCoreApplication.translate("Widget", u"Rafraichir", None))
        self.btn_ajouter.setText(QCoreApplication.translate("Widget", u"Ajouter Ville", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Ville:", None))
        self.btn_obtenir.setText(QCoreApplication.translate("Widget", u"Obtenir la meteo", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Historique de recherche", None))
    # retranslateUi

