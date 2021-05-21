import PySimpleGUI as sg
import abrirconta
import acessarconta
class Menu:
    def __init__(self):

        layout = [
            [sg.Text('O que deseja fazer:', size=(40,1))],
            [sg.Checkbox('Abrir Conta',key='abrir'), sg.Checkbox('Acessar Conta',key='acessar')],
            [sg.Button('Iniciar', size=(10,0))]
        ]

        janela = sg.Window("Banco dos Reis").layout(layout)

        self.button, self.values = janela.read()
        janela.close()

    def Iniciar(self):

        abrir = self.values['abrir']

        if (abrir == True):
            abrirconta.conta(self)
            numero = self.values['numero']
            titular = self.values['titular']
            saldo = self.values['saldo']
            limite = self.values['limite']
            print(f'Numero da Conta:{numero}')
            print(f'Titular:{titular}')
            print(f'Deposito:{saldo}')
            print(f'Limite:{limite}')
        else:
            acessarconta.conta(self)
            numero = self.values['numero']
            senha = self.values['senha']
            print(f'Numero da Conta:{numero}')
            print(f'Senha:{senha}')


tela = Menu()
tela.Iniciar()