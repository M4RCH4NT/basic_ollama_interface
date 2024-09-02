from interface.interface import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from time import time

import sys, os, json, ollama, subprocess


def infer_text(text, model):

    response = ollama.chat(model=model, messages= [
        {
            "role": "user", 
            "content": text
        }
    ])

    return response["message"]["content"]

def get_heading_for_text(message_body, model, base_model = "phi3", max_char = 1000):

    question = message_body[0]
    answer = message_body[1]

    if len(answer) > max_char :
        answer = answer[:max_char]

    input_prompt = f"Question: {question}\n\nAnswer: {answer}\n\nGive me a short title that decribes this text. It can only be a few words. Only give me the title."

    try:
        response = infer_text(input_prompt, base_model)
    except:
        response = infer_text(input_prompt, model)

    response = str(response).replace('"', "").replace('*', "").replace('#', "").replace("title:", "").replace("Title:", "").split("\n")[0]

    try:
        while response[0] == " ":
            response = response[1:]
    except:
        response = None

    if response != None:
        if len(response) > 100:
            response = response[:100]

    return response

def stream_text(text, model, jsonify = False, system_prompt = ""):
    
    if type(text) == list:

        input_text = []

        if system_prompt != "" :
            
            input_text.append(
                {
                    "role" : "system",
                    "content" : system_prompt
                }
            )

        for idx, text_message in enumerate(text):

            if idx % 2 == 0 :
                input_text.append(
                    {
                        "role" : "user",
                        "content" : text_message
                    }
                )
            else:
                input_text.append(
                    {
                        "role" : "assistant",
                        "content" : text_message
                    }
                )

        if jsonify:
            ollama_iterator = ollama.chat(model=model, format="json", stream=True, messages= input_text)
        else:
            ollama_iterator = ollama.chat(model=model, stream=True, messages= input_text)


        return ollama_iterator

    else:

        if jsonify:
            ollama_iterator = ollama.chat(model=model, format="json", stream=True, messages=[
                {
                    "role" : "user",
                    "content" : text
                }
            ])
        else:
            ollama_iterator = ollama.chat(model=model, stream=True, messages=[
                {
                    "role" : "user",
                    "content" : text
                }
            ])


        return ollama_iterator


class OllamaStreamThread(QtCore.QObject):

    chunk_writer = QtCore.pyqtSignal(str)
    finished = QtCore.pyqtSignal()
    kill_thread = QtCore.pyqtSignal()

    def __init__(self, prompt, model, jsonify_output = False, system_prompt = ""):
        super().__init__()

        self.ollama_model = model
        self.ollama_prompt = prompt
        self.jsonify_output = jsonify_output
        self.system_prompt = system_prompt

    def run(self):

        for chunk in stream_text(self.ollama_prompt, self.ollama_model, self.jsonify_output, self.system_prompt):
            new_letter = chunk['message']['content']   
            self.chunk_writer.emit(new_letter)

        self.finished.emit()
        self.kill_thread.emit()


def load_json_file(filename: str) -> dict:
    with open(filename, 'r') as f:
        return json.load(f)

def save_json_file(filename: str, data: dict):
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=4))
        f.close()



class ClickableQLabel(QtWidgets.QLabel):
    clicked=QtCore.pyqtSignal()

    def mousePressEvent(self, ev):
        self.clicked.emit()



def connect_events(self: Ui_MainWindow):
    
    self.button_attach_file.clicked.connect(self.button_attach_file_clicked)
    self.button_new_chat.clicked.connect(self.button_new_chat_clicked)
    self.button_send_chat.clicked.connect(self.button_send_chat_clicked)
    self.button_hide_message_headers.clicked.connect(self.button_hide_message_headers_clicked) 

    self.mw.set_text_box(self.text_input_prompt)
    self.mw.set_call_function(self.button_send_chat_clicked)

    self.text_input_prompt.installEventFilter(self.mw)

    self.actionSwitch_To_Big.triggered.connect(self.switch_to_big_clicked)
    self.actionSwitch_To_Small.triggered.connect(self.switch_to_small_clicked)

    self.combo_box_models.currentTextChanged.connect(self.combo_box_models_currentTextChanged)

