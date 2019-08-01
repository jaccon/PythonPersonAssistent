import os
import json
import sys
from gtts import gTTS
from pygame import mixer
import json

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

sys.path.insert(0,'./components/wikipedia/')
import wiki as wikipedia

sys.path.insert(0,'./components/tts/')
import tts as tts

sys.path.insert(0,'./components/actions/')
import actions as actions

typedSpeechFile = config_data["record_file"]

os.system('tput clear')
print (config_data["intro"])
tts.textSpeeach(config_data["intro"])

while True:
    print ('')
    str = input(config_data["input_type"])
    tts.textSpeeach(str)
    actions.listen(str)
   