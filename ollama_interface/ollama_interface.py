from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QCoreApplication, QPoint
from interface.interface import Ui_MainWindow
import ollama, json
import os
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


def load_json_file(filename) -> dict:
    with open(filename, 'r') as f:
        return json.load(f)

def save_json_file(filename, data: dict):

    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=4))
        f.close()

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

    self.button_process_text.clicked.connect(self.Process_Text_Pressed)
    self.button_copy_text.clicked.connect(self.Copy_Text_Pressed)
    self.button_process_text_prompt.clicked.connect(self.Process_Text_Prompt_Pressed)
    self.button_clear_chat.clicked.connect(self.Clear_Chat)
    

    self.actionInference.triggered.connect(self.inference_menu_bar_clicked)
    self.actionSettings.triggered.connect(self.settings_menu_bar_clicked)
    self.actionPrompt.triggered.connect(self.prompt_menu_bar_clicked)

    self.actionSwitch_To_Small.triggered.connect(switch_to_small_clicked)
    self.actionSwitch_To_Chat.triggered.connect(switch_to_chat_clicked)

    self.list_instructions_settings.clicked.connect(self.list_item_selected)

    self.button_save_selected.clicked.connect(self.button_save_selected_press)
    self.button_remove_selected.clicked.connect(self.button_remove_selected_press)
    self.button_add_new_instruction.clicked.connect(self.button_add_instruction_press)


def switch_to_small_clicked(self: Ui_MainWindow):

    subprocess.Popen(["cd", "../ollama_interface_small", "&","pythonw", "ollama_interface.py"], shell=True)
    QCoreApplication.quit()

def switch_to_chat_clicked(self: Ui_MainWindow):

    subprocess.Popen(["cd", "../ollama_interface_chat", "&","pythonw", "chat_interface.py"], shell=True)
    QCoreApplication.quit()

def Process_Text_Pressed(self: Ui_MainWindow):


    model_selected = self.list_models.currentItem().text()
    instruction_selected = self.list_instructions.currentItem().text()
    
    input_text = str(self.plaintext_input.toPlainText())

    if input_text == "" or input_text == None:
        return

    prompt_text = str(self.available_instructions[instruction_selected]).replace("#$PROMPT$#", input_text)

    # new_text = infer_text(prompt_text, model_selected)
    self.button_process_text.setEnabled(False)

    # self.plaintext_output.setPlainText("")
    self.plaintext_output.setMarkdown("")
    self.plaintext_buffer = ""


    self.thread = QThread()
    self.worker = OllamaStreamThread(prompt_text, model_selected)

    self.worker.moveToThread(self.thread)

    self.thread.started.connect(self.worker.run)

    self.worker.kill_thread.connect(self.thread.quit)
    self.worker.kill_thread.connect(self.worker.deleteLater)
    self.thread.finished.connect(self.thread.deleteLater)

    self.worker.chunk_writer.connect(self.Update_Inference_Board)
    self.worker.finished.connect(self.Enable_Inference_Board)

    self.thread.start()

def Process_Text_Prompt_Pressed(self: Ui_MainWindow):

    model_selected = self.combo_model_list.currentText()
    
    input_text = str(self.plaintext_input_prompt.toPlainText())

    if input_text == "" or input_text == None:
        return

    system_prompt = str(self.plaintext_system_prompt.toPlainText())

    self.plaintext_input_prompt.setPlainText("")

    # new_text = infer_text(prompt_text, model_selected)
    self.button_process_text_prompt.setEnabled(False)
    self.button_clear_chat.setEnabled(False)

    # self.plaintext_output_prompt.setPlainText("")
    self.plaintext_output_prompt.setMarkdown("")

    jsonify_output = self.checkbox_jsonify.isChecked()

    if self.current_chat != "":
        self.cross_chat.append(self.current_chat)
    
    self.current_chat = ""
    self.cross_chat.append(input_text)

    self.Update_Prompt_Board()

    self.thread = QThread()
    self.worker = OllamaStreamThread(self.cross_chat, model_selected, jsonify_output, system_prompt)

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

    self.plaintext_system_prompt.setPlainText("")

    self.Update_Prompt_Board()

def Add_Letter_To_Running_Chat(self, added_letter):

    self.current_chat = self.current_chat + added_letter
    self.Update_Prompt_Board()


def Copy_Text_Pressed(self: Ui_MainWindow):
    
    output_text = str(self.plaintext_output.toMarkdown())

    self.plaintext_input.setPlainText(output_text)

def Update_Inference_Board(self: Ui_MainWindow, added_letter):
    # current = self.plaintext_output.toPlainText()
    # current = self.plaintext_output.toMarkdown()


    current = self.plaintext_buffer

    new_current = current + added_letter
    self.plaintext_output.setMarkdown(new_current)

    self.plaintext_buffer = new_current

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

    self.plaintext_output_prompt.setMarkdown(output_message)
    self.plaintext_output_prompt.verticalScrollBar().setValue(self.plaintext_output_prompt.verticalScrollBar().maximum())



def Enable_Inference_Board(self):

    self.button_process_text.setEnabled(True)

def Enable_Prompt_Board(self):

    self.button_process_text_prompt.setEnabled(True)
    self.button_clear_chat.setEnabled(True)

def Load_Configuration(self):

    self.configuration = load_json_file("ollama_interface_config.json")
    self.available_instructions = self.configuration["instructions"]

    self.list_instructions.clear()
    for instruction in list(self.available_instructions.keys()):
        self.list_instructions.addItem(instruction)

    self.list_models.clear()
    self.combo_model_list.clear()

    self.all_models = [model_entry["name"] for model_entry in ollama.list()["models"]]
    self.all_models.sort()

    for model_name in self.all_models:
        self.combo_model_list.addItem(model_name)
        self.list_models.addItem(model_name)

    # for model_name in self.configuration["model_list"]:
    #     self.combo_model_list.addItem(model_name)

    self.list_models.setCurrentRow(0)
    self.list_instructions.setCurrentRow(0)

    model = self.list_models.currentItem().text()
    print(model)

    self.update_instruction_list_settings()


