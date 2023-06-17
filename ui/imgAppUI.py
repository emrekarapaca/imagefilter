# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/krpc1/OneDrive/Masaüstü/ImgFilterAPP/ImgFilterAPP/ui/imagefilter.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 417)
        MainWindow.setMinimumSize(QtCore.QSize(825, 417))
        MainWindow.setMaximumSize(QtCore.QSize(825, 417))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.segmentation_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.segmentation_groupBox.setGeometry(QtCore.QRect(10, 207, 180, 85))
        self.segmentation_groupBox.setObjectName("segmentation_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.segmentation_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.multi_otsu_button = QtWidgets.QPushButton(self.segmentation_groupBox)
        self.multi_otsu_button.setObjectName("multi_otsu_button")
        self.gridLayout.addWidget(self.multi_otsu_button, 0, 0, 1, 1)
        self.chan_vese_button = QtWidgets.QPushButton(self.segmentation_groupBox)
        self.chan_vese_button.setObjectName("chan_vese_button")
        self.gridLayout.addWidget(self.chan_vese_button, 0, 1, 1, 1)
        self.morphological_snakes_button = QtWidgets.QPushButton(self.segmentation_groupBox)
        self.morphological_snakes_button.setObjectName("morphological_snakes_button")
        self.gridLayout.addWidget(self.morphological_snakes_button, 1, 0, 1, 1)
        self.conversion_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.conversion_groupBox.setGeometry(QtCore.QRect(10, 145, 176, 56))
        self.conversion_groupBox.setObjectName("conversion_groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.conversion_groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rgb_to_gs_button = QtWidgets.QPushButton(self.conversion_groupBox)
        self.rgb_to_gs_button.setObjectName("rgb_to_gs_button")
        self.horizontalLayout.addWidget(self.rgb_to_gs_button)
        self.rgb_to_hsv_button = QtWidgets.QPushButton(self.conversion_groupBox)
        self.rgb_to_hsv_button.setObjectName("rgb_to_hsv_button")
        self.horizontalLayout.addWidget(self.rgb_to_hsv_button)
        self.source_output_tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.source_output_tab_widget.setGeometry(QtCore.QRect(10, 10, 180, 129))
        self.source_output_tab_widget.setObjectName("source_output_tab_widget")
        self.source_tab_widget = QtWidgets.QWidget()
        self.source_tab_widget.setObjectName("source_tab_widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.source_tab_widget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.open_source_button = QtWidgets.QPushButton(self.source_tab_widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/open_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_source_button.setIcon(icon1)
        self.open_source_button.setObjectName("open_source_button")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.open_source_button)
        self.export_as_source_button = QtWidgets.QPushButton(self.source_tab_widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/export_as_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_as_source_button.setIcon(icon2)
        self.export_as_source_button.setObjectName("export_as_source_button")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.export_as_source_button)
        self.clear_source_button = QtWidgets.QPushButton(self.source_tab_widget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/clear_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_source_button.setIcon(icon3)
        self.clear_source_button.setObjectName("clear_source_button")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.clear_source_button)
        self.source_output_tab_widget.addTab(self.source_tab_widget, "")
        self.output_tab_widget = QtWidgets.QWidget()
        self.output_tab_widget.setObjectName("output_tab_widget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.output_tab_widget)
        self.formLayout_3.setObjectName("formLayout_3")
        self.save_output_button = QtWidgets.QPushButton(self.output_tab_widget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/save_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_output_button.setIcon(icon4)
        self.save_output_button.setObjectName("save_output_button")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.save_output_button)
        self.undo_output_button = QtWidgets.QPushButton(self.output_tab_widget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/undo_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undo_output_button.setIcon(icon5)
        self.undo_output_button.setObjectName("undo_output_button")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.undo_output_button)
        self.save_as_output_button = QtWidgets.QPushButton(self.output_tab_widget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/save_as_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_as_output_button.setIcon(icon6)
        self.save_as_output_button.setObjectName("save_as_output_button")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.save_as_output_button)
        self.redo_output_button = QtWidgets.QPushButton(self.output_tab_widget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/redo_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redo_output_button.setIcon(icon7)
        self.redo_output_button.setObjectName("redo_output_button")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.redo_output_button)
        self.export_as_output_button = QtWidgets.QPushButton(self.output_tab_widget)
        self.export_as_output_button.setIcon(icon2)
        self.export_as_output_button.setObjectName("export_as_output_button")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.export_as_output_button)
        self.clear_output_button = QtWidgets.QPushButton(self.output_tab_widget)
        self.clear_output_button.setIcon(icon3)
        self.clear_output_button.setObjectName("clear_output_button")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.clear_output_button)
        self.source_output_tab_widget.addTab(self.output_tab_widget, "")
        self.edge_detection_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.edge_detection_groupBox.setGeometry(QtCore.QRect(10, 298, 176, 85))
        self.edge_detection_groupBox.setObjectName("edge_detection_groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.edge_detection_groupBox)
        self.formLayout.setObjectName("formLayout")
        self.roberts_button = QtWidgets.QPushButton(self.edge_detection_groupBox)
        self.roberts_button.setObjectName("roberts_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.roberts_button)
        self.sobel_button = QtWidgets.QPushButton(self.edge_detection_groupBox)
        self.sobel_button.setObjectName("sobel_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sobel_button)
        self.scharr_button = QtWidgets.QPushButton(self.edge_detection_groupBox)
        self.scharr_button.setObjectName("scharr_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.scharr_button)
        self.prewitt_button = QtWidgets.QPushButton(self.edge_detection_groupBox)
        self.prewitt_button.setObjectName("prewitt_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.prewitt_button)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 20, 611, 311))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.source_groupBox = QtWidgets.QGroupBox(self.widget)
        self.source_groupBox.setObjectName("source_groupBox")
        self.source_label = QtWidgets.QLabel(self.source_groupBox)
        self.source_label.setGeometry(QtCore.QRect(10, 20, 280, 280))
        self.source_label.setMinimumSize(QtCore.QSize(280, 280))
        self.source_label.setMaximumSize(QtCore.QSize(280, 280))
        self.source_label.setFrameShape(QtWidgets.QFrame.Box)
        self.source_label.setText("")
        self.source_label.setObjectName("source_label")
        self.horizontalLayout_2.addWidget(self.source_groupBox)
        self.output_groupBox = QtWidgets.QGroupBox(self.widget)
        self.output_groupBox.setObjectName("output_groupBox")
        self.output_label = QtWidgets.QLabel(self.output_groupBox)
        self.output_label.setGeometry(QtCore.QRect(10, 20, 280, 280))
        self.output_label.setMinimumSize(QtCore.QSize(280, 280))
        self.output_label.setMaximumSize(QtCore.QSize(280, 280))
        self.output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.output_label.setText("")
        self.output_label.setObjectName("output_label")
        self.horizontalLayout_2.addWidget(self.output_groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 21))
        self.menubar.setObjectName("menubar")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        self.menuExport_as = QtWidgets.QMenu(self.file_menu)
        self.menuExport_as.setIcon(icon2)
        self.menuExport_as.setObjectName("menuExport_as")
        self.edit_menu = QtWidgets.QMenu(self.menubar)
        self.edit_menu.setObjectName("edit_menu")
        self.edit_clear_menu = QtWidgets.QMenu(self.edit_menu)
        self.edit_clear_menu.setIcon(icon3)
        self.edit_clear_menu.setObjectName("edit_clear_menu")
        self.conversion_menu = QtWidgets.QMenu(self.menubar)
        self.conversion_menu.setObjectName("conversion_menu")
        self.segmentation_menu = QtWidgets.QMenu(self.menubar)
        self.segmentation_menu.setObjectName("segmentation_menu")
        self.edge_detection_menu = QtWidgets.QMenu(self.menubar)
        self.edge_detection_menu.setObjectName("edge_detection_menu")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.open_source_action = QtWidgets.QAction(MainWindow)
        self.open_source_action.setIcon(icon1)
        self.open_source_action.setObjectName("open_source_action")
        self.save_output_action = QtWidgets.QAction(MainWindow)
        self.save_output_action.setIcon(icon4)
        self.save_output_action.setObjectName("save_output_action")
        self.save_as_output_action = QtWidgets.QAction(MainWindow)
        self.save_as_output_action.setIcon(icon6)
        self.save_as_output_action.setObjectName("save_as_output_action")
        self.export_as_source_action = QtWidgets.QAction(MainWindow)
        self.export_as_source_action.setObjectName("export_as_source_action")
        self.export_as_output_action = QtWidgets.QAction(MainWindow)
        self.export_as_output_action.setObjectName("export_as_output_action")
        self.close_action = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/close_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_action.setIcon(icon8)
        self.close_action.setObjectName("close_action")
        self.clear_source_action = QtWidgets.QAction(MainWindow)
        self.clear_source_action.setObjectName("clear_source_action")
        self.clear_output_action = QtWidgets.QAction(MainWindow)
        self.clear_output_action.setObjectName("clear_output_action")
        self.undo_output_action = QtWidgets.QAction(MainWindow)
        self.undo_output_action.setIcon(icon5)
        self.undo_output_action.setObjectName("undo_output_action")
        self.redo_output_action = QtWidgets.QAction(MainWindow)
        self.redo_output_action.setIcon(icon7)
        self.redo_output_action.setObjectName("redo_output_action")
        self.rgb_to_gs_action = QtWidgets.QAction(MainWindow)
        self.rgb_to_gs_action.setObjectName("rgb_to_gs_action")
        self.rgb_to_hsv_action = QtWidgets.QAction(MainWindow)
        self.rgb_to_hsv_action.setObjectName("rgb_to_hsv_action")
        self.multi_otsu_action = QtWidgets.QAction(MainWindow)
        self.multi_otsu_action.setObjectName("multi_otsu_action")
        self.chan_vese_action = QtWidgets.QAction(MainWindow)
        self.chan_vese_action.setObjectName("chan_vese_action")
        self.morphological_snakes_action = QtWidgets.QAction(MainWindow)
        self.morphological_snakes_action.setObjectName("morphological_snakes_action")
        self.roberts_action = QtWidgets.QAction(MainWindow)
        self.roberts_action.setObjectName("roberts_action")
        self.sobel_action = QtWidgets.QAction(MainWindow)
        self.sobel_action.setObjectName("sobel_action")
        self.scharr_action = QtWidgets.QAction(MainWindow)
        self.scharr_action.setObjectName("scharr_action")
        self.prewitt_action = QtWidgets.QAction(MainWindow)
        self.prewitt_action.setObjectName("prewitt_action")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/about_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon9)
        self.actionAbout.setObjectName("actionAbout")
        self.menuExport_as.addAction(self.export_as_source_action)
        self.menuExport_as.addAction(self.export_as_output_action)
        self.file_menu.addAction(self.open_source_action)
        self.file_menu.addAction(self.save_output_action)
        self.file_menu.addAction(self.save_as_output_action)
        self.file_menu.addAction(self.menuExport_as.menuAction())
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.close_action)
        self.edit_clear_menu.addAction(self.clear_source_action)
        self.edit_clear_menu.addAction(self.clear_output_action)
        self.edit_menu.addAction(self.edit_clear_menu.menuAction())
        self.edit_menu.addAction(self.undo_output_action)
        self.edit_menu.addAction(self.redo_output_action)
        self.conversion_menu.addAction(self.rgb_to_gs_action)
        self.conversion_menu.addAction(self.rgb_to_hsv_action)
        self.segmentation_menu.addAction(self.multi_otsu_action)
        self.segmentation_menu.addAction(self.chan_vese_action)
        self.segmentation_menu.addAction(self.morphological_snakes_action)
        self.edge_detection_menu.addAction(self.roberts_action)
        self.edge_detection_menu.addAction(self.sobel_action)
        self.edge_detection_menu.addAction(self.scharr_action)
        self.edge_detection_menu.addAction(self.prewitt_action)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.edit_menu.menuAction())
        self.menubar.addAction(self.conversion_menu.menuAction())
        self.menubar.addAction(self.segmentation_menu.menuAction())
        self.menubar.addAction(self.edge_detection_menu.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.source_output_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.source_output_tab_widget, self.open_source_button)
        MainWindow.setTabOrder(self.open_source_button, self.export_as_source_button)
        MainWindow.setTabOrder(self.export_as_source_button, self.clear_source_button)
        MainWindow.setTabOrder(self.clear_source_button, self.save_output_button)
        MainWindow.setTabOrder(self.save_output_button, self.undo_output_button)
        MainWindow.setTabOrder(self.undo_output_button, self.save_as_output_button)
        MainWindow.setTabOrder(self.save_as_output_button, self.redo_output_button)
        MainWindow.setTabOrder(self.redo_output_button, self.export_as_output_button)
        MainWindow.setTabOrder(self.export_as_output_button, self.clear_output_button)
        MainWindow.setTabOrder(self.clear_output_button, self.rgb_to_gs_button)
        MainWindow.setTabOrder(self.rgb_to_gs_button, self.rgb_to_hsv_button)
        MainWindow.setTabOrder(self.rgb_to_hsv_button, self.multi_otsu_button)
        MainWindow.setTabOrder(self.multi_otsu_button, self.chan_vese_button)
        MainWindow.setTabOrder(self.chan_vese_button, self.morphological_snakes_button)
        MainWindow.setTabOrder(self.morphological_snakes_button, self.roberts_button)
        MainWindow.setTabOrder(self.roberts_button, self.sobel_button)
        MainWindow.setTabOrder(self.sobel_button, self.scharr_button)
        MainWindow.setTabOrder(self.scharr_button, self.prewitt_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Filter Application"))
        self.segmentation_groupBox.setTitle(_translate("MainWindow", "Segmentation"))
        self.multi_otsu_button.setText(_translate("MainWindow", "Multi-Otsu"))
        self.chan_vese_button.setText(_translate("MainWindow", "Chan-Vese"))
        self.morphological_snakes_button.setText(_translate("MainWindow", "Morph. Snakes"))
        self.conversion_groupBox.setTitle(_translate("MainWindow", "Conversion"))
        self.rgb_to_gs_button.setText(_translate("MainWindow", "RGB to GS"))
        self.rgb_to_hsv_button.setText(_translate("MainWindow", "RGB to HSV"))
        self.open_source_button.setText(_translate("MainWindow", "Open"))
        self.export_as_source_button.setText(_translate("MainWindow", "Export as"))
        self.clear_source_button.setText(_translate("MainWindow", "Clear"))
        self.source_output_tab_widget.setTabText(self.source_output_tab_widget.indexOf(self.source_tab_widget), _translate("MainWindow", "Source"))
        self.save_output_button.setText(_translate("MainWindow", "Save"))
        self.undo_output_button.setText(_translate("MainWindow", "Undo"))
        self.save_as_output_button.setText(_translate("MainWindow", "Save as"))
        self.redo_output_button.setText(_translate("MainWindow", "Redo"))
        self.export_as_output_button.setText(_translate("MainWindow", "Export as"))
        self.clear_output_button.setText(_translate("MainWindow", "Clear"))
        self.source_output_tab_widget.setTabText(self.source_output_tab_widget.indexOf(self.output_tab_widget), _translate("MainWindow", "Output"))
        self.edge_detection_groupBox.setTitle(_translate("MainWindow", "Edge detection"))
        self.roberts_button.setText(_translate("MainWindow", "Roberts"))
        self.sobel_button.setText(_translate("MainWindow", "Sobel"))
        self.scharr_button.setText(_translate("MainWindow", "Scharr"))
        self.prewitt_button.setText(_translate("MainWindow", "Prewitt"))
        self.source_groupBox.setTitle(_translate("MainWindow", "Source"))
        self.output_groupBox.setTitle(_translate("MainWindow", "Output"))
        self.file_menu.setTitle(_translate("MainWindow", "File"))
        self.menuExport_as.setTitle(_translate("MainWindow", "Export as"))
        self.edit_menu.setTitle(_translate("MainWindow", "Edit"))
        self.edit_clear_menu.setTitle(_translate("MainWindow", "Clear"))
        self.conversion_menu.setTitle(_translate("MainWindow", "Conversion"))
        self.segmentation_menu.setTitle(_translate("MainWindow", "Segmentation"))
        self.edge_detection_menu.setTitle(_translate("MainWindow", "Edge detection"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.open_source_action.setText(_translate("MainWindow", "Open Source"))
        self.open_source_action.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.save_output_action.setText(_translate("MainWindow", "Save Output"))
        self.save_output_action.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.save_as_output_action.setText(_translate("MainWindow", "Save as Output"))
        self.save_as_output_action.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.export_as_source_action.setText(_translate("MainWindow", "Source"))
        self.export_as_output_action.setText(_translate("MainWindow", "Output"))
        self.close_action.setText(_translate("MainWindow", "Close"))
        self.close_action.setShortcut(_translate("MainWindow", "Shift+F4"))
        self.clear_source_action.setText(_translate("MainWindow", "Source"))
        self.clear_output_action.setText(_translate("MainWindow", "Output"))
        self.undo_output_action.setText(_translate("MainWindow", "Undo Output"))
        self.undo_output_action.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.redo_output_action.setText(_translate("MainWindow", "Redo Output"))
        self.redo_output_action.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.rgb_to_gs_action.setText(_translate("MainWindow", "RGB to Grayscale"))
        self.rgb_to_hsv_action.setText(_translate("MainWindow", "RGB to HSV"))
        self.multi_otsu_action.setText(_translate("MainWindow", "Multi-Otsu"))
        self.chan_vese_action.setText(_translate("MainWindow", "Chan-Vese"))
        self.morphological_snakes_action.setText(_translate("MainWindow", "Morphological Snakes"))
        self.roberts_action.setText(_translate("MainWindow", "Roberts"))
        self.sobel_action.setText(_translate("MainWindow", "Sobel"))
        self.scharr_action.setText(_translate("MainWindow", "Scharr"))
        self.prewitt_action.setText(_translate("MainWindow", "Prewitt"))
        self.actionAbout.setText(_translate("MainWindow", "About"))