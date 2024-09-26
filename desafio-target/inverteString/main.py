import os

# Limpa o terminal a cada início de execução
def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    limpar_terminal()


    # Carrega em memória a string que queremos inverter
    string_desejada = input('Entre com a string a ser invertida: \n')

    # Inicializa uma string vazia
    string_invertida = ''

    # Percorre caracteres da string adicionando os de traz pra frente
    for char in string_desejada:
        string_invertida = char + string_invertida
    
    # Imprime a string invertida
    print(f'A string invertida fica assim `{string_invertida}`')

if __name__ == '__main__':
    main()