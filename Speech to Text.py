"""
#There are many APIs available for speech to text:

#Google Speech Recognition

#Google Cloud Speech API

#Wit.ai

#Microsoft Bing Voice Recognition

#Houndify API

#IBM Speech to Text

#Spext

#Dragon

#I have taken some sample of audio data set of different types and tests with all above mentioned APIs.

#By this experiment I have came to conclusion:

#Spext, SoundHound Inc. and are doing great job.

#I am mentioning below code of some APIs::
"""

#########################################

## download video from you tube

import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     ydl.download(['https://www.youtube.com/watch?v=Fq2CvmgoO7I&t=12s'])

import speech_recognition as sr
sr.__version__

# obtain path to "english.wav" in the same folder as this script

import os as os
os.getcwd()
os.chdir('C:\\Users\\rishabh.gupta\\Desktop\\Google Coloud')
os.listdir()


# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile('Nike_Wav.wav') as source:
    audio = r.record(source)  # read the entire audio file
    
type(audio)

# recognize speech using Google Speech Recognition

# for testing purposes, we're just using the default API key
# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
# instead of `r.recognize_google(audio)`

print("Google Speech Recognition thinks you said " + r.recognize_google(audio))


# recognize speech using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""

print("Google Cloud Speech thinks you said " + 
      r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))


# recognize speech using Wit.ai
# for Demo here i have mentioned my key 

WIT_AI_KEY = "NJLLZIVVPATBPXQI55FTCQTS5ZKOXA7A"  # Wit.ai keys are 32-character uppercase alphanumeric strings

print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))

    
# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings

print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))


# recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "34ywDSThwb9zr_SkfpDHKQ=="  # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = "hdDcg37uGKKkU5T6x5G9HuNbLxnD9GUsW4GNw_5EXHZlBU9y0tTmTYDwQLF69LBoAg4YgB4D0jROoeV1L4clrA=="  # Houndify client keys are Base64-encoded strings


print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))

#for Demo here i have mentioned my username and passowrd  

# recognize speech using IBM Speech to Text
IBM_USERNAME = "rishabh.gupta@iimu.ac.in"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = "IIMU"  # IBM Speech to Text passwords are mixed-case alphanumeric strings

print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))

