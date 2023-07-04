import random
import pygame
from time import sleep
from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Escolha um numero aleatorio entre 1 e 100 e boa sorte!!')],
    [sg.Text('Digite seu nome'), sg.Input(key='pessoa1', size=(20, 1))],
    [sg.Text('Digite o numero escolhido'), sg.Input(key='pergunta1', size=(5, 1))],
    [sg.Text('Ira ganhar em quantas chances?'), sg.Input(key='quantChance', size=(5, 1))],
    [sg.Button('Jogar'), sg.Text('Chances: ', key='Chance')],
    [sg.Text('Numero sorteado: X  ', key='numeroAleatorio', size=(40, 10))],
    [sg.Text('', key='editavel', size=(40, 3))]


]

#janela
janela = sg.Window('Cassino', layout)
#Ler os eventos

while True:
    eventos, valores = janela.read()
    pergunta1 =int(valores['pergunta1'])
    pessoa1 = valores['pessoa1']
    situação = 0
    numAle = 0
    contagem = int(valores['quantChance'])
    count = 0
    listaNum = []
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Jogar':
        while situação == 0:
            contagem -= 1
            count += 1
            janela.read(timeout=contagem)
            numAle = random.randint(1, 100)
            while numAle in listaNum:
                numAle = random.randint(1, 100)
            listaNum.append(numAle)
            sleep(0.2)
            janela['Chance'].update(f'chances {contagem}')
            janela['numeroAleatorio'].update(f'Numero sorteado {listaNum}  ')
            print(numAle)
            if contagem == 0:
                situação = 1
                janela['editavel'].update('Suas chances chegaram a 0 você mamou =/')
            if pergunta1 == numAle:
                pygame.init()
                pygame.mixer.init()
                janela['editavel'].update(f'Aeeeeeeeeeeeeeeeeew ganhou na sua {count}º tentativa Otario .I.')
                situação = 1
                pygame.mixer.music.load('kasino-mp3.mp3')
                pygame.mixer.music.play()









