- 一段用于听写单词的小代码
- 使用方式：在list.txt中输入自己需要的单词，而后运行程序即可
- 第三方库
  - import requests
  - playsound
  - pyttsx3
- 当程序最开始运行时，会询问是否更新语音库
  - 如果选择是，会向https://api.dictionaryapi.dev提交get请求，如果有人声语音，自动下载并保存在audio_lib文件夹里
- 然后开始听写， audio_lib没有文件的话就会通过pyttsx3自动生成一段语音。





- A small piece of code for dictating words
- How to use: Input the words you need in list.txt, and then run the program
- third-party library
  - import requests
  - playsound
  - pyttsx3
- When the program first runs, it asks whether to update the language library
- if you choose, will submit a get request to https://api.dictionaryapi.dev, if the voice of speech, automatically download and save in audio_lib folder
- Then start dictation, audio_lib will automatically generate a voice through pyttsx3 if there is no file.