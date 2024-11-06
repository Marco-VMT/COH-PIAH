# Bibliotecas
import re


# Função de entrada

def entrada_float(mensagem):
    '''A função controla o tipo de varíavel inserida.'''
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Insira um número decimal.")


# Funções de texto

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    
    print("\nBem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")


    wal = entrada_float("Entre o tamanho médio de palavra:")
    ttr = entrada_float("Entre a relação Type-Token:")
    hlr = entrada_float("Entre a Razão Hapax Legomana:")
    sal = entrada_float("Entre o tamanho médio de sentença:")
    sac = entrada_float("Entre a complexidade média da sentença:")
    pal = entrada_float("Entre o tamanho medio de frase:")

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


# Funções de apoio aos cálculos


def contar_caracteres(lista_qualquer):
    '''Recebe uma lista qualquer e retorna a quantidade de caracteres.'''
    n_caracter = 0
    if type(lista_qualquer) == str:
            n_caracter += len(lista_qualquer)
    else:
        for l_q in lista_qualquer:
            n_caracter += len(l_q)

    return n_caracter


def lista_sentencas(t):
    '''Recebe um texto e retorna uma lista com todas as sentenças.'''  
    
    lista_de_sentencas_por_texto = []
    lista_de_sentencas = []
    lista_de_sentencas_por_texto = separa_sentencas(t)
    lista_de_sentencas.append(lista_de_sentencas_por_texto)
                      
    return lista_de_sentencas


def lista_frases(t):
    '''Recebe um texto e retorna uma lista com todas as frases.'''  
    
    lista_de_sentencas = lista_sentencas(t)
    lista_de_frases = []
    total_lista_de_frases = []

    for lista_s_posicao in lista_de_sentencas:
        for lista_f_posicao in lista_s_posicao:       
                frase = separa_frases(lista_f_posicao)
                lista_de_frases.append(frase)

        total_lista_de_frases.append(lista_de_frases)
        lista_de_frases = []

    return total_lista_de_frases


def total_palavras(t):
    '''Recebe um texto e retorna com o número total de palavras.'''  
    n_palavras = []
    
    n_palavra = 0
    sentenca = separa_sentencas(t)

    for s in sentenca:
        frase = separa_frases(s)

        for f in frase:
            palavra = separa_palavras(f)
            n_palavra += len(palavra)

    n_palavras.append(n_palavra)
                       
    return n_palavras


def total_caracteres(t):
    n_caracteres = []
    
    n_caracter = 0
    sentenca = separa_sentencas(t)

    for s in sentenca:
        frase = separa_frases(s)

        for f in frase:
            palavra = separa_palavras(f)

            for p in palavra:
                n_caracter += len(p)

    n_caracteres.append(n_caracter)
    
    return n_caracteres


def total_palavras_diferentes(t):
    '''Recebe um texto e retorna o número de palavras diferentes.'''  
    
    qtd_palavras_diferentes = []
    lista_palavras = []
    
    qtd_palavras_diferente = 0
    sentenca = separa_sentencas(t)

    for s in sentenca:
        frase = separa_frases(s)

        for f in frase:
            lista_palavras_individuais = separa_palavras(f)  
            lista_palavras = lista_palavras + lista_palavras_individuais                                      

    qtd_palavras_diferente += n_palavras_diferentes(lista_palavras)
    qtd_palavras_diferentes.append(qtd_palavras_diferente)
                       
    return qtd_palavras_diferentes


def total_palavras_unicas(t):
    '''Recebe um texto e Retorna o número de palavras usadas uma única vez.'''  
    qtd_palavras_unicas = []
    lista_palavras_unica = []
    
    qtd_palavras_unica = 0
    sentenca = separa_sentencas(t)

    for s in sentenca:
        frase = separa_frases(s)

        for f in frase:
            lista_palavras_unica_individuais = separa_palavras(f)  
            lista_palavras_unica = lista_palavras_unica + lista_palavras_unica_individuais                                      

    qtd_palavras_unica +=n_palavras_unicas(lista_palavras_unica)
    qtd_palavras_unicas.append(qtd_palavras_unica)
    lista_palavras_unica = []
                           
    return qtd_palavras_unicas


