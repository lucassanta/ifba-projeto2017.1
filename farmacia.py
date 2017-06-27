# -*- coding: utf-8 -*- #
from datetime import date


Lista = []
continuar = True
p=True
# O cadastro/busca/atualizac~ao/remoc~ao de produtos qumicos
while continuar:
    opcao = input('O que você deseja? 1-Cadastrar, 2-Buscar, 3-Remover, 4-Atualizar, 5-Sair. ')
    if opcao == 1:
        nome = raw_input('Digite o nome do produto quimico: ')

        ano = input('digite o ano de validade: ')
        mes = input('digite o mês de validade:')
        dia = input('digite o dia de validade:')
        validade = date(ano, mes, dia)

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
            ano = input('digite o ano')
            mes = input('digite o mês')
            dia = input('digite o dia')
            buscaValidade = date(ano, mes, dia)
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
            buscaPreco = raw_input('Insira a preço/Kg a ser procurado.')
            for f in Lista:
                if f[4] == buscaPreco:
                    print f
    sim = ('Continuar? sim(S) Não(n)')
    if sim == 'S':
        continuar = False
    if opcao == 3:
        remocao = input('Deseja remover por: 1-Nome do produto, 2-Validade, 3-Estado, 4-Massa, 5-Preço do produto. ')
        if remocao is 1:
            remocaoNome = raw_input('Insira o nome a ser excluido.')
            for f in Lista:
                if f[0] == remocaoNome:
                    Lista.remove(f)
        if remocao is 2:
            ano = input('digite o ano')
            mes = input('digite o mês')
            dia = input('digite o dia')
            remocaoValidade = date(ano, mes, dia)
            for f in Lista:
                if f[1] == remocaoValidade:
                    Lista.remove(f)
        if remocao is 3:
            remocaoEstado = raw_input('Para remoção por Estado digite o estado.')
            for f in Lista:
                if f[2] == remocaoEstado:
                    Lista.remove(f)
        if remocao is 4:
            remocaoMassa = raw_input('Para remoção por massa digite a massa.')
            for f in Lista:
                if f[3] == remocaoMassa:
                    Lista.remove(f)
        if remocao is 5:
            remocaoPpM = raw_input('Para remoção por preço/massa digite a preço/massa.')
            for f in Lista:
                if f[3] == remocaoPpM:
                    Lista.remove(f)
    if opcao == 4:
            buscaNome= raw_input('Insira o Nome a ser procurado.')
            for f in Lista:
                if f[0] == buscaNome:
                    print f
                    Lista.remove(f)
                    print 'Agora os dados do determinado cadastro será atualizado manualmente.'
                    nome = raw_input('Digite o nome do produto quimico: ')

                    ano = input('digite o ano de validade')
                    mes = input('digite o mês de validade')
                    dia = input('digite o dia de validade')
                    validade = date(ano, mes, dia)

                    estado = raw_input('Digite o estado do produto (sólido, gasoso ou líquido: ')
                    massa = raw_input('Digite  a massa do produto (em Kg): ')
                    preco = raw_input('Digite o preço por grama: ')

                    Lista.append([nome, validade, estado, massa, preco])
                print Lista
    if opcao==5:
        print Lista
        continuar = False

