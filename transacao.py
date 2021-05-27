import PySimpleGUI as sg


def conta(self):
    layout = [
        [sg.Text('Qual operação deseja fazer:', size=(40, 1))],
        [sg.Checkbox('Extrato', key='extrato'), sg.Checkbox('Transferência', key='transferencia'), sg.Checkbox('Aumentar Limete', key='limite')],
        [sg.Button('Iniciar', size=(10, 0))]
    ]
    janela = sg.Window("Menu - Banco dos Reis").layout(layout)
    self.button, self.values = janela.Read()

def trans(self):
    layout = [
        [sg.Text('Conta Bancaria - Banco dos Reis')],
        [sg.Text('Codigo do Banco:', size=(15, 0)), sg.Input(size=(8, 0), key='codigo')],
        [sg.Text('Numero da Conta:',size=(15,0)), sg.Input(size=(8,0),key='numero')],
        [sg.Text('Titular:',(15,0)), sg.Input(size=(40,0),key='titular')],
        [sg.Text('Valor:', (15, 0)), sg.Input(size=(15, 0), key='valor')],
        [sg.Button('Transferir')]
      ]
    janela = sg.Window("Transferência - Banco dos Reis").layout(layout)
    self.button, self.values = janela.Read()

def limite(self):
    layout = [
        [sg.Text('Conta Bancaria - Banco dos Reis')],
        [sg.Text('Limite Solicitado:',size=(15,0)), sg.Input(size=(8,0),key='desejado')],
        [sg.Button('Solicitar')]
      ]
    janela = sg.Window("Limite - Banco dos Reis").layout(layout)
    self.button, self.values = janela.Read()