def total_frases(t):
    '''Recebe um texto e retorna o número de frases.'''
    n_frases = 0
    lista_de_frases = lista_frases(t)
    numero_total_frases = []
    
    for l_f in lista_de_frases:
        for frases in l_f:
            n_frases += len(frases)
        numero_total_frases.append(n_frases)
        n_frases = 0

    return numero_total_frases


# Funções de Cálculo dos Índices

def eq_wal(t):
    '''Recebe um texto e calcula o tamanho médio de palavra (média simples do número de caracteres por palavra).'''
    wal_b = []

    n_caracteres = total_caracteres(t)
    n_palavras = total_palavras(t)

    for n_c in n_caracteres:
        wal = n_c / n_palavras[n_caracteres.index(n_c)]
        wal_b.append(wal)
        
    return wal_b


def eq_ttr(t):
    '''Recebe um texto e calcula a Relação Type-Token (número de palavras diferentes utilizadas em um texto divididas pelo total de palavras).'''
    ttr_b = []

    n_palavras = total_palavras(t)
    qtd_palavras_diferentes = total_palavras_diferentes(t)

    for qtd_p_d in qtd_palavras_diferentes:
        ttr = qtd_p_d / n_palavras[qtd_palavras_diferentes.index(qtd_p_d)]
        ttr_b.append(ttr)

    return ttr_b


def eq_hlr(t):
    '''Recebe um texto e calcula a Razão Hapax Legomana (número de palavras utilizadas uma única vez dividido pelo número total de palavras).'''
    hlr_b = []

    n_palavras = total_palavras(t)
    qtd_palavras_unicas = total_palavras_unicas(t)

    for qtd_p_u in qtd_palavras_unicas:
        hlr = qtd_p_u / n_palavras[qtd_palavras_unicas.index(qtd_p_u)]
        hlr_b.append(hlr)

    return hlr_b


def eq_sal(t):
    '''Recebe um texto e calcula o tamanho médio de sentença (média simples do número de caracteres por sentença).'''
    sal_b = []
    caracteres_sentenca = []
    total_caracteres_sentencas = []
    
    lista_de_sentencas = lista_sentencas(t)

    for l_s in lista_de_sentencas:
        for valor in l_s:
            n_caracteres_sentenca = contar_caracteres(valor)
            caracteres_sentenca.append(n_caracteres_sentenca)

        total_caracteres_sentencas.append(caracteres_sentenca)
        caracteres_sentenca = []

    for t_c_s in total_caracteres_sentencas:
        sal = sum(t_c_s) / len(total_caracteres_sentencas[total_caracteres_sentencas.index(t_c_s)])
        sal_b.append(sal)

    return sal_b


def eq_sac(t):
    '''Recebe um texto e calcula a complexidade de sentença (média simples do número de frases por sentença).'''
    sac_b = []
    quantidade_frases = []
    total_lista_frases = []

    lista_de_frases = lista_frases(t)

    for l_f in lista_de_frases:
        for frases_internas in l_f:
            n_frases = len(frases_internas)
            quantidade_frases.append(n_frases)

        total_lista_frases.append(quantidade_frases)
        quantidade_frases = []
    
    for t_l_f in total_lista_frases:
        sac = sum(t_l_f) / len(t_l_f)
        sac_b.append(sac)
    
    return sac_b


