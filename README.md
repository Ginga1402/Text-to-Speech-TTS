👨‍💻 Humanly Sculpted, 🤖 AI-Scripted: The Perfect Synergy

# **Text-to-Speech (TTS)**



## **Project Description**

Welcome to the **Text-to-Speech (TTS)** repository! This open-source project provides a variety of methods for implementing **Text-to-Speech** functionality in Python. The goal of this repo is to offer multiple approaches for converting text into speech, helping you choose the one that best suits your needs.


![Image](https://github.com/user-attachments/assets/85253878-d52f-4ef3-a6b7-c0c04afe2930)


The repository contains implementations using different libraries and models, including:
1. **Google Text-to-Speech (gTTS)** — A simple and easy-to-use method for converting text to speech via Google's Text-to-Speech API.
2. **Microsoft SpeechT5** — A powerful text-to-speech model using Microsoft's `speecht5_tts` from the Hugging Face Transformers library.
3. **Kokoro TTS** — An open-weight, high-quality TTS model that provides a realistic voice synthesis.

Whether you need a quick solution for a small project or a more advanced, customizable system, this repo has you covered!

---




## **Installation Instructions**

Follow these simple steps to get the Text-to-Speech functionality running on your local machine:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/Ginga1402/Text-to-Speech-TTS.git
    ```
2. Navigate into the project directory:
    ```bash
    cd Text-to-Speech-TTS
    ```
3. Set up a virtual environment (recommended for Python projects):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
    ```
4. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## **Usage**

After the installation, you can use any of the provided scripts to convert text to speech.

### 1. **Using Google Text-to-Speech (gTTS)**

To use Google’s TTS engine, run the `gtts_demo.py` script:
```bash
python gtts_demo.py
```

This will take a provided text input and convert it into speech using Google's TTS API.

### 2. **Using Microsoft SpeechT5**

To use the Microsoft SpeechT5 TTS model, run the microsoft_tts.ipynb Jupyter Notebook. You can use the Hugging Face transformers pipeline to generate speech from text:
```bash
jupyter notebook microsoft_tts.ipynby
```

### 3. **Using Kokoro TTS**

To use the Kokoro TTS model, open the KOKORO_TTS.ipynb Jupyter Notebook:
```bash
jupyter notebook KOKORO_TTS.ipynb
```

This will walk you through using Kokoro’s open-weight model to convert text to speech with high-quality output.

## **Use Cases**

### This project is useful for various scenarios:

1. Accessibility: Convert written content into speech for visually impaired users.

2. Voice Assistants: Build simple voice assistant features for applications.

3. Automation: Automate audio responses for chatbots or customer service systems.

4. Content Creation: Create audiobooks or podcasts from text content.


## **Technologies Used**
   
### This repository includes implementations of Text-to-Speech using the following technologies:

1. Python

2. gTTS (Google Text-to-Speech)

3. Microsoft SpeechT5 (via Hugging Face Transformers)

4. Kokoro TTS (Open-weight TTS model)


## **Contributing**
Contributions to this project are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.

## **License**
This project is licensed under the MIT License - see the LICENSE file for details.

