# Teste sistema bancário

import textwrap


def menu():
    menu = """\n
    ================== BANCO DIO ==================
    ESCOLHA UMA OPÇÃO PARA REALIZAR UMA OPERAÇÃO:
    
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    ===============================================
    => """
    return input(textwrap.dedent(menu))
    


def criar_usuario(usuarios):
    pass


def cadastrar_conta():
    pass


def depositar(saldo, valor, extrato, /):
    valor = 0
    saldo = saldo + valor
    extrato = saldo


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    pass


def exibir_extrato(saldo, /, *, extrato):
    pass


def sair():
    pass


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo: float = 0
    limite: float = 500
    extrato = ''
    numero_saques: int = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = input('Favor informar o valor do seu depósito: ')
            if valor.isdigit():
                saldo, extrato = depositar(saldo, valor, extrato)
                print(f'Depósito de R$ {valor:.2f} realizado com sucesso')
            else:
                print(f'Atenção, {valor} não é um valor válido. Por favor, tente novamente!')
    
        elif opcao == 's':
            valor_sacado = input('Favor informar o valor do seu saque: ')
            if valor_sacado.isdigit():
                valor_sacado = float(valor_sacado)
                if valor_sacado <= 500:
                    if LIMITE_SAQUES > 0:
                        if valor_sacado <= saldo:
                            saldo = saldo - valor_sacado
                            LIMITE_SAQUES -=1
                            extrato += f'Saque: R$ {valor_sacado:.2f}\n'
                            print(f'Saque de R$ {valor_sacado:.2f} realizado com sucesso!')
                        else:
                            print('Atenção, você não tem saldo suficiente para realizar esta operação')
                            print(f'Saldo atual: R$ {saldo:.2f}!')
                    else:
                        print('Atenção, seu limite de saques diários se esgotou!')
                        print('Por favor, tente novamente amanhã!')
                else:
                    print(f'Atenção, sua tentativa de saque é maior do que o limite de R$ 500.00 por saque.')
                    print('Por favor tente novamente')
            else:
                print(f'Atenção, {valor_sacado} não é um valor válido. Por favor, tente novamente!')
        
        elif opcao == 'e':
            print('================== BANCO DIO ==================')
            print('                                               ')
            print('=================== EXTRATO ===================')
            print('Não foram realizadas movimentações.' if not extrato else extrato)
            print(f'Saldo: R$ {saldo:.2f}')
            print('===============================================')
        
        elif opcao == 'q':
            break

        else:
            print(f'Atenção, {opcao} não é uma opção válida.')
            print('Tente uma opção válida ou "q" para sair.')

main()