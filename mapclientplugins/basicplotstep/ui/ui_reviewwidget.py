# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reviewwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mapclientplugins.basicplotstep.ui.matplotlibwidget import MatplotlibWidget


class Ui_ReviewWidget(object):
    def setupUi(self, ReviewWidget):
        if not ReviewWidget.objectName():
            ReviewWidget.setObjectName(u"ReviewWidget")
        ReviewWidget.resize(592, 467)
        self.horizontalLayout = QHBoxLayout(ReviewWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(ReviewWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButtonClear = QPushButton(self.groupBox)
        self.pushButtonClear.setObjectName(u"pushButtonClear")

        self.verticalLayout.addWidget(self.pushButtonClear)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButtonDone = QPushButton(self.groupBox)
        self.pushButtonDone.setObjectName(u"pushButtonDone")

        self.verticalLayout.addWidget(self.pushButtonDone)


        self.horizontalLayout.addWidget(self.groupBox)

        self.widgetPlot = MatplotlibWidget(ReviewWidget)
        self.widgetPlot.setObjectName(u"widgetPlot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetPlot.sizePolicy().hasHeightForWidth())
        self.widgetPlot.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.widgetPlot)


        self.retranslateUi(ReviewWidget)

        QMetaObject.connectSlotsByName(ReviewWidget)
    # setupUi

    def retranslateUi(self, ReviewWidget):
        ReviewWidget.setWindowTitle(QCoreApplication.translate("ReviewWidget", u"Review", None))
        self.groupBox.setTitle("")
        self.pushButtonClear.setText(QCoreApplication.translate("ReviewWidget", u"Clear", None))
        self.pushButtonDone.setText(QCoreApplication.translate("ReviewWidget", u"Done", None))
    # retranslateUi

