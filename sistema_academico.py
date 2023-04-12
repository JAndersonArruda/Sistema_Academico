''' Escreva um programa para manipular um sistema acadêmico. A estrutura desse programa pode ser baseada no exemplo da calculadora que fizemos durante 
a aula síncrona. O programa deve usar listas (ou dicionários) e funções para fazer todas as operações.

-- É obrigatório do uso de funções.

O programa deve apresentar um menu com as seguintes funcionalidades:

    a) Cadastrar: cadastra os alunos com matricula(int), nome (str), curso(str) e CRE [Coeficiente de Rendimento Escolar] (float). Dica: você pode salvar 
em um dicionário ou em uma lista bidimensional.
    b) Pesquisar: busca todos os dados do aluno e mostra o resultado. Essa função deve apresentar todas as informações do aluno encontrado; ou uma mensagem 
que "o aluno não foi encontrado". A pesquisa pode ser feita pela matricula do aluno, que é um valor que não se repete na lista (ou dicionário).
    c) Listar: apresenta todas as informações de todos os alunos que já estão cadastrados na lista (ou no dicionário).
    d) Atualizar: recebe um ou mais valores para atualizar os dados de algum aluno (a matrícula, pode ser usada para escolher o aluno a ser atualizado) da 
lista (ou do dicionário).
    e) Remover: recebe um valor como parâmetro (a matrícula, de preferência) e remove o aluno da lista (ou do dicionário).
    f) Encerrar: encerra a execução do programa.

-- As quesitos acima representarão um total de 6 funções que devem aparecer no código do programa. Caso desejem criar novas funcionalidade para gerar o 
diferencial nas respostas poderão fazer. Será bem interessante!'''


# Sistema Acadêmico
def sistema_academico():
    print('--**Sistema Acadêmico**--')
    print('1-Cadastrar')
    print('2-Pesquisar')
    print('3-Listar')
    print('4-Atualizar')
    print('5-Remover')
    print('6-Encerrar')

    opcao = int(input('Digite uma opção: '))
    return opcao


matricul = {}


def cadastrar():
    print('-->Opção de Cadastro:')
    matri = int(input('--->Número da Matricula: '))
    nom = input('--->Nome: ')
    cur = input('---Curso: ')
    coeficiente = float(input('--->Coeficiente de Rendimento Escolar: '))
    matricul[matri] = {'nome': nom, 'curso': cur, 'cre': coeficiente}
    return matricul[matri]


def pesquisar():
    print('-->Opção de Pesquisa:')
    proc = input('--->Número da matrícula: ')
    if proc in matricul:
        return matricul[proc]
    else:
        return None
    

def listar():
    print('-->Opção de Listaçao: ')
    return matricul


def atualizar():
    print('-->Opção de Atualização:')


def remover():
    print('-->Opção de Remoção:')
    remov = input('Número de matrícula: ')
    matricul.pop(int(remov))
    return remov


cond = True
while (cond):
    opcao = sistema_academico()
    if (opcao == 1):
        resultado = cadastrar()
        print(f'--->Aluno cadastrado')
    elif (opcao == 2):
        resultado = pesquisar()
        if resultado == None:
            print(f'--->O Aluno não foi encontrado!')
        else:
            print(f'--->Pesquisa: {resultado}')
    elif (opcao == 3):
        resultado = listar()
        print(f'--->Listação: {resultado}')
    elif (opcao == 4):
        resultado = atualizar()
        print(f'--->Atualizado.')
    elif (opcao == 5):
        resultado = remover()
        print(f'--->{resultado} removido.')
    elif (opcao == 6):
        cond = False
        print('--Você escolheu encerrar o programa--')
    else:
        print('--Opção Inválida--')
