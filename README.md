`A Versão atualizada está concentrada na branch VERSAO 2 deste repositório`

-----

# Sistema Bancário Simplificado em Python

Este é um sistema bancário básico, interativo e em sua primeira versão, desenvolvido em Python. Ele permite que o usuário realize operações financeiras simples e essenciais, incluindo solicitação de empréstimo.

-----

## Funcionalidades

O sistema oferece um menu simples com as seguintes opções:

  * **[d] Depositar**: Adicione dinheiro à sua conta.
  * **[s] Sacar**: Retire dinheiro, respeitando limites diários e por transação.
  * **[e] Extrato**: Visualize todas as suas movimentações e o saldo atual.
  * **[a] Ajuda\_Emprestimo**: Simule um empréstimo, verificando sua elegibilidade e calculando as parcelas com juros.
  * **[q] Sair**: Encerre o programa a qualquer momento.

-----

## Regras de Negócio e Limites do Sistema

O banco simplificado opera com algumas regras internas:

  * **Depósito**: Apenas valores maiores que zero são aceitos.
  * **Saque**:
      * **Limite por saque**: Você só pode sacar até `R$ 500,00` por vez.
      * **Limite diário**: Máximo de `3` saques por dia.
      * Não é possível sacar mais do que o seu **saldo** atual.
      * Constar no **extrato** todo saque realizado.
      * Exibir os em valores monetários em decimais (R$ xxx.xx)
   
    -----

## Minha Sugestão e Aplicado de Regras de Negócio
     
  * **Empréstimo**:
      * O valor pedido deve ser **positivo**.
      * **Elegibilidade**: Para simular um empréstimo, seu **`limite_acumulado`** (total de saques feitos) deve ser de, no mínimo, `R$ 1500,00`.
      * O valor do empréstimo não pode ser mais do que o **dobro** do seu **`limite_acumulado`**.
      * Você precisa ter um **saldo** equivalente a pelo menos **10%** do valor do empréstimo solicitado.
      * Se aprovado, você pode escolher de `1` a `12` parcelas.
      * A taxa de juros aplicada na simulação é de `5% ao mês`.
      * O **`limite_acumulado`** registra o total que você já sacou (usado para regras de empréstimo).


-----

## Estrutura do Código

O código é construído em um **loop principal (`while True`)** que exibe o menu e processa a escolha do usuário até que a opção de sair seja selecionada.

  * **Variáveis Iniciais**: `saldo`, `limite`, `limite_acumulado`, `extrato`, `numero_saques` e `LIMITE_SAQUES` são definidas no início e controlam o estado do banco.
  * **Controle de Fluxo**: As operações são gerenciadas por uma cadeia de `if`/`elif` com base na opção escolhida pelo usuário.
  * **Seção de Empréstimo (`[a]`)**: Esta seção possui uma lógica mais complexa, usando uma **variável de status (`emprestimo_aprovado`)** para guiar o fluxo. Primeiro, são verificadas todas as condições de negação. Se nenhuma delas for verdadeira, o empréstimo é considerado "pré-aprovado", e então o sistema pede e valida o número de parcelas.
  * **Tratamento de Erros**: O sistema usa blocos `try-except` para capturar entradas inválidas do usuário (como digitar texto onde se espera um número), prevenindo que o programa trave.
  * **Formatação de Saída**: Utiliza **f-strings** com formatação `:.2f` para garantir que valores monetários sejam exibidos com duas casas decimais, de forma clara e profissional.

-----

## Melhorias Futuras

Este é um ponto de partida\! Você pode expandir este sistema com as seguintes ideias:

  * **Histórico de Empréstimos**: Adicionar informações de empréstimos concedidos ao extrato.
  * **Funções**: Organizar o código em funções para cada operação (depósito, saque, extrato, empréstimo) para melhor legibilidade e manutenção.
  * **Persistência de Dados**: Salvar os dados do `saldo`, `extrato` etc. em um arquivo para que as informações não se percam ao fechar o programa.
  * **Novas Operações**: Adicionar funcionalidades como transferências, pagamento de contas, etc.

-----


Sou novato nesse mundo da tecnologia então que tal conectar comigo no LinkdIn? [Clique Aqui](edin.com/in/fernando-m-do-valle-b653a7349/)

<img src="https://raw.githubusercontent.com/DaDosValle/Imagens/refs/heads/main/minha%20logomarca%20analista%20e%20devs.jpg" width="300">
