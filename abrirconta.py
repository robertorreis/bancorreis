import PySimpleGUI as sg

def conta(self):
    layout = [
        [sg.Text('Conta Bancaria - Banco dos Reis')],
        [sg.Text('Numero da Conta:',size=(15,0)), sg.Input(size=(8,0),key='numero')],
        [sg.Text('Titular:',(15,0)), sg.Input(size=(40,0),key='titular')],
        [sg.Text('Deposito:',(15,0)), sg.Input(size=(20,0),key='saldo')],
        [sg.Text('Limite:',(15,0)), sg.Input(size=(20,0),key='limite')],
        [sg.Button('Cadastrar')]
      ]
    janela = sg.Window("Abertura de Conta - Banco dos Reis").layout(layout)
    self.button, self.values = janela.Read()



