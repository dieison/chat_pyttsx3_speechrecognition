import os
import pyttsx3 as p

import speech_recognition as sr

import requests

#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()

    #usando o microfone
    with sr.Microphone() as source:
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        #Frase para o usuario dizer algo
        #print("Diga alguma coisa: ")
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
    try:
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language='pt-BR')

        #Retorna a frase pronunciada
        #print("Você disse: " + frase)

    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")

    return frase

p.init('sapi5', True)

#speak() converts text to speech
p.speak("Seja bem vindo ao chatbot")

#loops until user specify to quit
while True: 
    p.speak("O que posso fazer por você?")
    userinput = ouvir_microfone()

    print("Comando: ", userinput)

    if ("abrir" in userinput.lower() and ("bloco de notas" in userinput.lower())) :
        p.speak("Abrindo bloco de notas")
        os.system("notepad")
    elif ("buscar" in userinput.lower()) :
        p.speak("Ok. Informe o que deseja buscar")
        termo = ouvir_microfone()
        req = requests.get("https://www.google.com/search?q=" + termo)
        print(req.text)
        break
    elif ("sair" in userinput.lower()) or ("encerrar" in userinput.lower()) :
        p.speak("Obrigado por conversarmos")
        break
    else :
        p.speak("Não temos suporte para isso. Tente novamente com outro comando.")