# Detector de Similaridade de Texto - COH-PIAH

Este projeto implementa um detector de similaridade de textos baseado em uma assinatura linguística. O código calcula várias métricas de um texto e compara com uma assinatura de referência para verificar a probabilidade de um texto estar "infectado" pelo estilo COH-PIAH.

## Funcionalidades

- **Entrada de Dados**: Permite ao usuário inserir textos e uma assinatura de referência.
- **Processamento Textual**: Divide textos em sentenças, frases e palavras, contabilizando palavras únicas e diferentes.
- **Métricas de Similaridade**: Calcula métricas linguísticas, como Tamanho Médio de Palavra, Razão Hapax Legomana e Complexidade de Sentença.
- **Análise de Similaridade**: Compara a assinatura do texto com a assinatura padrão para identificar similaridade.

## Estrutura do Código

### 1. Bibliotecas

- `re`: Utilizada para manipulação de expressões regulares na divisão de sentenças e frases.

### 2. Função de Entrada

- `entrada_float(mensagem)`: Solicita uma entrada do usuário e verifica se é um número decimal.

### 3. Funções de Entrada de Texto

- `le_assinatura()`: Recebe as métricas da assinatura linguística de referência.
- `le_textos()`: Lê os textos que serão comparados com a assinatura de referência.

### 4. Funções de Separação e Contagem

Estas funções separam o texto em componentes menores e contam palavras, frases e sentenças:

- `separa_sentencas(texto)`: Divide um texto em sentenças.
- `separa_frases(sentenca)`: Divide uma sentença em frases.
- `separa_palavras(frase)`: Divide uma frase em palavras.
- `n_palavras_unicas(lista_palavras)`: Conta palavras que aparecem apenas uma vez.
- `n_palavras_diferentes(lista_palavras)`: Conta palavras únicas em uma lista.

### 5. Funções Auxiliares

Funções que auxiliam o cálculo de métricas, como contagem de caracteres e criação de listas de sentenças e frases:

- `contar_caracteres(lista_qualquer)`: Conta caracteres em uma lista ou string.
- `lista_sentencas(t)`: Cria uma lista de sentenças de um texto.
- `lista_frases(t)`: Cria uma lista de frases de um texto.
- `total_palavras(t)`: Retorna o número total de palavras de um texto.
- `total_caracteres(t)`: Retorna o número total de caracteres de um texto.
- `total_palavras_diferentes(t)`: Retorna o número de palavras diferentes de um texto.
- `total_palavras_unicas(t)`: Retorna o número de palavras que aparecem uma única vez em um texto.
- `total_frases(t)`: Retorna o número de frases em um texto.

### 6. Funções para Cálculo dos Índices

Cada função calcula uma métrica específica usada para criar a assinatura do texto:

- `eq_wal(t)`: Calcula o tamanho médio de palavra.
- `eq_ttr(t)`: Calcula a relação Type-Token.
- `eq_hlr(t)`: Calcula a Razão Hapax Legomana.
- `eq_sal(t)`: Calcula o tamanho médio de sentença.
- `eq_sac(t)`: Calcula a complexidade média de sentença.
- `eq_pal(t)`: Calcula o tamanho médio de frase.

### 7. Funções de Análise dos Indicadores

- `compara_assinatura(as_a, as_b)`: Calcula o grau de similaridade entre duas assinaturas.
- `calcula_assinatura(texto)`: Gera a assinatura linguística de um texto.
- `avalia_textos(textos, as_a)`: Avalia uma lista de textos e retorna o índice do texto com maior similaridade com a assinatura de referência.

### 8. Função Principal

- `main()`: Coordena a execução do programa e exibe o resultado da análise de similaridade.

## Como Usar

1. Insira as métricas da assinatura de referência na função `le_assinatura()`.
2. Insira os textos para análise na função `le_textos()`.
3. O programa compara os textos com a assinatura de referência e exibe o texto com maior probabilidade de estar "infectado".

## Exemplo de Execução

Ao executar o código, o usuário será solicitado a:
1. Inserir uma assinatura de referência com valores como "Tamanho Médio de Palavra" e "Complexidade de Sentença".
2. Inserir o texto ou textos para análise.
3. O programa exibirá o índice do texto mais similar à assinatura de referência.
