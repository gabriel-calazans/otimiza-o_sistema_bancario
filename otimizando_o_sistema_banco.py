def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("✅ Depósito realizado com sucesso.")
    else:
        print("❌ Operação falhou! Valor inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("❌ Valor inválido para saque.")
    elif valor > saldo:
        print("❌ Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("❌ Operação falhou! Valor excede o limite de saque.")
    elif numero_saques >= limite_saques:
        print("❌ Operação falhou! Limite diário de saques atingido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("✅ Saque realizado com sucesso.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Sem movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("❌ Já existe usuário com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nasc,
        "cpf": cpf,
        "endereco": endereco
    })

    print("✅ Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    return next((u for u in usuarios if u["cpf"] == cpf), None)

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("❌ Usuário não encontrado. Conta não criada.")
        return

    contas.append({
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    })

    print(f"✅ Conta criada com sucesso! Número: {numero_conta}")

def listar_contas(contas):
    print("\n=========== CONTAS ===========")
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")
    print("================================")

# Programa principal
def main():
    AGENCIA = "0001"
    usuarios = []
    contas = []
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    contador_contas = 1

    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar usuário
[c] Criar conta
[l] Listar contas
[q] Sair
=> """

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            valor = float(input("Valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo, valor=valor, extrato=extrato,
                limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            criar_conta(AGENCIA, contador_contas, usuarios, contas)
            contador_contas += 1

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            print("✅ Sistema encerrado.")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
