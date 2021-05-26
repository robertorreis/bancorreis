import PySimpleGUI as sg


def conta(self):
    layout = [
        [sg.Text('Conta Bancaria - Banco dos Reis')],
        [sg.Text('Numero da Conta:',size=(15,0)), sg.Input(size=(8,0),key='numero')],
        [sg.Text('Titular:',(15,0)), sg.Input(size=(40,0),key='titular')],
        [sg.Button('Acessar')]
      ]
    janela = sg.Window("Acessar Conta").layout(layout)
    self.button, self.values = janela.Read()

