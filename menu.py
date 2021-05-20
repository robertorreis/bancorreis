import PySimpleGUI as sg
import abrirconta

class Menu:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('O que deseja fazer:', size=(40,1))],
            [sg.Checkbox('Abrir Conta',key='abrir'), sg.Checkbox('Acessar Conta',key='acessar')],
            [sg.Button('Iniciar', size=(10,0))]
        ]
        #janela
        janela = sg.Window("Banco dos Reis").layout(layout)
        #Extrais os dados da tela
        self.button, self.values = janela.read()

    def Iniciar(self):
        print(self.values)
        abrir = self.values['abrir']
        acessar = self.values['acessar']
        if (abrir == True):
            abrirconta.conta(self)
        else:
            pass

tela = Menu()
tela.Iniciar()