def eq_pal(t):
    '''Recebe um texto e calcula o tamanho médio de frase (média simples do número de caracteres por frase).'''
    pal_b = []
    caracteres_frase = []
    total_caracteres_frases = []
    
    lista_de_frases = lista_frases(t)
    numero_frases = total_frases(t)

    for l_f in lista_de_frases:
        for valor in l_f:
            n_caracteres_frase = contar_caracteres(valor)
            caracteres_frase.append(n_caracteres_frase)

        total_caracteres_frases.append(caracteres_frase)
        caracteres_frase = []
    
    for t_c_f in total_caracteres_frases:
        pal = sum(t_c_f) / numero_frases[total_caracteres_frases.index(t_c_f)]
        pal_b.append(pal)

    return pal_b


# Funções de análise dos indicadores

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    ass_cp = []
    diferencas = []

    somatoria_ass = 0

    if (type(as_a) == list and len(as_a) == 6) and (type(as_b) == list and len(as_b) == 6):
        for ass_a in as_a:
            modulo_da_diferença = abs((ass_a - as_b[as_a.index(ass_a)]))
            somatoria_ass += modulo_da_diferença
        ass_cp = somatoria_ass / len(as_a)
        return ass_cp
    
    else:
        if len(as_b) == len(as_a):
            for as_b_n in as_b:
                modulo_da_diferença = abs(as_b_n - as_a[as_b.index(as_b_n)])
                somatoria_ass += modulo_da_diferença
            ass_cp = somatoria_ass / len(as_a)
            return ass_cp
        
        else:
            for as_b_lista in as_b:
                for as_b_n in as_b_lista:
                    modulo_da_diferença = abs(as_b_n - as_a[as_b_lista.index(as_b_n)])
                    somatoria_ass += modulo_da_diferença
                diferencas.append(somatoria_ass)
                somatoria_ass = 0

        for dif in diferencas:
            if round(dif / len(as_a), 2) == 0:
                s_ab = 0
            else:       
                s_ab = dif / len(as_a)
            ass_cp.append(s_ab)
    
    ass_cp = min(ass_cp)
    return ass_cp
  

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.''' 

    as_b = []

    if len(texto) == 1 or type(texto) == str:
        if type(texto) == str:
            t = texto
        else:
            t = texto[0]

        as_b = eq_wal(t) + eq_ttr(t) + eq_hlr(t) + eq_sal(t) + eq_sac(t) + eq_pal(t)
        
        return as_b

    else:
        for t in texto:
            as_n = eq_wal(t) + eq_ttr(t) + eq_hlr(t) + eq_sal(t) + eq_sac(t) + eq_pal(t) #arrumar deixar para as funções ser executadas apenas uma vez 
            as_b.append(as_n)
            as_n = []

        return as_b


def avalia_textos(textos, as_a):
    '''Recebe uma lista de textos e uma assinatura de referência (as_a); retorna o número (1 a n) do texto com maior probabilidade de estar infectado por COH-PIAH.'''
    posicao = None
    menor_diferenca = float('inf')

    for i, t in enumerate(textos):
        assinaturas_dos_textos = calcula_assinatura(t)
        ass_cp = compara_assinatura(as_a, assinaturas_dos_textos)

        if ass_cp < menor_diferenca:
            menor_diferenca = ass_cp
            posicao = i + 1

    return posicao


# Função Principal

def main():
    '''Executa o programa completo'''
    as_a = le_assinatura()
    texto = le_textos()
    textos = texto
    as_b = calcula_assinatura(texto)
    ass_cp = compara_assinatura(as_a, as_b)
    texto_plagio = avalia_textos(textos, as_a)
    print("\nO autor do texto", texto_plagio,"está infectado com COH-PIAH")
    verificar_novamente = input("\nDeseja verificar outro texto? Y/N ")

    while verificar_novamente not in ("Y", "y", "N", "n"):
        print("\nEntrada inválida. Digite Y para verificar novamente ou N para não verificar.")
        verificar_novamente = input("Deseja verificar outro texto? Y/N ")

    return verificar_novamente


# Inicio do programa:

verificar_novamentre = main()


# Repetição do programa:

while verificar_novamentre in ("Y", "y"):
    verificar_novamentre = main()

quit()