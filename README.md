# Sistema Bancário em Python Versão 

Este é um sistema bancário simples desenvolvido em Python que simula operações básicas como cadastro de usuários, abertura de contas, depósitos, saques, extratos e solicitação de empréstimos.

---

## Sumário

- [Sobre](#sobre)
- [Funcionalidades](#funcionalidades)
- [Como usar](#como-usar)
- [Estrutura do Código](#estrutura-do-código)
- [Variáveis e Constantes](#variáveis-e-constantes)
- [Funções](#funções)
- [Fluxo do Programa](#fluxo-do-programa)
- [Considerações Finais](#considerações-finais)

---

## Sobre

Este sistema tem como objetivo oferecer uma interface simples e interativa para simular operações bancárias cotidianas. O usuário pode cadastrar clientes, criar contas vinculadas a esses clientes, realizar depósitos, saques limitados, consultar extratos e solicitar empréstimos com regras básicas de aprovação.

---

## Funcionalidades

- Cadastro de usuários com dados pessoais (nome, CPF, data de nascimento, endereço).
- Criação de contas bancárias vinculadas aos usuários cadastrados.
- Listagem de contas abertas.
- Depósito em conta.
- Saques com limites de valor, quantidade máxima diária e saldo disponível.
- Visualização do extrato da conta, incluindo depósitos, saques e informações sobre empréstimos.
- Solicitação de empréstimos com pré-aprovação baseada em critérios (histórico de saques, saldo e valor solicitado).
- Cálculo detalhado do empréstimo com número de parcelas, juros mensais e valor final.

---

## Como usar

1. Execute o script Python.
2. No menu principal, escolha uma opção digitando a letra correspondente:
   - `u`: Cadastrar usuário
   - `c`: Cadastrar conta
   - `l`: Listar contas
   - `d`: Depositar
   - `s`: Sacar
   - `e`: Extrato
   - `a`: Ajuda para empréstimo
   - `q`: Sair do sistema
3. Siga as instruções apresentadas para cada operação.
4. Ao finalizar, escolha a opção para sair ou retornar ao menu principal.

---

## Estrutura do Código

O código está organizado com:

- Variáveis globais para controle do saldo, limites, extrato e empréstimos.
- Constantes para limites de saque e número da agência.
- Listas para armazenar usuários e contas.
- Funções específicas para cada funcionalidade (ex: criar usuário, depositar, sacar, etc).
- Laço principal (`while True`) para exibir o menu e receber comandos do usuário.

---

## Variáveis e Constantes Principais

| Variável                | Descrição                                             |
|------------------------|-------------------------------------------------------|
| `saldo`                | Saldo atual da conta                                   |
| `limite`               | Limite máximo permitido para saque                    |
| `limite_acumulado`     | Total acumulado em saques para controle de empréstimos|
| `extrato`              | String que guarda o histórico de transações           |
| `numero_saques`        | Quantidade de saques realizados no dia                 |
| `valor_emprestimo`     | Valor solicitado para empréstimo                        |
| `parcelas`             | Número de parcelas para pagamento do empréstimo        |
| `total_juros_emprestimo`| Juros totais calculados para o empréstimo             |
| `valor_parcela_com_juros`| Valor de cada parcela incluindo juros                 |
| `LIMITE_SAQUES`        | Constante para limite máximo diário de saques          |
| `AGENCIA`              | Número fixo da agência bancária                         |
| `usuarios`             | Lista contendo os usuários cadastrados                  |
| `contas`               | Lista contendo as contas abertas                         |

---

## Funções

### `menu()`

Exibe o menu principal e retorna a opção escolhida pelo usuário.

---

### `depositar(saldo, valor, extrato)`

Realiza um depósito no saldo, atualiza o extrato e retorna os novos valores.

---

### `saque(saldo, valor, extrato, limite, numero_saques, limite_saques, limite_acumulado)`

Realiza um saque verificando se o valor solicitado não excede saldo, limite ou número máximo de saques. Atualiza o saldo, extrato, número de saques e limite acumulado.

---

### `extrato_movimentacao(saldo, extrato)`

Exibe o extrato da conta, incluindo saldo atual e informações sobre empréstimos solicitados.

---

### `criar_usuario(usuarios)`

Permite o cadastro de um novo usuário solicitando CPF, nome, data de nascimento e endereço. Verifica se o usuário já existe pelo CPF.

---

### `filtrar_usuario(cpf, usuarios)`

Retorna o usuário correspondente ao CPF informado ou `None` caso não exista.

---

### `criar_conta(agencia, numero_conta, usuarios)`

Cria uma nova conta vinculada a um usuário já cadastrado, solicitando o CPF para validação.

---

### `listar_contas(contas)`

Lista todas as contas cadastradas com seus dados principais.

---

## Fluxo do Programa

- Inicia o programa exibindo o menu principal.
- Usuário escolhe a operação desejada.
- De acordo com a operação, o programa chama a função correspondente.
- Após a operação, oferece ao usuário a opção de voltar ao menu ou encerrar o programa.
- O programa só termina quando o usuário escolhe sair (opção `q`).

---

## Considerações Finais

Este projeto é uma base simples para o entendimento de operações bancárias em Python. Pode ser expandido com funcionalidades adicionais como autenticação, controle de múltiplas contas por usuário, persistência de dados, interface gráfica, entre outros.

---

Se desejar ajuda para evoluir o projeto ou adicionar funcionalidades, estou à disposição!

[Fernando do Valle -LinkdIn](https://www.linkedin.com/in/fernando-m-do-valle)
