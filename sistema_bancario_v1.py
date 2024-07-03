menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "d":
        print("DEPOSITAR\n\n")
        
        deposito = float(input("Digite o valor para depósito: =>"))
        
        if deposito <= 0:
            print("ERRO - Valor inválido! Repita a operação!")
        else:
            saldo += deposito
            extrato += f"Depósito    R$ {deposito:.2f}\n"
        
    elif opcao == "s":
        print("SACAR\n\n")
        
        saque = float(input("Digite o valor de saque: =>"))
        
        if saque <= 0 or saque > saldo or numero_saques >= LIMITE_SAQUES :
            print("ERRO - Valor inválido! Repita a operação!")
        else:
            saldo -= saque
            extrato += f"Saque    R$ {deposito:.2f}\n"
        
    elif opcao == "e":
        print("EXTRATO\n\n")
        print(extrato)
        
    elif opcao == "q":
        print("SAIR\n\n")
        break
    
    else:
        print("Opção inválida, escolha novamente!")

print("Obrigado por usar nosso sistema!\n\n")
