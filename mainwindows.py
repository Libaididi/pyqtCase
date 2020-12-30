# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowfcwozM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(857, 798)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"QGroupBox{border:1px ridge gray;margin-top: 1ex;} QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, 30, -1)
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_time_elapsed = QLabel(self.groupBox_3)
        self.label_time_elapsed.setObjectName(u"label_time_elapsed")
        font2 = QFont()
        font2.setFamily(u"Ubuntu Mono")
        font2.setPointSize(12)
        self.label_time_elapsed.setFont(font2)

        self.gridLayout_2.addWidget(self.label_time_elapsed, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.progressBar_total = QProgressBar(self.groupBox_3)
        self.progressBar_total.setObjectName(u"progressBar_total")
        sizePolicy1.setHeightForWidth(self.progressBar_total.sizePolicy().hasHeightForWidth())
        self.progressBar_total.setSizePolicy(sizePolicy1)
        self.progressBar_total.setFont(font2)
        self.progressBar_total.setStyleSheet(u"")
        self.progressBar_total.setMaximum(1000)
        self.progressBar_total.setValue(0)
        self.progressBar_total.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.progressBar_total, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.progressBar_current = QProgressBar(self.groupBox_3)
        self.progressBar_current.setObjectName(u"progressBar_current")
        sizePolicy1.setHeightForWidth(self.progressBar_current.sizePolicy().hasHeightForWidth())
        self.progressBar_current.setSizePolicy(sizePolicy1)
        self.progressBar_current.setFont(font2)
        self.progressBar_current.setStyleSheet(u"/*\n"
"QProgressBar {\n"
"	border: 2px solid gray;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: rgba(0, 200, 0);\n"
"	width: 1px;\n"
"}*/")
        self.progressBar_current.setMaximum(1000)
        self.progressBar_current.setValue(0)
        self.progressBar_current.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.progressBar_current, 2, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 3)

        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"QGroupBox{border:1px ridge gray;margin-top: 1ex;} QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.pushButton_start = QPushButton(self.groupBox_2)
        self.pushButton_start.setObjectName(u"pushButton_start")
        sizePolicy1.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy1)
        self.pushButton_start.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton_start)

        self.pushButton_cancel = QPushButton(self.groupBox_2)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy1)
        self.pushButton_cancel.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton_cancel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)

        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox_config = QGroupBox(self.centralwidget)
        self.groupBox_config.setObjectName(u"groupBox_config")
        sizePolicy1.setHeightForWidth(self.groupBox_config.sizePolicy().hasHeightForWidth())
        self.groupBox_config.setSizePolicy(sizePolicy1)
        self.groupBox_config.setFont(font)
        self.groupBox_config.setStyleSheet(u"QGroupBox{border:1px ridge gray;margin-top: 1ex;} QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_config.setFlat(False)
        self.groupBox_config.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.groupBox_config)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.widget_engine = QWidget(self.groupBox_config)
        self.widget_engine.setObjectName(u"widget_engine")
        self.horizontalLayout = QHBoxLayout(self.widget_engine)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_google = QRadioButton(self.widget_engine)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_google)
        self.radioButton_google.setObjectName(u"radioButton_google")
        self.radioButton_google.setFont(font1)
        self.radioButton_google.setFocusPolicy(Qt.StrongFocus)
        self.radioButton_google.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_google)

        self.radioButton_bing = QRadioButton(self.widget_engine)
        self.buttonGroup.addButton(self.radioButton_bing)
        self.radioButton_bing.setObjectName(u"radioButton_bing")
        self.radioButton_bing.setFont(font1)
        self.radioButton_bing.setFocusPolicy(Qt.StrongFocus)

        self.horizontalLayout.addWidget(self.radioButton_bing)

        self.radioButton_baidu = QRadioButton(self.widget_engine)
        self.buttonGroup.addButton(self.radioButton_baidu)
        self.radioButton_baidu.setObjectName(u"radioButton_baidu")
        self.radioButton_baidu.setFont(font1)
        self.radioButton_baidu.setFocusPolicy(Qt.StrongFocus)

        self.horizontalLayout.addWidget(self.radioButton_baidu)


        self.verticalLayout.addWidget(self.widget_engine)

        self.widget_driver = QWidget(self.groupBox_config)
        self.widget_driver.setObjectName(u"widget_driver")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_driver)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton_chrome_headless = QRadioButton(self.widget_driver)
        self.radioButton_chrome_headless.setObjectName(u"radioButton_chrome_headless")
        self.radioButton_chrome_headless.setFont(font1)
        self.radioButton_chrome_headless.setChecked(True)

        self.horizontalLayout_6.addWidget(self.radioButton_chrome_headless)

        self.radioButton_chrome = QRadioButton(self.widget_driver)
        self.radioButton_chrome.setObjectName(u"radioButton_chrome")
        self.radioButton_chrome.setFont(font1)

        self.horizontalLayout_6.addWidget(self.radioButton_chrome)

        self.radioButton_phantomjs = QRadioButton(self.widget_driver)
        self.radioButton_phantomjs.setObjectName(u"radioButton_phantomjs")
        self.radioButton_phantomjs.setFont(font1)

        self.horizontalLayout_6.addWidget(self.radioButton_phantomjs)


        self.verticalLayout.addWidget(self.widget_driver)

        self.widget_keywords = QWidget(self.groupBox_config)
        self.widget_keywords.setObjectName(u"widget_keywords")
        self.gridLayout = QGridLayout(self.widget_keywords)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget_keywords)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_keywords = QLineEdit(self.widget_keywords)
        self.lineEdit_keywords.setObjectName(u"lineEdit_keywords")
        self.lineEdit_keywords.setFont(font1)

        self.gridLayout.addWidget(self.lineEdit_keywords, 0, 1, 1, 2)

        self.checkBox_from_file = QCheckBox(self.widget_keywords)
        self.checkBox_from_file.setObjectName(u"checkBox_from_file")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkBox_from_file.sizePolicy().hasHeightForWidth())
        self.checkBox_from_file.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(12)
        font4.setUnderline(False)
        self.checkBox_from_file.setFont(font4)

        self.gridLayout.addWidget(self.checkBox_from_file, 1, 0, 1, 1)

        self.lineEdit_path2file = QLineEdit(self.widget_keywords)
        self.lineEdit_path2file.setObjectName(u"lineEdit_path2file")
        self.lineEdit_path2file.setEnabled(False)
        self.lineEdit_path2file.setFont(font1)

        self.gridLayout.addWidget(self.lineEdit_path2file, 1, 1, 1, 1)

        self.pushButton_load_file = QPushButton(self.widget_keywords)
        self.pushButton_load_file.setObjectName(u"pushButton_load_file")
        self.pushButton_load_file.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_load_file.sizePolicy().hasHeightForWidth())
        self.pushButton_load_file.setSizePolicy(sizePolicy3)
        self.pushButton_load_file.setFont(font1)

        self.gridLayout.addWidget(self.pushButton_load_file, 1, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 6)
        self.gridLayout.setColumnStretch(2, 1)

        self.verticalLayout.addWidget(self.widget_keywords)

        self.widget_output = QWidget(self.groupBox_config)
        self.widget_output.setObjectName(u"widget_output")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_output)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.widget_output)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.lineEdit_output = QLineEdit(self.widget_output)
        self.lineEdit_output.setObjectName(u"lineEdit_output")
        sizePolicy3.setHeightForWidth(self.lineEdit_output.sizePolicy().hasHeightForWidth())
        self.lineEdit_output.setSizePolicy(sizePolicy3)
        self.lineEdit_output.setFont(font1)

        self.horizontalLayout_5.addWidget(self.lineEdit_output)

        self.pushButton_output = QPushButton(self.widget_output)
        self.pushButton_output.setObjectName(u"pushButton_output")
        self.pushButton_output.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_output.sizePolicy().hasHeightForWidth())
        self.pushButton_output.setSizePolicy(sizePolicy3)
        self.pushButton_output.setFont(font1)

        self.horizontalLayout_5.addWidget(self.pushButton_output)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 6)
        self.horizontalLayout_5.setStretch(2, 1)

        self.verticalLayout.addWidget(self.widget_output)

        self.widget_3 = QWidget(self.groupBox_config)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_face_only = QCheckBox(self.widget_3)
        self.checkBox_face_only.setObjectName(u"checkBox_face_only")
        sizePolicy1.setHeightForWidth(self.checkBox_face_only.sizePolicy().hasHeightForWidth())
        self.checkBox_face_only.setSizePolicy(sizePolicy1)
        self.checkBox_face_only.setFont(font1)

        self.horizontalLayout_4.addWidget(self.checkBox_face_only)

        self.checkBox_safe_mode = QCheckBox(self.widget_3)
        self.checkBox_safe_mode.setObjectName(u"checkBox_safe_mode")
        sizePolicy1.setHeightForWidth(self.checkBox_safe_mode.sizePolicy().hasHeightForWidth())
        self.checkBox_safe_mode.setSizePolicy(sizePolicy1)
        self.checkBox_safe_mode.setFont(font1)
        self.checkBox_safe_mode.setCheckable(True)
        self.checkBox_safe_mode.setChecked(True)

        self.horizontalLayout_4.addWidget(self.checkBox_safe_mode)

        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.spinBox_max_number = QSpinBox(self.widget_3)
        self.spinBox_max_number.setObjectName(u"spinBox_max_number")
        sizePolicy3.setHeightForWidth(self.spinBox_max_number.sizePolicy().hasHeightForWidth())
        self.spinBox_max_number.setSizePolicy(sizePolicy3)
        self.spinBox_max_number.setMinimumSize(QSize(0, 40))
        self.spinBox_max_number.setFont(font1)
        self.spinBox_max_number.setMinimum(1)
        self.spinBox_max_number.setMaximum(2000)
        self.spinBox_max_number.setValue(100)

        self.horizontalLayout_4.addWidget(self.spinBox_max_number)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.spinBox_num_threads = QSpinBox(self.widget_3)
        self.spinBox_num_threads.setObjectName(u"spinBox_num_threads")
        sizePolicy3.setHeightForWidth(self.spinBox_num_threads.sizePolicy().hasHeightForWidth())
        self.spinBox_num_threads.setSizePolicy(sizePolicy3)
        self.spinBox_num_threads.setMinimumSize(QSize(0, 40))
        self.spinBox_num_threads.setFont(font1)
        self.spinBox_num_threads.setMinimum(1)
        self.spinBox_num_threads.setMaximum(200)
        self.spinBox_num_threads.setValue(50)

        self.horizontalLayout_4.addWidget(self.spinBox_num_threads)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(4, 1)
        self.horizontalLayout_4.setStretch(5, 1)

        self.verticalLayout.addWidget(self.widget_3)

        self.widget_proxy = QWidget(self.groupBox_config)
        self.widget_proxy.setObjectName(u"widget_proxy")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_proxy)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 9, -1, 9)
        self.checkBox_proxy = QCheckBox(self.widget_proxy)
        self.checkBox_proxy.setObjectName(u"checkBox_proxy")
        sizePolicy2.setHeightForWidth(self.checkBox_proxy.sizePolicy().hasHeightForWidth())
        self.checkBox_proxy.setSizePolicy(sizePolicy2)
        self.checkBox_proxy.setFont(font1)

        self.horizontalLayout_2.addWidget(self.checkBox_proxy)

        self.widget_5 = QWidget(self.widget_proxy)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setEnabled(False)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.radioButton_http = QRadioButton(self.widget_5)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_http)
        self.radioButton_http.setObjectName(u"radioButton_http")
        sizePolicy1.setHeightForWidth(self.radioButton_http.sizePolicy().hasHeightForWidth())
        self.radioButton_http.setSizePolicy(sizePolicy1)
        self.radioButton_http.setFont(font1)
        self.radioButton_http.setFocusPolicy(Qt.TabFocus)
        self.radioButton_http.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton_http)

        self.radioButton_socks5 = QRadioButton(self.widget_5)
        self.buttonGroup_2.addButton(self.radioButton_socks5)
        self.radioButton_socks5.setObjectName(u"radioButton_socks5")
        sizePolicy1.setHeightForWidth(self.radioButton_socks5.sizePolicy().hasHeightForWidth())
        self.radioButton_socks5.setSizePolicy(sizePolicy1)
        self.radioButton_socks5.setFont(font1)
        self.radioButton_socks5.setFocusPolicy(Qt.TabFocus)
        self.radioButton_socks5.setChecked(False)

        self.horizontalLayout_3.addWidget(self.radioButton_socks5)

        self.lineEdit_proxy = QLineEdit(self.widget_5)
        self.lineEdit_proxy.setObjectName(u"lineEdit_proxy")
        self.lineEdit_proxy.setFont(font1)

        self.horizontalLayout_3.addWidget(self.lineEdit_proxy)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 4)

        self.horizontalLayout_2.addWidget(self.widget_5)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 5)

        self.verticalLayout.addWidget(self.widget_proxy)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 2)
        self.verticalLayout.setStretch(5, 1)

        self.gridLayout_3.addWidget(self.groupBox_config, 0, 0, 1, 1)

        self.plainTextEdit_log = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_log.setObjectName(u"plainTextEdit_log")
        font5 = QFont()
        font5.setFamily(u"Ubuntu Mono")
        self.plainTextEdit_log.setFont(font5)
        self.plainTextEdit_log.setReadOnly(True)
        self.plainTextEdit_log.setTabStopWidth(4)
        self.plainTextEdit_log.setMaximumBlockCount(0)

        self.gridLayout_3.addWidget(self.plainTextEdit_log, 2, 0, 1, 2)

        self.gridLayout_3.setRowStretch(0, 7)
        self.gridLayout_3.setRowStretch(1, 3)
        self.gridLayout_3.setRowStretch(2, 4)
        self.gridLayout_3.setColumnStretch(0, 8)
        self.gridLayout_3.setColumnStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 857, 26))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.lineEdit_keywords)
        self.label_7.setBuddy(self.lineEdit_output)
        self.label_6.setBuddy(self.spinBox_max_number)
        self.label_5.setBuddy(self.spinBox_num_threads)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit_keywords, self.checkBox_from_file)
        QWidget.setTabOrder(self.checkBox_from_file, self.lineEdit_path2file)
        QWidget.setTabOrder(self.lineEdit_path2file, self.pushButton_load_file)
        QWidget.setTabOrder(self.pushButton_load_file, self.lineEdit_output)
        QWidget.setTabOrder(self.lineEdit_output, self.pushButton_output)
        QWidget.setTabOrder(self.pushButton_output, self.checkBox_face_only)
        QWidget.setTabOrder(self.checkBox_face_only, self.checkBox_safe_mode)
        QWidget.setTabOrder(self.checkBox_safe_mode, self.spinBox_max_number)
        QWidget.setTabOrder(self.spinBox_max_number, self.spinBox_num_threads)
        QWidget.setTabOrder(self.spinBox_num_threads, self.checkBox_proxy)
        QWidget.setTabOrder(self.checkBox_proxy, self.radioButton_http)
        QWidget.setTabOrder(self.radioButton_http, self.radioButton_socks5)
        QWidget.setTabOrder(self.radioButton_socks5, self.lineEdit_proxy)
        QWidget.setTabOrder(self.lineEdit_proxy, self.pushButton_start)
        QWidget.setTabOrder(self.pushButton_start, self.pushButton_cancel)
        QWidget.setTabOrder(self.pushButton_cancel, self.radioButton_google)
        QWidget.setTabOrder(self.radioButton_google, self.radioButton_bing)
        QWidget.setTabOrder(self.radioButton_bing, self.radioButton_baidu)
        QWidget.setTabOrder(self.radioButton_baidu, self.plainTextEdit_log)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuAbout.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.checkBox_from_file.clicked.connect(self.lineEdit_keywords.setDisabled)
        self.checkBox_from_file.clicked.connect(self.pushButton_load_file.setEnabled)
        self.checkBox_from_file.clicked.connect(self.lineEdit_path2file.setEnabled)
        self.checkBox_proxy.clicked.connect(self.widget_5.setEnabled)
        self.checkBox_proxy.clicked.connect(self.lineEdit_proxy.setFocus)
        self.radioButton_google.toggled.connect(self.checkBox_safe_mode.setEnabled)
        self.radioButton_bing.toggled.connect(self.checkBox_safe_mode.setChecked)
        self.radioButton_baidu.toggled.connect(self.checkBox_safe_mode.setChecked)
        self.radioButton_google.toggled.connect(self.checkBox_safe_mode.setChecked)
        self.checkBox_from_file.clicked.connect(self.pushButton_load_file.click)
        self.radioButton_baidu.toggled.connect(self.widget_driver.setDisabled)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Progress", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Time Elapsed:", None))
        self.label_time_elapsed.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Total Progress:", None))
        self.progressBar_total.setFormat("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Current Progress:", None))
        self.progressBar_current.setFormat("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
#if QT_CONFIG(shortcut)
        self.pushButton_start.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_cancel.setText(QCoreApplication.translate("MainWindow", u"&Cancel", None))
        self.groupBox_config.setTitle(QCoreApplication.translate("MainWindow", u"Config", None))
        self.radioButton_google.setText(QCoreApplication.translate("MainWindow", u"&Google", None))
        self.radioButton_bing.setText(QCoreApplication.translate("MainWindow", u"&Bing", None))
        self.radioButton_baidu.setText(QCoreApplication.translate("MainWindow", u"B&aidu", None))
        self.radioButton_chrome_headless.setText(QCoreApplication.translate("MainWindow", u"ChromeHeadless", None))
        self.radioButton_chrome.setText(QCoreApplication.translate("MainWindow", u"Chrome", None))
        self.radioButton_phantomjs.setText(QCoreApplication.translate("MainWindow", u"PhantomJs", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"&Keywords:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_keywords.setToolTip(QCoreApplication.translate("MainWindow", u"Input keywords, seperated by comma  \", \"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_keywords.setStatusTip(QCoreApplication.translate("MainWindow", u"Hint: e.g. To download image of Micheal Jordan and Yao Ming, input \"Micheal Jordan, Yao Ming\"", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_keywords.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_keywords.setInputMask("")
        self.lineEdit_keywords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seperates by comma ( , )", None))
        self.checkBox_from_file.setText(QCoreApplication.translate("MainWindow", u"&Load File:", None))
#if QT_CONFIG(statustip)
        self.lineEdit_path2file.setStatusTip(QCoreApplication.translate("MainWindow", u"Hint: Enter path to a text file. Each line of the file contains a group of keywords", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit_path2file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Path to file", None))
        self.pushButton_load_file.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"&Output:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_output.setToolTip(QCoreApplication.translate("MainWindow", u"Path to output directory.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_output.setStatusTip(QCoreApplication.translate("MainWindow", u"Path to output directory.", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit_output.setInputMask("")
        self.lineEdit_output.setText(QCoreApplication.translate("MainWindow", u"./download_images", None))
        self.lineEdit_output.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Path to output directory.", None))
        self.pushButton_output.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBox_face_only.setText(QCoreApplication.translate("MainWindow", u"&Face Only", None))
        self.checkBox_safe_mode.setText(QCoreApplication.translate("MainWindow", u"&Safe Mode", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Max &number\n"
"per keywords", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"&Threads:", None))
        self.checkBox_proxy.setText(QCoreApplication.translate("MainWindow", u"&Proxy:", None))
        self.radioButton_http.setText(QCoreApplication.translate("MainWindow", u"HTTP", None))
        self.radioButton_socks5.setText(QCoreApplication.translate("MainWindow", u"Socks5", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_proxy.setToolTip(QCoreApplication.translate("MainWindow", u"input ip:port", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_proxy.setStatusTip(QCoreApplication.translate("MainWindow", u"xxx.xxx.xxx.xx:port", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit_proxy.setPlaceholderText(QCoreApplication.translate("MainWindow", u"xxx.xxx.xxx.xx:port", None))
        self.plainTextEdit_log.setPlainText("")
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton

import sys
class DemoMain(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  #调用Ui_Mainwindow中的函数setupUi实现显示界面
        #。。。。其他骚操作

        
if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=DemoMain()
    demo.show()
    sys.exit(app.exec_())

