saldo = 0
limite = 500
limite_acumulado = 0
extrato = ""
numero_saques = 0
valor_emprestimo = 0
parcelas = 0
total_juros_emprestimo = 0
valor_parcela_com_juros = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []



def menu():
    menu = """
    Seja bem_vindo(a) ao maior banco do Olá, Mundo!

    Como podemos ajudar hoje? Escolha uma opção:

    [u] Cadastrar_Usuario
    [c] Cadastrar_Conta
    [l] Listar_Conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [a] Ajuda_Emprestimo
    [q] Sair

    Digite Aqui => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"""
                  
        Valor de R$ {valor} depositado com sucesso!
                  
        \n""")                           
    else:
        print("Operação falhou! O valor informado é inválido.")
            
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques, limite_acumulado):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Você não tem saldo suficiente. Consulte o seu saldo e tente novamente\n")
        encerramento = input("Digite M para voltar ao menu.\n").upper()
        if encerramento == "M":
            print(menu())
    
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.\n")
        encerramento = input("Digite M para voltar ao menu.\n").upper()
        if encerramento == "M":
            print(menu())
        
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.\n")
        encerramento = input("Digite M para voltar ao menu.\n").upper()
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        limite_acumulado += valor
        
        print("Saque realizado com sucessos. Tenha um excelente dia!\n")
        encerramento = input("Digite M para voltar ao menu.\n").upper()
        if encerramento == "M":
            print(menu())
    else:
        print("Falha! Operação não identificada.\n")
        print("Tente novamente!\n")
        encerramento = input("Digite M para voltar ao menu.\n").upper()
        if encerramento == "M":
            print(menu())
            
    return saldo, extrato, numero_saques, limite_acumulado

def extrato_movimentacao(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}\n")
    print(f"Valor do empréstimo solicitado: R$ {valor_emprestimo:.2f}")
    print(f"Valor total a pagar (incluindo juros): R$ {valor_emprestimo + total_juros_emprestimo:.2f}")
    print(f"Número de parcelas: {parcelas}")
    print(f"Valor de cada parcela (com juros): R$ {valor_parcela_com_juros:.2f}")
    print("==========================================\n")

def criar_usuario(usuarios):
    
    cpf = input("Informe o seu CPF (somente numero sem traços): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nJá existe um usuário com esse cadastro. Tente Novamente!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento conforme exemplo: dd/mm/aaaa: ")
    endereco = input("Por favor, informe o seu endereço seguindo o exemplo: (logradouro, numero - bairro - cidade/sigla do estado): ")
    
    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Concluido!\n")
    print("Acesse a sua conta!")
    encerramento = input("Digite M para voltar ao menu.\n").upper()
    if encerramento == "M":
        print(menu())

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuarios:
        print("\n A sua conta foi criada. Aproveite para acessá-la")
        return {"agencia":agencia, "numero_conta": numero_conta, "usuario":usuario}
    else:
        print("Usuário não encontrado. Verifique seus dados e tente novamente!")
            
        
        
def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agencia:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print(linha)
         


while True:
    opcao = menu()
    if opcao == "d" or opcao == "D":
        valor = float(input("Informe o valor do depósito:  "))
        saldo, extrato = depositar(saldo, valor, extrato)
        encerramento = input("Digite M para voltar ao menu ou X para encerrar. ").upper()
        if encerramento == "M":
            print(menu())     
        elif encerramento == "X":
            print("Obrigado por utilizar nossos serviços!\n")
            break

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques, limite_acumulado = saque(
            saldo = saldo,
            valor = valor,
            extrato = extrato,
            limite = limite,
            numero_saques = numero_saques,
            limite_saques= LIMITE_SAQUES,
            limite_acumulado=limite_acumulado
        )

    elif opcao == "e":       
        extrato_movimentacao(saldo, extrato=extrato)
        encerramento = input("Digite M para voltar ao menu ou X para encerrar.\n").upper()
        if encerramento == "M":
            print(menu())
        else:
            break

    elif opcao == "a":
        emprestimo_aprovado = False
        mensagem_negacao = "" 
        valor_emprestimo = float(input("Quanto reais (R$) você precisa para o empréstimo?\n"))
        if valor_emprestimo <= 0:
            mensagem_negacao = "Operação de empréstimo falhou! O valor solicitado deve ser positivo."
        elif limite_acumulado < 1500:
            mensagem_negacao = f"Empréstimo não autorizado. Seu histórico de uso (limite acumulado: R${limite_acumulado:.2f}) ainda não atende aos requisitos mínimos (R$1500) para esta linha de crédito."
        elif valor_emprestimo > (limite_acumulado * 2):
            mensagem_negacao = "Empréstimo não autorizado. O valor solicitado excede a proporção permitida em relação ao seu limite acumulado."
        elif saldo < valor_emprestimo * 0.10:
            mensagem_negacao = "Empréstimo não autorizado. Saldo insuficiente para o valor solicitado. Mantenha um saldo mínimo."
        else:
            emprestimo_aprovado = True
    
        if emprestimo_aprovado:
            print("\nSeu empréstimo foi pré-aprovado! Agora, vamos definir as parcelas.")
            parcelas = 0 
            try:
                parcelas = int(input("De 1 até 12 parcelas. Quantas parcelas deseja para seu empréstimo? "))
            except ValueError:
                print("Entrada inválida para o número de parcelas. Por favor, digite um número inteiro.")
                
            if 0 < parcelas <= 12: 
                calculo_emprestimo_base = valor_emprestimo / parcelas 
                taxa_juros_percentual = 0.05
                valor_parcela_com_juros = calculo_emprestimo_base * (1 + taxa_juros_percentual)
                valor_da_taxa_por_parcela = calculo_emprestimo_base * taxa_juros_percentual
                total_juros_emprestimo = valor_da_taxa_por_parcela * parcelas
                print(f"\n--- Detalhamento do seu Empréstimo ---")
                print(f"Valor do empréstimo solicitado: R$ {valor_emprestimo:.2f}")
                print(f"Número de parcelas: {parcelas}")
                print(f"Valor de cada parcela (com juros): R$ {valor_parcela_com_juros:.2f}")
                print(f"Valor da taxa de juros por parcela: R$ {valor_da_taxa_por_parcela:.2f}")
                print(f"Taxa percentual aplicada: {taxa_juros_percentual * 100:.0f}% ao mês")
                print(f"Total de juros no empréstimo: R$ {total_juros_emprestimo:.2f}")
                print(f"Valor total a pagar (incluindo juros): R$ {valor_emprestimo + total_juros_emprestimo:.2f}")
                break
            else:
                print("Número de parcelas inválido. Por favor, escolha um número de 1 a 12.")
        else: 
            print(mensagem_negacao)
            
    elif opcao == "q":
        print("Obrigado por utilizar nosso serviço. Tenha um excelente dia!.\n")
        break

    elif opcao == "u":
        criar_usuario(usuarios)
        
    elif opcao == "c":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
                    
    elif opcao == "l":
        listar_contas(contas)
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        