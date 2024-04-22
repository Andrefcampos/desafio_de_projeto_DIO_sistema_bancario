
menu = '''
===============$$Banco$$===============
[1] Depositar
[2] Saque
[3] Extrato
[4] Sair
===============$$$$$$$$$===============
'''
deposito = n_deposito = n_saque = saque = saldo = 0
limite_saque = 3
extrato_saque = []
extrato_deposito = []

nome_operacoes = ['Depósito', 'Saque', 'Extrato', 'Sair', 'Extrato de depósito', 'Extrato de saque', 'Saldo']

while True:
    operacao = int(input(menu + '-> '))
    if operacao == 1:
        print(f'>>> Você selecionou a opção {nome_operacoes[0]}:')
        print()
        deposito = float(input('> Digite o valor a ser depositado -> R$ '))
        if deposito > 0:
            print(f'>> Você realizou um depósito de R$ {deposito:.2f}.')
            print()
            saldo += deposito
            extrato_deposito.append(deposito)
        else:
            print(f'>> Não foi possível realizar o depósito de R$ {deposito:.2f}. Realize um depósito elegível.')
    elif operacao == 2:
        print(f'>>> Você selecionou a opção {nome_operacoes[1]}:')
        print()
        saque = float(input('> Digite o valor do saque -> R$ '))
        if saque <= saldo:
            if limite_saque > 0:
                if saque <= 500.0:
                    print(f'>> Você realizou o saque no valor de R$ {saque:.2f}.')
                    print()
                    saldo -= saque
                    limite_saque -= 1
                    extrato_saque.append(saque)
                else:
                    print(f'--> ATENÇÃO!!! O seu limite é de R$ 500.00 por saque.')
                    print()
                print(f'-> Você ainda possui {limite_saque} saques disponíveis hoje.')
                print()
            else:
                print(f'>> Você atingiu seu limite de 3 saques diários. Por favor, volte outro dia.')
                print()        
        else:
            print(f'>> Você não tem saldo suficiente para realizar esse saque, por favor, informe outro valor.')
    elif operacao == 3:
        print(f'>>> Você selecionou a opção {nome_operacoes[2]}:')
        print()
        print(f'>{nome_operacoes[4].center(30)}<')
        print()
        for i, v in enumerate(extrato_deposito):
            print(f'- {i + 1}º depósito -> R$ {v};')
        print(f'>{nome_operacoes[5].center(30)}<')
        print()
        for i, v in enumerate(extrato_saque):
            print(f'- {i + 1}º saque -> R$ {v};')
        print(f'>{nome_operacoes[6].center(30)}<')
        print()
        print(f'- R$ {saldo}')
        print('-' * 34)
    elif operacao == 4:
        print('===== $Muito obrigado e volte sempre!$ =====')
        break
    else:
        print('>>> ATENÇÃO!!! Valor não corresponde com as opções em menu. Digite uma opção válida...')
        print()
