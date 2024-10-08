# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1564, 890)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_message_headers = QtWidgets.QFrame(self.centralwidget)
        self.frame_message_headers.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_message_headers.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_message_headers.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_message_headers.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_message_headers.setObjectName("frame_message_headers")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_message_headers)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.button_new_chat = QtWidgets.QPushButton(self.frame_message_headers)
        self.button_new_chat.setMinimumSize(QtCore.QSize(0, 40))
        self.button_new_chat.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_new_chat.setFont(font)
        self.button_new_chat.setObjectName("button_new_chat")
        self.verticalLayout_4.addWidget(self.button_new_chat)
        self.messages_scroll_area = QtWidgets.QScrollArea(self.frame_message_headers)
        self.messages_scroll_area.setStyleSheet("")
        self.messages_scroll_area.setWidgetResizable(True)
        self.messages_scroll_area.setObjectName("messages_scroll_area")
        self.messages_scroll_area_content = QtWidgets.QWidget()
        self.messages_scroll_area_content.setGeometry(QtCore.QRect(0, 0, 240, 729))
        self.messages_scroll_area_content.setObjectName("messages_scroll_area_content")
        self.messages_vertical_layout = QtWidgets.QVBoxLayout(self.messages_scroll_area_content)
        self.messages_vertical_layout.setObjectName("messages_vertical_layout")
        self.messages_scroll_area.setWidget(self.messages_scroll_area_content)
        self.verticalLayout_4.addWidget(self.messages_scroll_area)
        self.combo_box_models = QtWidgets.QComboBox(self.frame_message_headers)
        self.combo_box_models.setMinimumSize(QtCore.QSize(0, 40))
        self.combo_box_models.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.combo_box_models.setFont(font)
        self.combo_box_models.setObjectName("combo_box_models")
        self.combo_box_models.addItem("")
        self.combo_box_models.addItem("")
        self.combo_box_models.addItem("")
        self.verticalLayout_4.addWidget(self.combo_box_models)
        self.horizontalLayout_8.addWidget(self.frame_message_headers)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(17, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_hide_message_headers = QtWidgets.QPushButton(self.frame)
        self.button_hide_message_headers.setMinimumSize(QtCore.QSize(15, 80))
        self.button_hide_message_headers.setMaximumSize(QtCore.QSize(15, 80))
        self.button_hide_message_headers.setObjectName("button_hide_message_headers")
        self.verticalLayout_2.addWidget(self.button_hide_message_headers)
        self.horizontalLayout_8.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chat_interface_scroll_area = QtWidgets.QScrollArea(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat_interface_scroll_area.sizePolicy().hasHeightForWidth())
        self.chat_interface_scroll_area.setSizePolicy(sizePolicy)
        self.chat_interface_scroll_area.setWidgetResizable(True)
        self.chat_interface_scroll_area.setObjectName("chat_interface_scroll_area")
        self.chat_interface_scroll_area_content = QtWidgets.QWidget()
        self.chat_interface_scroll_area_content.setGeometry(QtCore.QRect(0, 0, 1261, 695))
        self.chat_interface_scroll_area_content.setObjectName("chat_interface_scroll_area_content")
        self.chat_interface_vertical_layout = QtWidgets.QVBoxLayout(self.chat_interface_scroll_area_content)
        self.chat_interface_vertical_layout.setObjectName("chat_interface_vertical_layout")
        self.chat_interface_scroll_area.setWidget(self.chat_interface_scroll_area_content)
        self.verticalLayout.addWidget(self.chat_interface_scroll_area)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.input_box_horizontal_layout = QtWidgets.QHBoxLayout(self.frame_3)
        self.input_box_horizontal_layout.setObjectName("input_box_horizontal_layout")
        self.button_attach_file = QtWidgets.QPushButton(self.frame_3)
        self.button_attach_file.setEnabled(False)
        self.button_attach_file.setMinimumSize(QtCore.QSize(40, 40))
        self.button_attach_file.setMaximumSize(QtCore.QSize(40, 40))
        self.button_attach_file.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("attach.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_attach_file.setIcon(icon)
        self.button_attach_file.setIconSize(QtCore.QSize(35, 35))
        self.button_attach_file.setObjectName("button_attach_file")
        self.input_box_horizontal_layout.addWidget(self.button_attach_file)
        self.text_input_prompt = QtWidgets.QPlainTextEdit(self.frame_3)
        self.text_input_prompt.setEnabled(False)
        self.text_input_prompt.setMinimumSize(QtCore.QSize(0, 40))
        self.text_input_prompt.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_input_prompt.setFont(font)
        self.text_input_prompt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_input_prompt.setObjectName("text_input_prompt")
        self.input_box_horizontal_layout.addWidget(self.text_input_prompt)
        self.button_send_chat = QtWidgets.QPushButton(self.frame_3)
        self.button_send_chat.setEnabled(False)
        self.button_send_chat.setMinimumSize(QtCore.QSize(40, 40))
        self.button_send_chat.setMaximumSize(QtCore.QSize(40, 40))
        self.button_send_chat.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("button_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_send_chat.setIcon(icon1)
        self.button_send_chat.setIconSize(QtCore.QSize(35, 35))
        self.button_send_chat.setObjectName("button_send_chat")
        self.input_box_horizontal_layout.addWidget(self.button_send_chat)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout_8.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1564, 21))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSwitch_To_Small = QtWidgets.QAction(MainWindow)
        self.actionSwitch_To_Small.setObjectName("actionSwitch_To_Small")
        self.actionSwitch_To_Big = QtWidgets.QAction(MainWindow)
        self.actionSwitch_To_Big.setObjectName("actionSwitch_To_Big")
        self.menuMain.addAction(self.actionSwitch_To_Small)
        self.menuMain.addAction(self.actionSwitch_To_Big)
        self.menubar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ollama Chat"))
        self.button_new_chat.setText(_translate("MainWindow", "New Chat"))
        self.combo_box_models.setItemText(0, _translate("MainWindow", "Model 1"))
        self.combo_box_models.setItemText(1, _translate("MainWindow", "Model 2"))
        self.combo_box_models.setItemText(2, _translate("MainWindow", "Model 3"))
        self.button_hide_message_headers.setText(_translate("MainWindow", "<\n"
"<\n"
"<"))
        self.text_input_prompt.setPlaceholderText(_translate("MainWindow", "Message Ollama"))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.actionSwitch_To_Small.setText(_translate("MainWindow", "Switch To Small"))
        self.actionSwitch_To_Big.setText(_translate("MainWindow", "Switch To Big"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
