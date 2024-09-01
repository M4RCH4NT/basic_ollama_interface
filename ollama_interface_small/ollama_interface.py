from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from interface.interface import Ui_MainWindow
import ollama, json, os
import subprocess

def infer_text(text, model):

    response = ollama.chat(model=model, messages= [
        {
            "role": "user", 
            "content": text
        }
    ])

    return response["message"]["content"]

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


def load_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)


class OllamaStreamThread(QObject):

    chunk_writer = pyqtSignal(str)
    finished = pyqtSignal()
    kill_thread = pyqtSignal()

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



def Connect_Events(self: Ui_MainWindow):

    self.button_process_text_prompt.clicked.connect(self.Process_Text_Prompt_Pressed)
    self.button_clear_chat.clicked.connect(self.Clear_Chat)
    
    self.actionSwitch_To_Big.triggered.connect(self.switch_to_big_clicked)
    self.actionSwitch_To_Chat.triggered.connect(self.switch_to_chat_clicked)

def switch_to_big_clicked(self: Ui_MainWindow):

    subprocess.Popen(["cd", "../ollama_interface", "&","pythonw", "ollama_interface.py"], shell=True)
    QtCore.QCoreApplication.quit()


def switch_to_chat_clicked(self: Ui_MainWindow):

    subprocess.Popen(["cd", "../ollama_interface_chat", "&","pythonw", "chat_interface.py"], shell=True)
    QtCore.QCoreApplication.quit()

def Process_Text_Prompt_Pressed(self: Ui_MainWindow):

    model_selected = self.combo_model_list.currentText()
    
    input_text = str(self.plaintext_input_prompt.toPlainText())

    if input_text == "" or input_text == None:
        return

    self.plaintext_input_prompt.setPlainText("")

    # new_text = infer_text(prompt_text, model_selected)
    self.button_process_text_prompt.setEnabled(False)
    self.button_clear_chat.setEnabled(False)

    # self.plaintext_output_prompt.setPlainText("")
    self.plaintext_output_prompt.setMarkdown("")


    if self.current_chat != "":
        self.cross_chat.append(self.current_chat)
    
    self.current_chat = ""
    self.cross_chat.append(input_text)

    self.Update_Prompt_Board()

    self.thread = QThread()
    self.worker = OllamaStreamThread(self.cross_chat, model_selected)

    self.worker.moveToThread(self.thread)

    self.thread.started.connect(self.worker.run)

    self.worker.kill_thread.connect(self.thread.quit)
    self.worker.kill_thread.connect(self.worker.deleteLater)
    self.thread.finished.connect(self.thread.deleteLater)

    self.worker.chunk_writer.connect(self.Add_Letter_To_Running_Chat)
    self.worker.finished.connect(self.Enable_Prompt_Board)

    self.thread.start()

def Clear_Chat(self):
    self.cross_chat = []
    self.current_chat = ""

    self.Update_Prompt_Board()

def Add_Letter_To_Running_Chat(self, added_letter):

    self.current_chat = self.current_chat + added_letter
    self.Update_Prompt_Board()

def Update_Prompt_Board(self: Ui_MainWindow):

    output_message = ""

    for idx, message in enumerate(self.cross_chat) :

        if idx % 2 == 0:
            output_message = output_message + "\n**User**:\n"
        else:
            output_message = output_message + "\n**Assistant**:\n"
        
        output_message = output_message + message +"\n"

    if self.current_chat != "" :
        output_message = output_message + "\n**Assistant**:\n"
        output_message = output_message + self.current_chat +"\n"

    # self.plaintext_output_prompt.setPlainText(output_message)
    self.plaintext_output_prompt.setMarkdown(output_message)
    self.plaintext_output_prompt.verticalScrollBar().setValue(self.plaintext_output_prompt.verticalScrollBar().maximum())

def Enable_Prompt_Board(self):

    self.button_process_text_prompt.setEnabled(True)
    self.button_clear_chat.setEnabled(True)

