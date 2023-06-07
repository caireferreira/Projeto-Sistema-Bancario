
def menu():
    menu = """\n

    ============ CAIRÊ BANK ============

             Seja bem-vindo(a)!

    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [nc]\tNova conta
    [lc]\tListar minhas contas
    [nu]\tNovo usuário
    [q] \tSair

    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /): #REGRA: RECEBER OS ARGUMENTOS APENAS POR POSIÇÃO
    if valor > 0:
            saldo += valor
            extrato += f"Depósito :\tR$ {valor:.2f}\n"
            print("\n Uhul!! Depósito realizado! :)")

    else:
        print("\n Oh não, Operação falhou! O valor informado é inválido! :(")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):#REGRA: RECEBER OS ARGUMENTOS APENAS POR CHAVE = NOMEADOS
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo: #IF EXCEDEU O SALDO
            print("\n Oh não! Seu saldo insuficiente! :(")

        elif excedeu_limite:#IF EXCEDEU O LIMITE
            print("\n Oh não! O valor do saque excede o seu limite! :(")

        elif excedeu_saques:#IF EXCEDEU O SAQUE
            print("\n Oh não! Você excedeu seu número de saques diários! :(")

        elif valor > 0: #ELIF PARA MOSTRAR O SAQUE FEITO
            saldo -= valor
            extrato += f"Saque: \t\tR$ {valor:.2f}\n"
            numero_saques += 1
            print("\n Uhul!! Saque realizado! :)")

        else:
            print("\n Oh não, Operação falhou! O valor informado é inválido! :(")

        return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):#REGRA RECEBER SALDO POR ARGUMENTO POSICIONAL E EXTRATO POR ARGUMENTO NOMEADO
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\tR$ {saldo:.2f}")
    print("=============================")

def criar_usuario(usuarios): #REGRA NÃO PODE CADASTRAR 2 USUARIOS COM O MESMO CPF
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios) #VERIFICA SE O CPF JÁ EXISTE

    if usuario: #RESPOSTA CASO JÁ EXISTA O USUÁRIO
        print("Opa! Já exite um usuário com esse CPF")
        return
    
    #CASO NÃO EXISTA, RECOLHE AS INFORMAÇÕES
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (Logradouro, numero - Bairro - Cidade/UF): ")

    #ADICIONA COMO DICIONARIO (CHAVE:VALOR)
    usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})

    print("Usuário criado! É bom demais ter você com a gente! :D")

def filtrar_usuario(cpf, usuarios): #FILTRA DENTRO DA LISTA USUARIOS SE O CAMPO "CPF" ESTÁ PREENCHIDO COM O CPF INFORMADO!
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] #COMPRESSÃO DE LISTAS

    return usuarios_filtrados[0] if usuarios_filtrados else None 
    #VERIFICA SE O FILTRO É OU NÃO UMA LISTA VAZIA! CASO NÃO ENCONTRAR RETORNARÁ "NONE", SE ESTIVER PREENCHIDA RETORNARÁ O PRIMEIRO ELEMENTO ACHADO NO FILTRO.

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o seu CPF: ") #PEGA O CPF PARA JA VINCULAR A CNOVA CONTA AO CPF DO USUÁRIO
    usuario = filtrar_usuario(cpf, usuarios) #UTILIZA O MESMO FILTRO DE NOVO USUÁRIO

    if usuario: #CASO ENCONTRE O USUÁRIO, CRIAMOS A CONTA E VINCULA A CONTA DELE
        #CRIA UM DICIONARIO DA CONTA (CHAVE:VALOR)
        print("\n Uhul! Conta criada com sucesso! :D")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}

    print("\n Não localizamos o seu CPF! Crie seu usuário e abra sua conta com a gente! :D")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0 
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:

        opcao = menu() #GUARDA A INFORMÇÃO DADA NO MENU

        if opcao == "d": #IF DE DEPÓSITO
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s": #IF DE SAQUE
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e": #IF DE EXTRATO
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu": #IF DE CRIAR USUARIO
            criar_usuario(usuarios)

        elif opcao == "nc":#IF DE CRIAÇÃO DE CONTA
            numero_conta = len(contas) + 1 #FAZ A CONTAGEM E ADICIONA MAIS UMA CONTA POR CPF.
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a opção desejada.")

main()
