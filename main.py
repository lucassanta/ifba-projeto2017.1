#-*-coding:utf8;-*-
lista=""
produtos=[]
medicamentos=[]
funcionarios=[]
relatorios=[]
def menu_principal(lista):
    print("***** MENU PRINCIPAL *****")
    print("1 - Produtos Químicos")
    print("2 - Medicamentos")
    print("3 - Funcionários")
    print("4 - Relatórios")
    opcao=raw_input("Digite a opção desejada: ")
    if opcao=="1":
        lista='PRODUTO'
        menu_produto(lista)
    if opcao=="2":
        lista='MEDICAMENTO'
        menu_medicamento(lista)
    if opcao=="3":
        lista='FUNCIONARIO'
        menu_funcionario(lista)
    if opcao=="4":
        lista='RELATORIO'
        menu_relatorio(lista)
    menu_principal(lista)

def menu_produto(lista):
    print("***** PRODUTOS *****")
    menu_sec(lista)   
def menu_medicamento(lista):
    print("***** MEDICAMENTOS *****")
    menu_sec(lista)         
def menu_funcionario(lista):
    print("***** FUNCIONÁRIOS *****")
    menu_sec(lista)      
def menu_relatorio(lista):
    print("***** RELATÓRIOS *****")
    menu_sec(lista)    
def cadastro(lista):
    print '***** CADASTRAR - ',lista,' *****'
 
def busca(lista):
    print '***** BUSCAR - ',lista,' *****'

def atualiza(lista):
    print '***** ATUALIZAR - ',lista,' *****'
 
def remove(lista):
    print '***** REMOVER - ',lista,' *****'

def menu_sec(lista):
    print("1 - Cadastrar")
    print("2 - Buscar")
    print("3 - Atualizar")
    print("4 - Remover")
    opcao_s=raw_input("Digite a opção desejada: ")
    if opcao_s=="1":
        cadastro(lista)
    if opcao_s=="2":
        busca(lista)
    if opcao_s=="3":
        atualiza(lista)
    if opcao_s=="4":
        remove(lista)
    menu_sec(lista) 

menu_principal(lista)