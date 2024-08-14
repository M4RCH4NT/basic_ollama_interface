# Basic Ollama Interface
**Author: Marchant Fourie**
## Overview

This repo provides python scripts for GUIs that can be used to prompt Ollama models. There are two versions, a normal version and a small version. 

- **ollama_interface**: Normal GUI with an interface to the Ollama model and an additional interface for processsing text with default commands
- **ollama_interface_small**: Stripped version of the GUI with only an interface to prompt the ollama models

## File Structure

- `README.md`
- **ollama_interface/**
    - `ollama_interface_config.json`
    - `ollama_interface.py` 
    - **interface**/
        - `interface.ui`
        - `interface.py`
        - `dark_style.qss`
- **ollama_interface_small/**
    - `ollama_interface_config.json`
    - `ollama_interface.py` 
    - **interface**/
        - `interface.ui`
        - `interface.py`
        - `dark_style.qss`


## Getting Started

### Installation

Python needs to be installed on your system as well as a package manager such as pip. The required packages can be found in `requirements.txt`. To install the packages using pip use the following command:

```Powershell
pip install -r requirements.
```

#### PyQT5

The QUI was created using the pyqt5 python library. The required libraries are installed when using pip, but other packages might be required for it to work on **linux**. If you get an error like this:

```bash
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, minimal, minimalegl, offscreen, vnc, xcb.

Aborted (core dumped)
```

Then you probably need to install the following packages:

```bash
sudo apt install libxcb-xinerama0 libxkbcommon-x11-0 libglu1-mesa
```

You might also need to export an environment variable:
```bash
export QT_DEBUG_PLUGINS=1
```

#### Ollama

You also need to install ollama to use the LLM functionalities. The installation instructions can be found at https://ollama.com/.

You then also need to install the model you want to use. You can get a list of the available models at https://ollama.com/library.

You can then install the model by running the following command in the terminal:

```powershell
ollama pull <model_name>:<tag>
```
The tag usually defines either the size of the model or to just use the latest one. Remember to add your model name to the `ollama_interface_config.json` file.

### Usage

The program can be run by executing the scripts in the environment where the packages are installed. The scrips can be executed from the terminal using:

```Powershell
python <script.py>
```

## Interface

The normal interface has three windows which can be controlled in the menubar at the top left corner of the screen. The windows are as follows:

### Chat

The chat window allows you to send messages to the LLM and receive responses. Your prompt is typed in the top text box and the responses are displayed in the bottom text box after the generate button is clicked. You can specify a system message. If the system message is kept blank then the default system message is used. The JSONIFY option can be selected if you want the response to be displayed in JSON. The model to use can be selected from the dropdown menu. The model names displayed is specified in the `ollama_interface_config.json` file. The clear chat button clears the conversation so that a new one can be started.

### Text Inference

This window allows you to run pre-defined instruction on the input text and will be displayed in the output text box. The instruction list is defined in the `ollama_interface_config.json` file and are shown in the list. The model to use can be selected from the model list. The copy text to input button allows you to copy the output text to the input box for further processing.

### Settings

*This has not yet been implemented. The aim is to enable the user to modify the configuration from the GUI instead of having to edit the config files directly.*

## Small version

The small version only has the chat window with no additional options for jsonify and providing the system message. The idea is that it is a small window which you can open and place somewhere to ask simple questions while working on your work.

## Configuration

All configurations are set within the `ollama_interface_config.json` file

This stores the following settings:

- model_list - A list of the models you install in ollama and want to use in the interface
- use_theme - A path to the qss file which can be used to style the pyqt5 interface. Set to null if you don't want to use a theme
- instructions (*not used in small version*) - This is used to specify specific instructions which can be used by the interface
    - The format is as follows:
        - `"instruction title" : "instruction prompt and include #$PROMPT$# where the text in the prompt should be placed"`

## Future Work

- To add the settings window in the normal interface for editing the configuration.
- To add additional windows to both interfaces to change basic ollama parameters such as system message, temperature, context length, etc.
- Add support for analysing pdf documents. Will be a massive task and will probably be done in another project.