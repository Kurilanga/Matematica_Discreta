# Primeira parte: Uso do comando "open" para abrir nosso arquivo de texto.
arquivo = open('arquivo3.txt', 'r')

# Segunda parte: Criação de uma variavel que recebe a leitura da primeira linha do nosso
# arquivo para que possamos saber quantas operações tem dentro dele.
primeira_linha = int(arquivo.readline())
# Terceita parte: Uso do "for" junto com o range da variavel "primeira_linha" para que este
# loop funcione para o numero de operações que temos no arquivo. Assim tambem filtrando,
# com as funçoes "split" e "strip", os demais valores que nao correspondem aos dos conjuntos,
# para que consigamos criar variaveis que guardam apenas os valores dos dois conjuntos que serão processados.
for x in range(primeira_linha):
    operacao = arquivo.readline()
    operacao = operacao.rstrip()
    operacao = operacao.strip('\n')
    conjunto_um  = arquivo.readline()
    conjunto_um = conjunto_um.rstrip()
    conjunto_um = conjunto_um.strip('\n')
    conjunto_dois = arquivo.readline()
    conjunto_dois = conjunto_dois.rstrip()
    conjunto_dois = conjunto_dois.strip('\n')
    conjunto_um = conjunto_um.split(', ')
    conjunto_dois = conjunto_dois.split(', ')
# Depois de cada leitura o dois conjuntos passam por um "if" para ver qual é o tipo de operação que deve ser
# feita e dentro deste "if" passam todas ou por um "if" dentro de um "for" no caso da união ou um "for" dentro
# de um "for" nos outros casos, para que as operações sejam resolvidas e transformadas em um novo conjunto resultante.
    if operacao == "U":
        listas = conjunto_um
        listas = listas + conjunto_dois
        uniao = []
        for a in listas:
            if a not in uniao:
                uniao.append(a)
        print ('União: Conjunto 1 {}, Conjunto 2 {}. Resultado: {} \n'.format(conjunto_um, conjunto_dois, uniao))


    if operacao == "I":
        intersecao = []
        for a in conjunto_um:
            for b in conjunto_dois:
                if a == b:
                    intersecao.append(a)
        print('Interseção: Conjunto 1 {}, Conjunto 2 {}. Resultado: {} \n'.format(conjunto_um, conjunto_dois, intersecao))

    if operacao == "D":
        diferenca = []
        for a in conjunto_um:
            # Criação de variavel auxiliar "achou" para identificar elementos iguais no primeiro e no segundo conjunto
            # para que esse elemento não faça parte do conjunto final.
            achou=0
            for b in conjunto_dois:
                if a == b:
                    achou=1
            if achou == 0:
                diferenca.append(a)
        print('Diferença: Conjunto 1 {}, Conjunto 2 {}. Resultado: {} \n'.format(conjunto_um, conjunto_dois, diferenca))

    if operacao == "C":
        lista = [[conjunto_um], [conjunto_dois]]
        print('Produto Cartesiano: Conjunto 1 {}, Conjunto 2 {}.'.format(conjunto_um, conjunto_dois), end = " ")
        print('Resultado: ', end = "")
        for x in conjunto_um:
            for y in conjunto_dois:
                print('({}, {});'.format(x,y), end = "")
        print('\n')


