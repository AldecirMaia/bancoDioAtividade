"""_summary_
Deposito
    O app deve ser possivel depositar valores positivos na conta bancaria
Saque
    limite maximo de 3 saques por dia, com limite maximo de 500 reais por saque
Extrato
    exibir o saldo
"""

saldo = 0
limite = 500
extrato = [""]
numero_saque = 0
limite_saque = 3
while True:
    opcao = int(input(
        "Digite a sua opçao \n 1 - para Deposito \n 2 - para Saque \n 3 - para Extrato \n 4 - para sair"))

    if opcao == 1:
        valor_saldo = float(input("Digite o valor a ser depositado"))
        if valor_saldo < 0:
            print("Digite um valor valido")
        else:
            saldo += valor_saldo
            print(f"o valor deposito foi de R$ {saldo:.2f} ")
    elif opcao == 2:
        valor_saque = float(input("Digite o valor a ser sacado"))
        if valor_saque <= 500 and valor_saque <= saldo:
            numero_saque += 1
            extrato.append(valor_saque)
            if numero_saque == limite_saque:
                saldo = saldo
                print("Voce ja realizou o limite maximo de saques no dia!")
            else:
                print("saque realizado com sucesso")
                saldo = saldo - valor_saque
        else:
            print("O valor do saque é maior que o permitido")

    elif opcao == 3:
        print(f"Seu saldo atual é de R$ {saldo}")
        print(f"Saques realizados R$ {extrato}")
    elif opcao == 4:
        print("Obrigado por utilizar nosso BANCO")
        break
    else:
        print("Digite uma opção valida")
