import json
import os

# Limpa o terminal a cada início de execução
def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Função que carrega o arquivo json para dicionário em memória
def importar_json(arquivo):
    try:
        with open(arquivo, 'r') as arquivoCarregado:
            json_vendas = json.load(arquivoCarregado)

        return json_vendas
    except FileNotFoundError:
        print('Arquivo não encontrado')
    
# Função que encontra o menor valor em um dicionario do tipo ('dia' : 'valor')    
def menor_valor(lista_vendas):

    valor = float('inf')

    for venda in lista_vendas:
        if venda['valor'] == 0:
            continue
        if venda['valor'] < valor:
            valor = venda['valor']
    return valor

# Função que encontra o maior valor em um dicionario do tipo ('dia' : 'valor')    
def maior_valor(lista_vendas):

    valor = 0

    for venda in lista_vendas:

        if venda['valor'] == 0:
            continue
        
        if venda['valor'] > valor:
            valor = venda['valor']
    return valor

# Função que calcula quantidade de dias que o faturamento superou o media
def dias_acima_da_media(lista_vendas):

    soma_total_de_vendas = 0
    dias_de_venda = 0
    dias_vendido_acima_da_media = 0

    for venda in lista_vendas:

        if venda['valor'] > 0:
            dias_de_venda += 1
            soma_total_de_vendas += venda['valor']

    media_venda_diaria = soma_total_de_vendas / dias_de_venda

    print(f'venda media mensal: {media_venda_diaria}')

    for venda in lista_vendas:
        if venda['valor'] > media_venda_diaria:
            dias_vendido_acima_da_media += 1

    return dias_vendido_acima_da_media

def main():
    # Carrega o arquivo json em memória
    caminho_do_arquivo = 'dados.json'
    json_vendas = importar_json(caminho_do_arquivo)
    
    # Aloca menor venda para variavel e imprime no console
    menor_venda = menor_valor(json_vendas)
    print(f'O menor valor de venda diária foi de ${menor_venda}')


    # Aloca maior venda para variavel e imprime no console
    maior_venda = maior_valor(json_vendas)
    print(f'O maior valor de venda diária foi de ${maior_venda}')
    
    # Aloca quantidade de dias de faturamento acima da média em variável e a imprime no console
    dias_acima = dias_acima_da_media(json_vendas)
    print(f'O valor de faturamento diário foi acima da média {dias_acima} dias.')

if __name__ == '__main__':
    main()