def Switch_To_Prompt_Page(self: Ui_MainWindow):

    self.stackedWidget.setCurrentWidget(self.promp_page)
    self.Clear_Chat()

def Switch_To_Settings_Page(self: Ui_MainWindow):

    self.stackedWidget.setCurrentWidget(self.settings_page)


def Switch_To_Inference_Page(self: Ui_MainWindow):

    self.stackedWidget.setCurrentWidget(self.inference_page)


def prompt_menu_bar_clicked(self):
    self.Switch_To_Prompt_Page()

def inference_menu_bar_clicked(self):
    self.Switch_To_Inference_Page()

def settings_menu_bar_clicked(self):
    self.Switch_To_Settings_Page()

def list_item_selected(self: Ui_MainWindow):

    config = load_json_file("ollama_interface_config.json")

    instruction_selected = self.list_instructions_settings.currentItem().text()
    
    self.line_edit_selected_title.setText(instruction_selected)
    self.plaintext_selected_prompt.setPlainText(config["instructions"][instruction_selected])



def update_instruction_list_settings(self: Ui_MainWindow):

    self.list_instructions_settings.clear()

    config = load_json_file("ollama_interface_config.json")

    all_instructions = list(config["instructions"].keys())

    for instruction in all_instructions:
        self.list_instructions_settings.addItem(instruction)

    self.list_instructions_settings.setCurrentIndex(self.list_instructions_settings.indexAt(QPoint(0, 0)))
    self.list_item_selected()

def button_save_selected_press(self: Ui_MainWindow):

    instruction_selected = self.list_instructions_settings.currentItem().text()

    config = load_json_file("ollama_interface_config.json")

    config["instructions"].pop(instruction_selected, None)
    config["instructions"][self.line_edit_selected_title.text()] = self.plaintext_selected_prompt.toPlainText()

    save_json_file("ollama_interface_config.json", config)

    self.update_instruction_list_settings()

def button_remove_selected_press(self: Ui_MainWindow):

    instruction_selected = self.list_instructions_settings.currentItem().text()

    config = load_json_file("ollama_interface_config.json")

    config["instructions"].pop(instruction_selected, None)

    save_json_file("ollama_interface_config.json", config)

    self.update_instruction_list_settings()


def button_add_instruction_press(self: Ui_MainWindow):

    config = load_json_file("ollama_interface_config.json")

    new_instruction = self.line_edit_new_title.text()

    if new_instruction in list(config["instructions"].keys()):
        
        msg = QtWidgets.QErrorMessage()
        msg.showMessage('Instruction already in instruction list!')
        msg.exec_()
        
        return
    
    config["instructions"][new_instruction] = self.plaintext_new_prompt.toPlainText()

    save_json_file("ollama_interface_config.json", config)

    self.update_instruction_list_settings()

if __name__ == "__main__":

    # print(infer_text("Hello my friendly llm", "qwen2:latest"))
    # exit()

    setattr(Ui_MainWindow, "Process_Text_Pressed", Process_Text_Pressed)
    setattr(Ui_MainWindow, "Process_Text_Prompt_Pressed", Process_Text_Prompt_Pressed)
    setattr(Ui_MainWindow, "Copy_Text_Pressed", Copy_Text_Pressed)
    setattr(Ui_MainWindow, "Load_Configuration", Load_Configuration)
    setattr(Ui_MainWindow, "Update_Inference_Board", Update_Inference_Board)
    setattr(Ui_MainWindow, "Update_Prompt_Board", Update_Prompt_Board)
    setattr(Ui_MainWindow, "Enable_Inference_Board", Enable_Inference_Board)
    setattr(Ui_MainWindow, "Enable_Prompt_Board", Enable_Prompt_Board)
    setattr(Ui_MainWindow, "Switch_To_Prompt_Page", Switch_To_Prompt_Page)
    setattr(Ui_MainWindow, "Switch_To_Settings_Page", Switch_To_Settings_Page)
    setattr(Ui_MainWindow, "Switch_To_Inference_Page", Switch_To_Inference_Page)
    setattr(Ui_MainWindow, "prompt_menu_bar_clicked", prompt_menu_bar_clicked)
    setattr(Ui_MainWindow, "inference_menu_bar_clicked", inference_menu_bar_clicked)
    setattr(Ui_MainWindow, "settings_menu_bar_clicked", settings_menu_bar_clicked)
    setattr(Ui_MainWindow, "switch_to_small_clicked", switch_to_small_clicked)

    setattr(Ui_MainWindow, "list_item_selected", list_item_selected)
    setattr(Ui_MainWindow, "update_instruction_list_settings", update_instruction_list_settings)

    setattr(Ui_MainWindow, "Clear_Chat", Clear_Chat)
    setattr(Ui_MainWindow, "Add_Letter_To_Running_Chat", Add_Letter_To_Running_Chat)
    setattr(Ui_MainWindow, "button_save_selected_press", button_save_selected_press)
    setattr(Ui_MainWindow, "button_remove_selected_press", button_remove_selected_press)
    setattr(Ui_MainWindow, "button_add_instruction_press", button_add_instruction_press)
    
    setattr(Ui_MainWindow, "Connect_Events", Connect_Events)

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


    ui.Load_Configuration()
    ui.Connect_Events()
    ui.Switch_To_Prompt_Page()

    MainWindow.show()
    sys.exit(app.exec_())



