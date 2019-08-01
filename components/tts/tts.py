import os
import sys
from gtts import gTTS
from pygame import mixer
import json

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

typedSpeechFile = config_data["record_file"]

def textSpeeach(str):
    
    from pygame import mixer

    tts = gTTS(text=str, lang='pt')
    tts.save(typedSpeechFile)
    mixer.init()
    mixer.music.load(typedSpeechFile)
    mixer.music.play()
    mixer.music.play()
