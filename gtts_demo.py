from gtts import gTTS
import os
import time

def text_to_speech(text,lang):
    language = lang
    audioobj = gTTS(text=text, lang=language, slow=False)
    
    # Generate a unique file name based on timestamp
    timestamp = int(time.time())
    file_path = f"output_{timestamp}.mp3"
    
    # Check if the file exists and remove it
    if os.path.exists(file_path):
        os.remove(file_path)

    audioobj.save(file_path)

    return file_path



########

test = """ This repository is designed to explore various methods for transcribing text to speech and converting speech to text.
These techniques are crucial for the development of any generative AI application. Enhancing capabilities in both transcription and translation."""

transcibed = text_to_speech(text=test,lang='en')


