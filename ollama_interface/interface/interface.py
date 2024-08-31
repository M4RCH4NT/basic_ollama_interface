# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1745, 1035)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.inference_page = QtWidgets.QWidget()
        self.inference_page.setObjectName("inference_page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.inference_page)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.inference_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 21))
        self.label.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.list_instructions = QtWidgets.QListWidget(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list_instructions.setFont(font)
        self.list_instructions.setObjectName("list_instructions")
        self.verticalLayout.addWidget(self.list_instructions)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(0, 21))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.list_models = QtWidgets.QListWidget(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list_models.setFont(font)
        self.list_models.setObjectName("list_models")
        self.verticalLayout.addWidget(self.list_models)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.inference_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setMinimumSize(QtCore.QSize(0, 21))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.plaintext_input = QtWidgets.QPlainTextEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plaintext_input.setFont(font)
        self.plaintext_input.setObjectName("plaintext_input")
        self.verticalLayout_2.addWidget(self.plaintext_input)
        self.button_process_text = QtWidgets.QPushButton(self.frame_2)
        self.button_process_text.setMinimumSize(QtCore.QSize(0, 41))
        self.button_process_text.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_process_text.setFont(font)
        self.button_process_text.setObjectName("button_process_text")
        self.verticalLayout_2.addWidget(self.button_process_text)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.inference_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setMinimumSize(QtCore.QSize(0, 21))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.plaintext_output = QtWidgets.QTextEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plaintext_output.setFont(font)
        self.plaintext_output.setObjectName("plaintext_output")
        self.verticalLayout_3.addWidget(self.plaintext_output)
        self.button_copy_text = QtWidgets.QPushButton(self.frame_3)
        self.button_copy_text.setMinimumSize(QtCore.QSize(0, 41))
        self.button_copy_text.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_copy_text.setFont(font)
        self.button_copy_text.setObjectName("button_copy_text")
        self.verticalLayout_3.addWidget(self.button_copy_text)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.inference_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.settings_page)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_6 = QtWidgets.QFrame(self.settings_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.list_instructions_settings = QtWidgets.QListWidget(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list_instructions_settings.setFont(font)
        self.list_instructions_settings.setObjectName("list_instructions_settings")
        self.verticalLayout_5.addWidget(self.list_instructions_settings)
        self.horizontalLayout_5.addWidget(self.frame_6)
        self.frame_9 = QtWidgets.QFrame(self.settings_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_13 = QtWidgets.QLabel(self.frame_7)
        self.label_13.setMinimumSize(QtCore.QSize(0, 25))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_6.addWidget(self.label_13)
        self.line_edit_selected_title = QtWidgets.QLineEdit(self.frame_7)
        self.line_edit_selected_title.setMinimumSize(QtCore.QSize(0, 30))
        self.line_edit_selected_title.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_edit_selected_title.setFont(font)
        self.line_edit_selected_title.setText("")
        self.line_edit_selected_title.setReadOnly(False)
        self.line_edit_selected_title.setObjectName("line_edit_selected_title")
        self.verticalLayout_6.addWidget(self.line_edit_selected_title)
        self.label_12 = QtWidgets.QLabel(self.frame_7)
        self.label_12.setMinimumSize(QtCore.QSize(0, 25))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.plaintext_selected_prompt = QtWidgets.QPlainTextEdit(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plaintext_selected_prompt.setFont(font)
        self.plaintext_selected_prompt.setObjectName("plaintext_selected_prompt")
        self.verticalLayout_6.addWidget(self.plaintext_selected_prompt)
        self.button_save_selected = QtWidgets.QPushButton(self.frame_7)
        self.button_save_selected.setMinimumSize(QtCore.QSize(0, 35))
        self.button_save_selected.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_save_selected.setFont(font)
        self.button_save_selected.setObjectName("button_save_selected")
        self.verticalLayout_6.addWidget(self.button_save_selected)
        self.button_remove_selected = QtWidgets.QPushButton(self.frame_7)
        self.button_remove_selected.setMinimumSize(QtCore.QSize(0, 35))
        self.button_remove_selected.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_remove_selected.setFont(font)
        self.button_remove_selected.setObjectName("button_remove_selected")
        self.verticalLayout_6.addWidget(self.button_remove_selected)
        self.verticalLayout_8.addWidget(self.frame_7)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.frame_8 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.frame_8)
        self.label_11.setMinimumSize(QtCore.QSize(0, 25))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.line_edit_new_title = QtWidgets.QLineEdit(self.frame_8)
        self.line_edit_new_title.setMinimumSize(QtCore.QSize(0, 30))
        self.line_edit_new_title.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_edit_new_title.setFont(font)
        self.line_edit_new_title.setText("")
        self.line_edit_new_title.setObjectName("line_edit_new_title")
        self.verticalLayout_7.addWidget(self.line_edit_new_title)
        self.label_10 = QtWidgets.QLabel(self.frame_8)
        self.label_10.setMinimumSize(QtCore.QSize(0, 25))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.plaintext_new_prompt = QtWidgets.QPlainTextEdit(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plaintext_new_prompt.setFont(font)
        self.plaintext_new_prompt.setObjectName("plaintext_new_prompt")
        self.verticalLayout_7.addWidget(self.plaintext_new_prompt)
        self.button_add_new_instruction = QtWidgets.QPushButton(self.frame_8)
        self.button_add_new_instruction.setMinimumSize(QtCore.QSize(0, 35))
        self.button_add_new_instruction.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_add_new_instruction.setFont(font)
        self.button_add_new_instruction.setObjectName("button_add_new_instruction")
        self.verticalLayout_7.addWidget(self.button_add_new_instruction)
        self.verticalLayout_8.addWidget(self.frame_8)
        self.horizontalLayout_5.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.settings_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_5.addWidget(self.frame_10)
        self.stackedWidget.addWidget(self.settings_page)
        self.promp_page = QtWidgets.QWidget()
        self.promp_page.setObjectName("promp_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.promp_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.plaintext_input_prompt = QtWidgets.QPlainTextEdit(self.promp_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.plaintext_input_prompt.sizePolicy().hasHeightForWidth())
        self.plaintext_input_prompt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plaintext_input_prompt.setFont(font)
        self.plaintext_input_prompt.setObjectName("plaintext_input_prompt")
        self.verticalLayout_4.addWidget(self.plaintext_input_prompt)
        self.frame_4 = QtWidgets.QFrame(self.promp_page)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 81))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setMinimumSize(QtCore.QSize(131, 61))
        self.label_5.setMaximumSize(QtCore.QSize(131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.plaintext_system_prompt = QtWidgets.QPlainTextEdit(self.frame_4)
        self.plaintext_system_prompt.setMinimumSize(QtCore.QSize(0, 61))
        self.plaintext_system_prompt.setMaximumSize(QtCore.QSize(16777215, 61))
        self.plaintext_system_prompt.setObjectName("plaintext_system_prompt")
        self.horizontalLayout_3.addWidget(self.plaintext_system_prompt)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.promp_page)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 61))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkbox_jsonify = QtWidgets.QCheckBox(self.frame_5)
        self.checkbox_jsonify.setMinimumSize(QtCore.QSize(131, 41))
        self.checkbox_jsonify.setMaximumSize(QtCore.QSize(131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkbox_jsonify.setFont(font)
        self.checkbox_jsonify.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkbox_jsonify.setObjectName("checkbox_jsonify")
        self.horizontalLayout_4.addWidget(self.checkbox_jsonify)
        spacerItem1 = QtWidgets.QSpacerItem(161, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.combo_model_list = QtWidgets.QComboBox(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_model_list.sizePolicy().hasHeightForWidth())
        self.combo_model_list.setSizePolicy(sizePolicy)
        self.combo_model_list.setMinimumSize(QtCore.QSize(100, 41))
        self.combo_model_list.setMaximumSize(QtCore.QSize(251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.combo_model_list.setFont(font)
        self.combo_model_list.setObjectName("combo_model_list")
        self.horizontalLayout_4.addWidget(self.combo_model_list)
        self.button_process_text_prompt = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_process_text_prompt.sizePolicy().hasHeightForWidth())
        self.button_process_text_prompt.setSizePolicy(sizePolicy)
        self.button_process_text_prompt.setMinimumSize(QtCore.QSize(100, 41))
        self.button_process_text_prompt.setMaximumSize(QtCore.QSize(251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_process_text_prompt.setFont(font)
        self.button_process_text_prompt.setObjectName("button_process_text_prompt")
        self.horizontalLayout_4.addWidget(self.button_process_text_prompt)
        self.button_clear_chat = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_clear_chat.sizePolicy().hasHeightForWidth())
        self.button_clear_chat.setSizePolicy(sizePolicy)
        self.button_clear_chat.setMinimumSize(QtCore.QSize(100, 41))
        self.button_clear_chat.setMaximumSize(QtCore.QSize(251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_clear_chat.setFont(font)
        self.button_clear_chat.setObjectName("button_clear_chat")
        self.horizontalLayout_4.addWidget(self.button_clear_chat)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(161, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.plaintext_output_prompt = QtWidgets.QTextEdit(self.promp_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.plaintext_output_prompt.sizePolicy().hasHeightForWidth())
        self.plaintext_output_prompt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plaintext_output_prompt.setFont(font)
        self.plaintext_output_prompt.setObjectName("plaintext_output_prompt")
        self.verticalLayout_4.addWidget(self.plaintext_output_prompt)
        self.stackedWidget.addWidget(self.promp_page)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1745, 21))
        self.menubar.setObjectName("menubar")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPrompt = QtWidgets.QAction(MainWindow)
        self.actionPrompt.setObjectName("actionPrompt")
        self.actionInference = QtWidgets.QAction(MainWindow)
        self.actionInference.setObjectName("actionInference")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSwitch_To_Small = QtWidgets.QAction(MainWindow)
        self.actionSwitch_To_Small.setObjectName("actionSwitch_To_Small")
        self.menuWindow.addAction(self.actionPrompt)
        self.menuWindow.addAction(self.actionInference)
        self.menuWindow.addAction(self.actionSettings)
        self.menuWindow.addAction(self.actionSwitch_To_Small)
        self.menubar.addAction(self.menuWindow.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Instruction List"))
        self.label_2.setText(_translate("MainWindow", "Model List"))
        self.label_3.setText(_translate("MainWindow", "Input Text"))
        self.button_process_text.setText(_translate("MainWindow", "Process Text"))
        self.label_4.setText(_translate("MainWindow", "Model Output"))
        self.button_copy_text.setText(_translate("MainWindow", "Copy Text To Input"))
        self.label_6.setText(_translate("MainWindow", "Instruction List"))
        self.label_13.setText(_translate("MainWindow", "Selected Instruction Title"))
        self.label_12.setText(_translate("MainWindow", "Selected Instruction Prompt"))
        self.button_save_selected.setText(_translate("MainWindow", "Save"))
        self.button_remove_selected.setText(_translate("MainWindow", "Remove"))
        self.label_11.setText(_translate("MainWindow", "Instruction Title"))
        self.label_10.setText(_translate("MainWindow", "Instruction Prompt"))
        self.button_add_new_instruction.setText(_translate("MainWindow", "Add"))
        self.label_5.setText(_translate("MainWindow", "System Message:"))
        self.checkbox_jsonify.setText(_translate("MainWindow", "JSONIFY"))
        self.button_process_text_prompt.setText(_translate("MainWindow", "Generate"))
        self.button_clear_chat.setText(_translate("MainWindow", "Clear Chat"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.actionPrompt.setText(_translate("MainWindow", "Chat"))
        self.actionInference.setText(_translate("MainWindow", "Text Inference"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionSwitch_To_Small.setText(_translate("MainWindow", "Switch To Small"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
