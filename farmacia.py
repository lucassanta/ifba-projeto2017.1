# -*- coding: utf-8 -*- #

Lista = []
continuar = True
cont = True

while continuar:
    opcao = input('O que você deseja? 1-Cadastrar, 2-Buscar, 3-Remover, 4-Atualizar. ')
    if opcao == 1:
        nome = raw_input('Digite o nome do produto quimico: ')
        validade = raw_input('Digite  a validade do produto: ')
        estado = raw_input('Digite o estado do produto (sólido, gasoso ou líquido: ')
        massa = raw_input('Digite  a massa do produto (em Kg): ')
        preco = raw_input('Digite o preço por grama: ')

        Lista.append([nome, validade, estado, massa, preco])

    if opcao == 2:
        busca = input('Buscar pelo: 1-Nome do produto, 2-Validade, 3-Estado, 4-Massa, 5-Preço do produto. ')
        if busca is 1:
            buscaNome = raw_input('Insira o nome do produto a ser procurado.')
            for f in Lista:
                if f[0] == buscaNome:
                    print f
        if busca is 2:
            buscaValidade = raw_input('Insira a validade a ser procurado.')
            for f in Lista:
                if f[1] == buscaValidade:
                    print f
        if busca is 3:
            buscaEstado = raw_input('Insira o Estado a ser procurado.')
            for f in Lista:
                if f[2] == buscaEstado:
                    print f
        if busca is 4:
            buscaMassa = raw_input('Insira a massa a ser procurada.')
            for f in Lista:
                if f[3] == buscaMassa:
                    print f
        if busca is 5:
            buscaPreco = raw_input('Insira a preço/Kg a ser procurada.')
            for f in Lista:
                if f[4] == buscaPreco:
                    print f
    if opcao == 3:
        remocao = input('Deseja remover por: 1-Nome do produto, 2-Validade, 3-Estado, 4-Massa, 5-Preço do produto. ')
        if remocao is 1:
            remocaomodelo = raw_input('Insira o nome a ser excluido.')
            for f in Lista:
                if f[0] == remocaomodelo:
                    Lista.remove(f)
        if remocao is 2:
            remocaoano = raw_input('Insira o Ano a ser excluido.')
            for f in Lista:
                if f[1] == remocaoano:
                    Lista.remove(f)
        if remocao is 3:
            remocaocor = raw_input('Insira a Cor a ser excluida.')
            for f in Lista:
                if f[2] == remocaocor:
                    Lista.remove(f)
        if remocao is 4:
            remocaopreco = raw_input('Insira o Preço a ser excluido.')
            for f in Lista:
                if f[3] == remocaopreco:
                    Lista.remove(f)