def Load_Configuration(self: Ui_MainWindow):

    self.configuration = load_json_file("ollama_interface_config.json")

    self.combo_model_list.clear()

    self.all_models = [model_entry["name"] for model_entry in ollama.list()["models"]]
    self.all_models.sort()

    for model_name in self.all_models:
        self.combo_model_list.addItem(model_name)

    # for model_name in self.configuration["model_list"]:
    #     self.combo_model_list.addItem(model_name)

def Resize_Components(self):

    window_width = self.mw.width()
    window_height = self.mw.height()

    top = self.button_process_text_prompt.geometry().top()
    left = self.button_process_text_prompt.geometry().left()
    height = self.button_process_text_prompt.geometry().height()
    self.button_process_text_prompt.setGeometry(QtCore.QRect(left, top, window_width - left - 10, height))

    top = self.button_clear_chat.geometry().top()
    left = self.button_clear_chat.geometry().left()
    height = self.button_clear_chat.geometry().height()
    self.button_clear_chat.setGeometry(QtCore.QRect(left, top, window_width - left - 10, height))

    top = self.combo_model_list.geometry().top()
    left = self.combo_model_list.geometry().left()
    height = self.combo_model_list.geometry().height()
    self.combo_model_list.setGeometry(QtCore.QRect(left, top, window_width - left - 10, height))

    top = self.plaintext_input_prompt.geometry().top()
    left = self.plaintext_input_prompt.geometry().left()
    height = self.plaintext_input_prompt.geometry().height()
    self.plaintext_input_prompt.setGeometry(QtCore.QRect(left, top, window_width - left - 10, height))

    top = self.plaintext_output_prompt.geometry().top()
    left = self.plaintext_output_prompt.geometry().left()
    height = self.plaintext_output_prompt.geometry().height()
    self.plaintext_output_prompt.setGeometry(QtCore.QRect(left, top, window_width - left - 10, window_height - top - 45))


def connect_mainwindow(self, mw):
    self.mw = mw

if __name__ == "__main__":

    # print(infer_text("Hello my friendly llm", "qwen2:latest"))
    # exit()

    setattr(Ui_MainWindow, "Process_Text_Prompt_Pressed", Process_Text_Prompt_Pressed)
    setattr(Ui_MainWindow, "Load_Configuration", Load_Configuration)
    setattr(Ui_MainWindow, "Update_Prompt_Board", Update_Prompt_Board)
    setattr(Ui_MainWindow, "Enable_Prompt_Board", Enable_Prompt_Board)
    setattr(Ui_MainWindow, "Resize_Components", Resize_Components)

    setattr(Ui_MainWindow, "connect_mainwindow", connect_mainwindow)

    setattr(Ui_MainWindow, "Clear_Chat", Clear_Chat)
    setattr(Ui_MainWindow, "Add_Letter_To_Running_Chat", Add_Letter_To_Running_Chat)
    
    setattr(Ui_MainWindow, "Connect_Events", Connect_Events)
    setattr(Ui_MainWindow, "switch_to_big_clicked", switch_to_big_clicked)
    setattr(Ui_MainWindow, "switch_to_chat_clicked", switch_to_chat_clicked)

    import sys
    app = QtWidgets.QApplication(sys.argv)

    config = load_json_file("ollama_interface_config.json")

    if "use_theme" in list(config.keys()):
        if config["use_theme"] != None :
            if os.path.exists(config["use_theme"]):

                f = open(config["use_theme"], "r")
                style = f.read()
                f.close()

                app.setStyleSheet(style)
            
            else:

                print(f"Could not load stylesheet - {config['use_theme']}")

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    ui.connect_mainwindow(MainWindow)
    ui.Load_Configuration()
    ui.Connect_Events()
    ui.Clear_Chat()

    ui.Resize_Components()

    MainWindow.resizeEvent = lambda x: ui.Resize_Components()

    MainWindow.show()
    sys.exit(app.exec_())