# O cadastro/busca/atualizac~ao/remoc~ao de medicamentos
cont= True
Lista2= []
while cont:
    opcao = input('O que você deseja? 1-Cadastrar, 2-Buscar, 3-Remover, 4-Atualizar, 5-Sair ')
    if opcao == 1:
        n = raw_input('Digite o nome do medicamento: ')
        patv = raw_input('Digite  o principio ativo: ')
        concentrcao = raw_input('Digite a concentração: ')

        ano = input('digite o ano de validade')
        mes = input('digite o mês de validade')
        dia = input('digite o dia de validade')
        valido = date(ano, mes, dia)

        composicao = raw_input('Digite a composição: ')

        Lista2.append([n, patv, concentrcao, valido, composicao])
    if opcao == 2:
        busca = input('Buscar pelo: 1-Nome do medicamento, 2-principio ativo, 3-concentração, 4-validade, 5-composição. ')
        if busca is 1:
            buscaN = raw_input('Insira o nome do produto a ser procurado.')
            for f in Lista2:
                if f[0] == buscaN:
                    print f
        if busca is 2:
            buscaPa = raw_input('Insira para procurar por principio ativo:')
            for f in Lista2:
                if f[1] == buscaPa:
                    print f
        if busca is 3:
            buscaConcentracao = raw_input('Insira a concentração a ser procurado.')
            for f in Lista2:
                if f[2] == buscaConcentracao:
                    print f
        if busca is 4:
            ano = input('digite o ano de validade')
            mes = input('digite o mês de validade')
            dia = input('digite o dia de validade')
            busacValido = date(ano, mes, dia)
            for f in Lista2:
                if f[3] == busacValido:
                    print f
        if busca is 5:
            buscaPreco = raw_input('Insira a composição a ser procurada.')
            for f in Lista2:
                if f[4] == buscaPreco:
                    print f
    if opcao == 3:
        remocao = input('Deseja remover por: 1-Nome, 2-Principio Ativo, 3-concentração, 4-validade, 5-composição. ')
        if remocao is 1:
            remocaoNome = raw_input('Insira o nome a ser excluido.')
            for f in Lista2:
                if f[0] == remocaoNome:
                    Lista2.remove(f)
        if remocao is 2:
            remocaoValidade= raw_input('Para remoção por Principio Ativo digite-o.')
            for f in Lista2:
                if f[1] == remocaoValidade:
                    Lista2.remove(f)
        if remocao is 3:
            remocaoEstado = raw_input('Para remoção por concentração digite-a .')
            for f in Lista2:
                if f[2] == remocaoEstado:
                    Lista2.remove(f)
        if remocao is 4:
            ano = input('digite o ano de validade')
            mes = input('digite o mês de validade')
            dia = input('digite o dia de validade')
            remocaValido = date(ano, mes, dia)

            for f in Lista2:
                if f[3] == remocaValido:
                    Lista2.remove(f)
        if remocao is 5:
            remocaoPpM = raw_input('Para remoção por composição digite-o.')
            for f in Lista2:
                if f[3] == remocaoPpM:
                    Lista2.remove(f)
    if opcao == 4:
            buscaNome= raw_input('Insira o Nome a ser procurado.')
            for f in Lista2:
                if f[0] == buscaNome:
                    print f
                    Lista2.remove(f)
                    print 'Agora os dados do determinado cadastro será atualizado manualmente.'
                    n = raw_input('Digite o nome do medicamento: ')
                    patv = raw_input('Digite  o principio ativo: ')
                    concentrcao = raw_input('Digite a concentração: ')

                    ano = input('digite o ano de validade')
                    mes = input('digite o mês de validade')
                    dia = input('digite o dia de validade')
                    Valido = date(ano, mes, dia)

                    composicao = raw_input('Digite a composição: ')

                    Lista2.append([n, patv, concentrcao, Valido, composicao])
                print Lista2
    if opcao==5:
        print Lista2
        cont=False
#O cadastro/busca/atualizac~ao/remoc~ao de funcionarios
play=True
Lista3=[]
while play:
    opcao = input('O que você deseja? 1-Cadastrar, 2-Buscar, 3-Remover, 4-Atualizar, 5-Sair/relatorio.')
    if opcao == 1:
        n = raw_input('Digite o nome do funcionario: ')
        s = raw_input('Digite  o salario: ')
        area = raw_input('Digite a medicamento em que ele fabrica: ')

        Lista3.append([n, s, area])
    if opcao == 2:
        busca = input('Buscar pelo: 1-Nome do funcionario, 2-Salario, 3-medicamento em que ele fabrica. ')
        if busca is 1:
            buscaN = raw_input('Insira o nome a ser procurado.')
            for f in Lista3:
                if f[0] == buscaN:
                    print f
        if busca is 2:
            buscaSalario = raw_input('Insira para procurar por salario:')
            for f in Lista3:
                if f[1] == buscaSalario:
                    print f
        if busca is 3:
            buscaArea = raw_input('Para procurar o funcionario pelo medicamento em que ele fabrica, digite:')
            for f in Lista3:
                if f[2] == buscaArea:
                    print f
    if opcao == 3:
        remocao = input('Deseja remover por: 1-Nome, 2-Salario, 3-medicamento em que ele fabrica. ')
        if remocao is 1:
            remocaoNome = raw_input('Insira o nome a ser excluido.')
            for f in Lista3:
                if f[0] == remocaoNome:
                    Lista3.remove(f)
        if remocao is 2:
            remocaoSalario= raw_input('Para remoção por Salario digite-o.')
            for f in Lista3:
                if f[1] == remocaoSalario:
                    Lista3.remove(f)
        if remocao is 3:
            remocaoArea = raw_input('Para remoção por medicamento em que ele fabrica digite-o .')
            for f in Lista3:
                if f[2] == remocaoArea:
                    Lista3.remove(f)

    if opcao == 4:
            buscaNome= raw_input('Insira o nome do funcionario a ser procurado.')
            for f in Lista3:
                if f[0] == buscaNome:
                    print f
                    Lista3.remove(f)
                    print 'Agora os dados do determinado cadastro será atualizado manualmente.'
                    n = raw_input('Digite o nome: ')
                    s = raw_input('Digite  o salario: ')
                    area = raw_input('Digite a  medicamento em que ele fabrica: ')

                    Lista3.append([n, s, area])
                print Lista3
#Informa os produtos qumicos e medicamentos a vencerem nos proximos 10 dias
    if opcao == 5:
        hj = date.today()
        for f in Lista :
            prazo = f[1].toordinal() - hj.toordinal()
            if prazo <= 10:
                print 'o produto', f, 'vencerá nos proximos 10 dias'
        for a in Lista2:
            prazo2= a[3].toordinal() - hj.toordinal()
            if prazo2 <= 10:
                print 'o produto', a , 'vencerá nos proximos 10 dias'
                play = False


