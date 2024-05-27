import os

restaurantes = [
    {'nome': 'Bife sujo', 'categoria': 'prato-feito', 'ativo': True},
    {'nome': 'Saco de feijao', 'categoria': 'feijoada', 'ativo': False},
    {'nome': 'Pé de banha', 'categoria': 'pastelaria', 'ativo': True}
]

def finalizar_app():
    os.system("clear")
    os.system("cls")
    print("Finalizando o app\n")

def voltar_menu_principal():
    input("Digite uma tecla para voltar ao menu principal: ")
'''
Funçaõ para exibir o nome do programa
↓↓↓
'''
def mostrar_subtitulo(texto):
    '''
    ↑↑↑
    Função responsavel por exibir o subtitulo no codigo
    '''
    os.system("clear")
    linha = '*'*(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opcoes():
    '''
    ↑↑↑
    Função responsavel pela as esciolhas das opções para fazer algo no app
    '''

    mostrar_subtitulo("ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕠\n".ljust(20))
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Ativar restaurante")
    print("4 - Sair\n")

def opcao_invalida():
    '''
    ↑↑↑
    Função para quando acontecer um erro
    '''
    mostrar_subtitulo("Opção inválida\n".ljust(20))
    voltar_menu_principal()

def listarRestaurantes():
    '''
    ↑↑↑
    Opção para listar restaurante na tela após ser cadastrado
    '''
    mostrar_subtitulo('Listando os Restaurantes'.ljust(20))
    print("Nome:".ljust(20), "Categoria:".ljust(22), "Status:".ljust(24))
  
 
    for restaurante in restaurantes:
        
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante["ativo"] else "Desativado"
        print(f' {nome_restaurante.ljust(20)}  {categoria.ljust(22)}  {ativo}')

    
        
def alternar_estado_restaurante():
     '''
     ↑↑↑
     Esse trecho serve para alterar o estado do restaurante entre true or false
     '''
     mostrar_subtitulo("Alterando o estado do restaurante".ljust(20))

     nome_restaurante = input("Digite o nome do Restaurante que desejas alterar")
     restaurante_encontrado = False



     for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso'if restaurante['ativo']else f"O restaurante {nome_restaurante} foi desativado"
            print(mensagem)

     if not restaurante_encontrado:
        print("o restaurante não foi encontrado")
            
            
            

            

def chamar_nome_do_app():
    print("""ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕠""")





def cadastrar_novo_restaurante():
    #Docstring

    """
    ↑↑↑
    Essa função é responsavel por cadastrar um novo restaurante

    inputs:
    -nome do restaurante
    -categoria do restaurante

    outputs:
    -adiciona um novo restaurante ao dicionario,
    """

    nome_do_restaurante = input("Digite o nome do novo restaurante: ")
    categoria = input(f'Digite a categoria do restaurante{nome_do_restaurante}:')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"Você cadastrou o restaurante: {nome_do_restaurante}")

def main():
    '''
    ↑↑↑
    Essa função é responsavel por selecionar as funções de desejadas
    '''
    while True:
        try:
            escolher_opcoes()
            opcaodigitada = int(input("Digite a opção desejada: "))
            if opcaodigitada == 1:
                print("Você escolheu cadastrar restaurante\n" )
                cadastrar_novo_restaurante()
                main()
            elif opcaodigitada == 2:
                listarRestaurantes()
                voltar_menu_principal()
                main()
            elif opcaodigitada == 3:
                alternar_estado_restaurante()
                
            elif opcaodigitada == 4:
                print("Você escolheu sair do aplicativo\n")
                finalizar_app()
                '''
                ↑↑↑
                Essa função é responsavel por finalizar o app
                '''
                break
            else:
                opcao_invalida()
                main()
        except ValueError:
            print("Por favor, digite um número.")
            main()

if __name__ == "__main__":
    chamar_nome_do_app()
    main()