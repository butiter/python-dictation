import random
import requests
import os
import playsound,pyttsx3


def pyttsx3play(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()

def play_word(word):
    # check if the audio file exists
    audio_file = f"./audio_lib/{word}.mp3"
    if os.path.exists(audio_file):
        playsound.playsound(audio_file)
        return
    # if not, use text-to-speech
    pyttsx3play(word)

def download_word_audio(word):
    # download the pronunciation of the word
    audio_file = f"./audio_lib/{word}.mp3"
    if os.path.exists(audio_file):
        return
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        data = response.json()
        audio_url = data[0]['phonetics'][0]['audio']
        if audio_url == "":
            if len(data[0]['phonetics']) >= 2:
                audio_url = data[0]['phonetics'][1]['audio']
            if audio_url == "":
                print(word,"has no audio")
                return
        audio_file = f"./audio_lib/{word}.mp3"
        response = requests.get(audio_url)
        with open(audio_file, "wb") as f:
            f.write(response.content)
        print(word,"has been download")
    except:
        print(word,"has no audio")

def get_word_info(word):
    # get the definition and translation of the word
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
        try:
            translation = data[0]['meanings'][0]['definitions'][0]['translation']['text']
        except KeyError:
            translation = ''
        return definition, translation
    else:
        return None, None

def listen_and_write():
    # read words from the list.txt
    with open('list.txt', 'r') as f:
        words = [line.strip() for line in f.readlines()]
    random.shuffle(words)
    # ask the user if they want to update the audio library
    update_audio_library = input("Do you want to update the audio library? (yes/no) ").lower() == "yes"
    if update_audio_library:
        if not os.path.exists("./audio_lib"):
            os.makedirs("./audio_lib")
        for word in words:
            download_word_audio(word)
    # play and test each word
    for word in words:
        play_word(word)
        user_input = input(f'')
        if user_input == "again":
            play_word(word)
            user_input = input(f'')
        if user_input == word:
            #definition, translation = get_word_info(word)
            print("Correct")
        else:
            print(f'Incorrect! The word is {word}.')

if __name__ == '__main__':
    listen_and_write()
