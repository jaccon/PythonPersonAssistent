# Python Text to Speech
# The simple and easy way to Python read what you type
# Created 14/07/2019
# developed by @jaccon

import os
import sys
from gtts import gTTS
from pygame import mixer
import time

typedSpeechFile = 'typed.mp3'

os.system('tput clear')
wellcome = "Olá, "
print (wellcome)
tts = gTTS(text=wellcome, lang='pt')
tts.save(typedSpeechFile)
mixer.init()
mixer.music.load(typedSpeechFile)
mixer.music.play()

while True:
    
    from pygame import mixer

    print ('')
    str = input('What to speak ?  ')
    tts = gTTS(text=str, lang='pt')
    tts.save(typedSpeechFile)
    
    mixer.init()
    mixer.music.load(typedSpeechFile)
    mixer.music.play()
    print ('')
    os.system('tput clear')

