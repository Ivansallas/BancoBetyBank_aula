## Sistema Bancário PROGRAMAÇÃO ORIENTADA A OBJETOS
print("****************************************************")
print("*******BEM VINDO AO SISTEMA BANCÁRIO****************")
print("****************************************************")

def criar_conta(numero_conta, titular, saldo_inicial, limite):
    conta = {
        "numero": numero_conta,
        "titular": titular,
        "saldo": saldo_inicial,
        "limite": limite
    }    
    return conta

def depositar(conta, valor):
    conta["saldo"] += valor
    
def sacar(conta, valor):
    conta["saldo"] -= valor
    
def extrato(conta):
    print("Saldo da conta {}: ".format(conta["saldo"]))

def transferir(conta_origem, conta_destino, valor):
    sacar(conta_origem, valor)
    depositar(conta_destino, valor)
    
# Criar a instacia da conta
conta1 = criar_conta("12345", "João Silva", 1000.0, 500.0)
conta2 = criar_conta("54321", "Maria Oliveira", 2000.0, 1000.0)

depositar(conta1, 500.0)
extrato(conta1)
sacar(conta1, 200.0)
extrato(conta1)
transferir(conta1, conta2, 300.0)
extrato(conta1)
extrato(conta2)