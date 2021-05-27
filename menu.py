import PySimpleGUI as sg
import abrirconta
import acessarconta
import transacao

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
            titular = self.values['titular']
            senha = sg.popup_get_text('Senha:', password_char='*')
            print(f'Numero da Conta:{numero}')
            print(f'Titular:{titular}')
            print(f'Senha:{senha}')
            transacao.conta(self)
            extrato = self.values['extrato']
            trans = self.values['transferencia']
            if(extrato == True):
                sg.popup('Valor em conta de R$ 2.000,00')
                print("Valor de R$ 2.000,00")
            elif(trans == True):
                transacao.trans(self)
                codigo = self.values['codigo']
                conta = self.values['numero']
                titular = self.values['titular']
                valor = self.values['valor']
                print(f'Codigo do Banco:{codigo}')
                print(f'Conta Corrente:{conta}')
                print(f'Titular:{titular}')
                print(f'Valor:{valor}')
                sg.popup('Tranferência Concluida')
            else:
                transacao.limite(self)
                limite = self.values['desejado']
                print(f'Limite Solicitado:{limite}')


tela = Menu()
tela.Iniciar()
