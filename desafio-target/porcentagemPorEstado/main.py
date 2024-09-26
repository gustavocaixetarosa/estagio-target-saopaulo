import os
import json

# Limpa o terminal a cada início de execução
def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def importar_json(arquivo):
    try:
        valores = json.loads(arquivo) 
        return valores
    except json.JSONDecodeError:
        print('Erro ao decodificar JSON')


def main():

    limpar_terminal()
    
    valores_por_estado = '''
    [
        {"estado": "SP", "valor": "67836.43"},
        {"estado": "RJ", "valor": "36678.66"},
        {"estado": "MG", "valor": "29229.88"},
        {"estado": "ES", "valor": "27165.48"},
        {"estado": "Outros", "valor": "19849.53"}
    ]
    '''

    valores_em_dicionario = importar_json(valores_por_estado)
    valor_total = 0

    for estado in valores_em_dicionario:
        valor_total += float(estado['valor'])


    for estado in valores_em_dicionario:
        percentual_de_representacao = (float(estado['valor']) / valor_total) * 100  # Multiplicado por 100 para obter a porcentagem
        print(f'O estado {estado["estado"]} representa {percentual_de_representacao:.2f}% das vendas totais.')



if __name__ == '__main__':
    main()