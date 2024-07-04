
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
    
    print()
    print(" BEM VINDO! ".center(50,"-"))
    opcao = input(menu)
    
    if opcao == "d":
        print(" DEPOSITAR ".center(50,"-")+"\n")
        deposito = float(input("Digite o valor para depósito: => "))
        
        if deposito > 0:
            saldo += deposito
            extrato += "Depósito ".ljust(40,"-")+" R$"+f"{deposito:.2f}\n".rjust(10)
            
        else:
            print("ERRO - Valor inválido! Repita a operação!")
        
        print("".center(50,"-")+"\n")
           
    elif opcao == "s":
        print(" SACAR ".center(50,"-")+"\n")
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saques: 
           print(f"ERRO - Excedeu quantidade de saques diários!")
           
        else: 
            saque = float(input("Digite o valor de saque: =>"))
            excedeu_saldo = saque > saldo
            excedeu_limite = saque > limite
            
            if excedeu_saldo:
                print(f"ERRO - Saldo = R$ {saldo:.2f} insuficiente! Digite outro valor!")
                
            elif saque <= 0:
                print("ERRO - Valor inválido! Repita a operação!")
                
            elif saque > limite:
                print(f"ERRO - Valor acima do limite de R$ {limite:.2f}.! Digite outro valor!")
                
            else:  
                saldo -= saque
                numero_saques += 1
                extrato += "Saque ".ljust(40,"-") + " R$"+ f"{saque:.2f}\n".rjust(10)
                print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
                print(f"Saldo atual é de R$ {saldo:.2f}.")
                
        print("".center(50,"-")+"\n")
        
    elif opcao == "e":
        print(" EXTRATO ".center(50,"-")+"\n")
        print("Nenhuma operação realizada!"if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}.")
        input(" Press Enter para voltar! ".center(50, "-"))  
        
    elif opcao == "q":
        break
        
    
    else:
        print("Opção inválida, tente novamente!")
        
print("Obrigado por usar nosso sistema!\n")
