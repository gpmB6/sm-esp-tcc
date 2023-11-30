# main.py

# Funcao que abre um arquivo generico
def executa_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as arq:
            code = arq.read()
            exec(code)
    except Exception as e:
        print(f"Erro ao executar {arquivo}: {e}")

# Funcoes que abrem os arquivos especificos de cada item do menu
def opcao_1():
    executa_arquivo('smart.py')

def opcao_2():
    executa_arquivo('insere.py')

def opcao_3():
    executa_arquivo('consulta.py')
    
def exit():
  print('Saindo...')
  sys.exit()

# Opcoes do menu
opcoes_menu = [
    ("Executar o SmartMotors", opcao_1),
    ("Inserir manualmente um treinamento", opcao_2),
    ("Escolher um treinamento anterior", opcao_3),
    ("Sair\n", exit),
]

# Main loop
while True:
    print('\n')
    # Enumera as opcoes do menu, comecando em 1
    for opcao, (nome, _) in enumerate(opcoes_menu, start=1):
        print(f"{opcao}. {nome}")

    # Pega entrada do usuario
    user_input = int(input("Escolha uma opcao: "))

    # Condicao pra manter a ordem e validar se está dentro das quantidades existentes
    if 1 <= user_input <= len(opcoes_menu):
        opcoes_menu[user_input - 1][1]()
    else:
        print("Opcao invalida.")
