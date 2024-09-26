import os

# Limpa o terminal a cada início de execução
def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Verifica se o número testado esta presente na sequência de Fibonacci
def esta_em_fib(num):

    # Inicia variáveis com os valores iniciais da sequência
    fib1 = 0
    fib2 = 1

    # Laço de repetição que dura até o novo número da sequência ser maior que o número verificado
    while num > fib1:
        soma = fib1 + fib2
        fib1 = fib2
        fib2 = soma

        # Verifica se o número foi encontra e caso positivo imprime no console e retorna
        if num == fib1:
            print('O número testado pertence à sequência de Fibonacci!')
            return

    # Imprime no console que o número não foi encontrado    
    print('O número testado NÃO pertence à sequência de Fibonacci.')


def main():
    # Limpa o terminal
    limpar_terminal()

    # Apresenta o programa
    print("=== Bem-vindo ao programa **Está em Fibonacci** da Target ===")

    # Carrega o número escolhido para uma variável em memória
    num = int(input('Informe o número que deseja testar:'))

    # Verifica se o número testado esta presente na sequência de Fibonacci
    esta_em_fib(num)


if __name__ == '__main__':
    main()