def switch_to_big_clicked(self: Ui_MainWindow):

    subprocess.Popen(["cd", "../ollama_interface", "&","pythonw", "ollama_interface.py"], shell=True)
    QtCore.QCoreApplication.quit()


def combo_box_models_currentTextChanged(self, text):
    if self.finished_loading_models == False:
        return

    self.config["last_used_model"] = self.combo_box_models.currentText()
    save_json_file("config.json", self.config)


def switch_to_small_clicked(self: Ui_MainWindow):

    subprocess.Popen(["cd", "../ollama_interface_small", "&","pythonw", "ollama_interface.py"], shell=True)
    QtCore.QCoreApplication.quit()

def setup_states(self: Ui_MainWindow):
    
    if not os.path.exists("chat_history.json"):
        save_json_file("chat_history.json", {})
        
    self.messages_vertical_layout.setAlignment(QtCore.Qt.AlignTop)

    self.config = load_json_file('config.json')

    self.message_heading_components = []
    self.selected_message_heading = None
    self.selected_message_heading_idx = None

    self.chat_components = []
    self.message_body = None

    self.processing_message = False
    self.message_headers_hidden = False
    self.finished_loading_models = False

    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("interface/attach.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.button_attach_file.setIcon(icon)
    
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("interface/button_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.button_send_chat.setIcon(icon)

    self.chat_interface_vertical_layout.setAlignment(QtCore.Qt.AlignTop)

    font = QtGui.QFont()
    font.setPointSize(self.config["chat_font_size"])

    self.markdown_to_html_converter = QtWidgets.QTextEdit(self.centralwidget)
    self.markdown_to_html_converter.setFont(font)
    self.markdown_to_html_converter.setObjectName("markdown_to_html_converter")
    self.markdown_to_html_converter.hide()

    # Loading ollama models

    last_used_model = self.config["last_used_model"]

    self.combo_box_models.clear()

    self.all_models = [model_entry["name"] for model_entry in ollama.list()["models"]]
    self.all_models.sort()

    for model_name in self.all_models:
        self.combo_box_models.addItem(model_name)


    if last_used_model in self.all_models:
        self.combo_box_models.setCurrentText(last_used_model)
        print(last_used_model)

    if last_used_model == None:
        self.config["last_used_model"] = self.all_models[0]
        save_json_file("config.json", self.config)

    self.finished_loading_models = True

    # Loading messages

    self.load_message_board()



def set_main_window(self: Ui_MainWindow, mw):
    self.mw = mw


def button_attach_file_clicked(self: Ui_MainWindow):
    if self.processing_message :
        return
    
def button_send_chat_clicked(self: Ui_MainWindow):
    if self.processing_message :
        return

    self.input_message = self.text_input_prompt.toPlainText()
    self.selected_model = self.combo_box_models.currentText()

    if self.input_message == "" :
        return
    
    self.text_input_prompt.setPlainText("")

    print(self.input_message, self.selected_model)

    self.button_attach_file.setEnabled(False)
    self.button_new_chat.setEnabled(False)
    self.button_send_chat.setEnabled(False)
    self.text_input_prompt.setEnabled(False)
    self.processing_message = True
    
    self.create_user_chat_panel(len(self.chat_components), self.input_message)

    self.message_body.append(self.input_message)

    self.ai_running_message = ""

    self.create_ai_chat_panel(len(self.chat_components), self.ai_running_message)

    self.thread = QtCore.QThread()
    self.worker = OllamaStreamThread(self.message_body, self.selected_model)

    self.worker.moveToThread(self.thread)

    self.thread.started.connect(self.worker.run)

    self.worker.kill_thread.connect(self.thread.quit)
    self.worker.kill_thread.connect(self.worker.deleteLater)
    self.thread.finished.connect(self.thread.deleteLater)

    self.worker.chunk_writer.connect(self.add_letter_to_chat)
    self.worker.finished.connect(self.done_adding_letters_to_chat)

    self.thread.start()

def button_new_chat_clicked(self: Ui_MainWindow):
    
    if self.processing_message :
        return

    chat_history = load_json_file("chat_history.json")

    new_chat = {
        "message_heading": None,
        "message_body": [],
    }

    new_entry = str(round(time()))

    chat_history[new_entry] = new_chat

    save_json_file("chat_history.json", chat_history)
    
    self.selected_message_heading_idx = 0
    self.selected_message_heading = new_entry

    self.button_attach_file.setEnabled(True)
    self.button_send_chat.setEnabled(True)
    self.text_input_prompt.setEnabled(True)
    
    self.load_message_board()
    self.load_chat_board()

def button_hide_message_headers_clicked(self: Ui_MainWindow):
    
    if self.message_headers_hidden :
        self.frame_message_headers.show()
        self.button_hide_message_headers.setText("<\n<\n<")
    else:
        self.frame_message_headers.hide()
        self.button_hide_message_headers.setText(">\n>\n>")

    self.message_headers_hidden = not self.message_headers_hidden


def add_letter_to_chat(self, added_letter):
    self.ai_running_message += added_letter

    self.markdown_to_html_converter.setMarkdown(self.ai_running_message)
    markdown_content = self.markdown_to_html_converter.toHtml()

    self.chat_components[-1][3].setText(markdown_content)

def done_adding_letters_to_chat(self):
    
    chat_history = load_json_file("chat_history.json")

    self.message_body.append(self.ai_running_message)
    chat_history[self.message_entry_key]["message_body"] = self.message_body

    message_heading = chat_history[self.message_entry_key]["message_heading"]

    if message_heading == None and len(self.message_body) > 1:

        new_heading = get_heading_for_text(self.message_body, self.selected_model)

        chat_history[self.message_entry_key]["message_heading"] = new_heading

    save_json_file("chat_history.json", chat_history)



    self.button_attach_file.setEnabled(True)
    self.button_new_chat.setEnabled(True)
    self.button_send_chat.setEnabled(True)
    self.text_input_prompt.setEnabled(True)
    self.processing_message = False

    self.load_message_board()


def create_message_board_item(self: Ui_MainWindow, idx, message_heading, message_key, make_bold):

    temp_frame = QtWidgets.QFrame(self.messages_scroll_area_content)
    # temp_frame.setMinimumSize(QtCore.QSize(0, 50))
    # temp_frame.setMinimumSize(QtCore.QSize(0, 40))
    # temp_frame.setMaximumSize(QtCore.QSize(16777215, 50))
    # temp_frame.setMaximumSize(QtCore.QSize(16777215, 40))
    temp_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    temp_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    temp_frame.setObjectName(f"message_board_frame_{idx}")

    temp_horizontal_layout = QtWidgets.QHBoxLayout(temp_frame)
    temp_horizontal_layout.setObjectName(f"message_board_horizontal_layout_{idx}")

    temp_label = ClickableQLabel(temp_frame)
    font = QtGui.QFont()
    font.setPointSize(self.config["message_board_font_size"])
    temp_label.setFont(font)
    temp_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
    temp_label.setObjectName(f"message_board_label_{idx}")
    temp_label.setWordWrap(True)
    if make_bold:
        temp_label.setText(f'<html><head/><body><p><span style=" font-weight:600; color:#0bb43b;">{message_heading}</span></p></body></html>')
    else:
        temp_label.setText(message_heading)
        
    temp_horizontal_layout.addWidget(temp_label)
    temp_button = QtWidgets.QPushButton(temp_frame)
    temp_button.setMinimumSize(QtCore.QSize(30, 30))
    temp_button.setMaximumSize(QtCore.QSize(30, 30))
    # temp_button.setMinimumSize(QtCore.QSize(20, 20))
    # temp_button.setMaximumSize(QtCore.QSize(20, 20))
    temp_button.setText("")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("interface/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    temp_button.setIcon(icon)
    temp_button.setIconSize(QtCore.QSize(20, 20))
    # temp_button.setIconSize(QtCore.QSize(15, 15))
    temp_button.setObjectName(f"message_board_button_{idx}")
    temp_horizontal_layout.addWidget(temp_button)
    self.messages_vertical_layout.addWidget(temp_frame)

    temp_frame.show()
    temp_label.show()
    temp_button.show()
    
    print("assigning idx:", idx)


    self.message_heading_components.append([temp_frame, temp_horizontal_layout, temp_label, temp_button])

    temp_button.clicked.connect(lambda: self.message_board_delete_clicked(idx, message_key))
    temp_label.clicked.connect(lambda: self.message_board_item_clicked(idx, message_key))

def load_message_board(self: Ui_MainWindow):
    
    self.delete_message_board()

    chat_history = load_json_file("chat_history.json")

    chat_history_keys = list(chat_history.keys())
    chat_history_keys.reverse()

    for idx, chat_entry in enumerate(chat_history_keys):

        message_heading = chat_history[chat_entry]["message_heading"]

        print("loading", message_heading)

        if message_heading == None:
            message_heading = "New chat"
        
        if idx == self.selected_message_heading_idx:
            create_message_board_item(self, idx, message_heading, chat_entry, True)
            self.message_body = chat_history[chat_entry]["message_body"]
            self.message_entry_key = chat_entry
        else:
            create_message_board_item(self, idx, message_heading, chat_entry, False)

def delete_message_board(self: Ui_MainWindow):

    for idx in range(len(self.message_heading_components)):
        
        self.messages_vertical_layout.removeWidget(self.message_heading_components[idx][0])
        self.message_heading_components[idx][3].deleteLater()
        self.message_heading_components[idx][2].deleteLater()
        self.message_heading_components[idx][1].deleteLater()
        self.message_heading_components[idx][0].deleteLater()
        self.message_heading_components[idx] = None

    self.message_heading_components = []


def message_board_item_clicked(self: Ui_MainWindow, component_idx, message_key):

    if self.processing_message :
        return

    print(component_idx, message_key)
    self.message_heading_components

    self.selected_message_heading_idx = component_idx
    self.selected_message_heading = message_key

    self.button_attach_file.setEnabled(True)
    self.button_send_chat.setEnabled(True)
    self.text_input_prompt.setEnabled(True)

    self.load_message_board()
    self.load_chat_board()

def message_board_delete_clicked(self: Ui_MainWindow, component_idx, message_key):

    if self.processing_message :
        return

    chat_history = load_json_file("chat_history.json")

    if component_idx == self.selected_message_heading_idx:

        self.selected_message_heading_idx = None
        self.selected_message_heading = None
        self.message_body = None
        self.button_attach_file.setEnabled(False)
        self.button_send_chat.setEnabled(False)
        self.text_input_prompt.setEnabled(False)

    chat_history.pop(message_key, None)

    save_json_file("chat_history.json", chat_history)

    self.load_message_board()
    self.load_chat_board()



def create_ai_chat_panel(self: Ui_MainWindow, idx, message_content):


    self.markdown_to_html_converter.setMarkdown(message_content)
    markdown_content = self.markdown_to_html_converter.toHtml()

    temp_frame = QtWidgets.QFrame(self.chat_interface_scroll_area_content)
    temp_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
    temp_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    temp_frame.setObjectName(f"ai_frame_{idx}")
    
    temp_horizontal_layout = QtWidgets.QHBoxLayout(temp_frame)
    temp_horizontal_layout.setAlignment(QtCore.Qt.AlignTop)
    temp_horizontal_layout.setObjectName(f"ai_horizontal_layout_{idx}")
    
    temp_label_ai_icon = QtWidgets.QLabel(temp_frame)
    temp_label_ai_icon.setMinimumSize(QtCore.QSize(40, 40))
    temp_label_ai_icon.setMaximumSize(QtCore.QSize(40, 40))
    temp_label_ai_icon.setText("")
    temp_label_ai_icon.setPixmap(QtGui.QPixmap(".\\interface\\robot.png"))
    temp_label_ai_icon.setScaledContents(True)
    temp_label_ai_icon.setObjectName(f"ai_label_ai_icon_{idx}")
    temp_horizontal_layout.addWidget(temp_label_ai_icon)
    
    temp_label_ai_message = QtWidgets.QLabel(temp_frame)
    font = QtGui.QFont()
    font.setPointSize(self.config["chat_font_size"])
    temp_label_ai_message.setFont(font)
    temp_label_ai_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
    temp_label_ai_message.setWordWrap(True)
    temp_label_ai_message.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
    temp_label_ai_message.setObjectName(f"ai_label_ai_message_{idx}")
    temp_horizontal_layout.addWidget(temp_label_ai_message)
    
    temp_space_frame = QtWidgets.QFrame(temp_frame)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(temp_space_frame.sizePolicy().hasHeightForWidth())
    temp_space_frame.setSizePolicy(sizePolicy)
    temp_space_frame.setMinimumSize(QtCore.QSize(100, 0))
    temp_space_frame.setMaximumSize(QtCore.QSize(100, 16777215))
    temp_space_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
    temp_space_frame.setFrameShadow(QtWidgets.QFrame.Plain)
    temp_space_frame.setLineWidth(0)
    temp_space_frame.setObjectName(f"ai_spacer_frame_{idx}")
    temp_horizontal_layout.addWidget(temp_space_frame)
    
    self.chat_interface_vertical_layout.addWidget(temp_frame)

    temp_label_ai_message.setText(markdown_content)

    temp_frame.show()
    temp_label_ai_icon.show()
    temp_label_ai_message.show()
    temp_space_frame.show()

    self.chat_components.append([temp_frame, temp_horizontal_layout, temp_label_ai_icon, temp_label_ai_message, temp_space_frame])

def create_user_chat_panel(self: Ui_MainWindow, idx, message_content):

    self.markdown_to_html_converter.setMarkdown(message_content)
    markdown_content = self.markdown_to_html_converter.toHtml()

    temp_frame = QtWidgets.QFrame(self.chat_interface_scroll_area_content)
    temp_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
    temp_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    temp_frame.setObjectName(f"user_frame_{idx}")
    
    temp_horizontal_layout = QtWidgets.QHBoxLayout(temp_frame)
    temp_horizontal_layout.setAlignment(QtCore.Qt.AlignTop)
    temp_horizontal_layout.setObjectName(f"horizontalLayout_{idx}")
    
    temp_label_user_message = QtWidgets.QLabel(temp_frame)
    font = QtGui.QFont()
    font.setPointSize(self.config["chat_font_size"])

    sizePolicy2 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
    sizePolicy2.setHorizontalStretch(0)
    sizePolicy2.setVerticalStretch(0)
    sizePolicy2.setHeightForWidth(temp_label_user_message.sizePolicy().hasHeightForWidth())
    temp_label_user_message.setSizePolicy(sizePolicy2)

    temp_label_user_message.setFont(font)
    temp_label_user_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
    temp_label_user_message.setWordWrap(True)
    temp_label_user_message.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
    temp_label_user_message.setObjectName(f"user_label_message_user_{idx}")
    temp_horizontal_layout.addWidget(temp_label_user_message)
    
    temp_label_user_icon = QtWidgets.QLabel(temp_frame)
    temp_label_user_icon.setMinimumSize(QtCore.QSize(40, 40))
    temp_label_user_icon.setMaximumSize(QtCore.QSize(40, 40))
    temp_label_user_icon.setText("")
    temp_label_user_icon.setPixmap(QtGui.QPixmap(".\\interface\\user.png"))
    temp_label_user_icon.setScaledContents(True)
    temp_label_user_icon.setObjectName(f"user_label_user_icon_{idx}")
    temp_horizontal_layout.addWidget(temp_label_user_icon)
    
    temp_space_frame = QtWidgets.QFrame(temp_frame)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(temp_space_frame.sizePolicy().hasHeightForWidth())
    temp_space_frame.setSizePolicy(sizePolicy)
    temp_space_frame.setMinimumSize(QtCore.QSize(100, 0))
    temp_space_frame.setMaximumSize(QtCore.QSize(100, 16777215))
    temp_space_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
    temp_space_frame.setFrameShadow(QtWidgets.QFrame.Plain)
    temp_space_frame.setLineWidth(0)
    temp_space_frame.setObjectName(f"user_spacer_frame_{idx}")
    # temp_horizontal_layout.addWidget(temp_space_frame)
    temp_horizontal_layout.insertWidget(0, temp_space_frame)

    self.chat_interface_vertical_layout.addWidget(temp_frame)

    temp_label_user_message.setText(markdown_content)

    temp_frame.show()
    temp_label_user_icon.show()
    temp_label_user_message.show()
    temp_space_frame.show()

    self.chat_components.append([temp_frame, temp_horizontal_layout, temp_label_user_icon, temp_label_user_message, temp_space_frame])

def delete_chat_board(self: Ui_MainWindow):

    if self.processing_message :
        return

    for idx in range(len(self.chat_components)):
        
        self.chat_interface_vertical_layout.removeWidget(self.chat_components[idx][0])
        self.chat_components[idx][4].deleteLater()
        self.chat_components[idx][3].deleteLater()
        self.chat_components[idx][2].deleteLater()
        self.chat_components[idx][1].deleteLater()
        self.chat_components[idx][0].deleteLater()
        self.chat_components[idx] = None

    self.chat_components = []

def load_chat_board(self: Ui_MainWindow):

    if self.processing_message :
        return

    self.delete_chat_board()

    if self.message_body == None:
        return
    
    for idx, message_content in enumerate(self.message_body):

        if idx % 2 == 0:
            create_user_chat_panel(self, idx, message_content)
            # create_ai_chat_panel(self, idx, message_content)
        else:
            create_ai_chat_panel(self, idx, message_content)






class MyMainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        self.shift_pressed = False
        super().__init__(*args, **kwargs)

    def set_text_box(self, textbox):

        self.textbox = textbox

    def set_call_function(self, func):
        self.handle_func = func

    def eventFilter(self, obj, event):

        if event.type() == QtCore.QEvent.KeyPress and obj is self.textbox:
            # print(event.key())
            if event.key() == QtCore.Qt.Key_Shift :
                self.shift_pressed = True
            elif event.key() == QtCore.Qt.Key_Return :
                if self.shift_pressed == False:
                    print("Enter is pressed")
                    self.handle_func()
                    return True

        elif event.type() == QtCore.QEvent.KeyRelease and obj is self.textbox:
            if event.key() == QtCore.Qt.Key_Shift :
                self.shift_pressed = False
        
        return super().eventFilter(obj, event)

if __name__ == "__main__":

    setattr(Ui_MainWindow, "connect_events", connect_events)
    setattr(Ui_MainWindow, "setup_states", setup_states)

    setattr(Ui_MainWindow, "button_attach_file_clicked", button_attach_file_clicked)
    setattr(Ui_MainWindow, "button_send_chat_clicked", button_send_chat_clicked)
    setattr(Ui_MainWindow, "button_new_chat_clicked", button_new_chat_clicked)
    setattr(Ui_MainWindow, "button_hide_message_headers_clicked", button_hide_message_headers_clicked)

    setattr(Ui_MainWindow, "load_message_board", load_message_board)
    setattr(Ui_MainWindow, "delete_message_board", delete_message_board)
    setattr(Ui_MainWindow, "message_board_item_clicked", message_board_item_clicked)
    setattr(Ui_MainWindow, "message_board_delete_clicked", message_board_delete_clicked)

    setattr(Ui_MainWindow, "create_ai_chat_panel", create_ai_chat_panel)
    setattr(Ui_MainWindow, "create_user_chat_panel", create_user_chat_panel)
    setattr(Ui_MainWindow, "delete_chat_board", delete_chat_board)
    setattr(Ui_MainWindow, "load_chat_board", load_chat_board)

    setattr(Ui_MainWindow, "set_main_window", set_main_window)
    
    setattr(Ui_MainWindow, "add_letter_to_chat", add_letter_to_chat)
    setattr(Ui_MainWindow, "done_adding_letters_to_chat", done_adding_letters_to_chat)

    setattr(Ui_MainWindow, "switch_to_small_clicked", switch_to_small_clicked)
    setattr(Ui_MainWindow, "switch_to_big_clicked", switch_to_big_clicked)

    setattr(Ui_MainWindow, "combo_box_models_currentTextChanged", combo_box_models_currentTextChanged)

    switch_to_small_clicked

    app = QtWidgets.QApplication(sys.argv)

    config = load_json_file("config.json")

    if "use_theme" in list(config.keys()):
        if config["use_theme"] != None :
            if os.path.exists(config["use_theme"]):

                f = open(config["use_theme"], "r")
                style = f.read()
                f.close()

                app.setStyleSheet(style)
            
            else:

                print(f"Could not load stylesheet - {config['use_theme']}")


    # MainWindow = QtWidgets.QMainWindow()
    MainWindow = MyMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.set_main_window(MainWindow)
    ui.connect_events()
    ui.setup_states()

    MainWindow.show()
    sys.exit(app.exec_())