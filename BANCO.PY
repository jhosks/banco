def cadastrar_codigos():
    contas = []
    saldos = []
    
    for c in range(2):
        codigo = int(input("Digite o código da conta: "))
        saldo = float(input("Digite o saldo da conta: "))
        contas.append(codigo)
        saldos.append(saldo)
    return contas, saldos

def mostrar_contas(contas, saldos):
    print("Contas - Saldos: ")
    for c in range (len(contas)):
        print("Conta: ", contas[c], " | Saldo: ", saldos[c])

def realizar_deposito(contas, saldos):
    codigo = int(input("Digite o código da conta: "))
    valor = float(input("Digite o valor a ser depositado: "))
    
    if codigo in contas:
        b = contas.index(codigo)
        saldos[b] += valor
        print("Depósito realizado com sucesso! c:")
    else:
        print("Conta não encontrada. :c")
        
def realizar_saque(contas, saldos):
    codigo = int(input("Digite o código da conta: "))
    valor = float(input("Digite o valor a ser sacado: "))
    
    if codigo in contas:
        b = contas.index(codigo)
        saldo = saldos[b]
        
        if saldo >= valor:
                saldos[b] -= valor
                print("Saque realizado com sucesso! :D")
        else:
            print("Conta não encontrada. :c")

def consultar_saldo(saldos):
    ativo = sum(saldos)
    print("O saldo bancário é: ", ativo)

contas, saldos = cadastrar_codigos()

while True:
    print("\nMenu: ")
    print("1 - Realizar Depósito")
    print("2 - Realizar Saque")
    print("3 - Consultar o ativo bancário")
    print("4 - Finalizar Programa")
    
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        realizar_deposito(contas, saldos)
    elif opcao == 2:
        realizar_saque(contas, saldos)
    elif opcao == 3:
        consultar_saldo(saldos)
    elif opcao == 4:
        break
    else:
        print("Opção não encontrada. Retorne ao Menu.")