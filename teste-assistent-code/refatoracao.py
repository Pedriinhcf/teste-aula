"""
Módulo para cálculo de estatísticas básicas de uma lista de números.

Este módulo contém funções para calcular soma, média, maior e menor valor
de uma lista de números, seguindo os princípios de Clean Code.
"""


def calcular_estatisticas(numeros):
    """
    Calcula estatísticas básicas de uma lista de números.

    Args:
        numeros (list): Lista de números (int ou float) não vazia.

    Returns:
        tuple: (soma_total, media, maior_valor, menor_valor)

    Raises:
        TypeError: Se a entrada não for uma lista.
        ValueError: Se a lista estiver vazia.

    Examples:
        >>> calcular_estatisticas([1, 2, 3, 4, 5])
        (15, 3.0, 5, 1)
    """
    # Validação de entrada
    if not isinstance(numeros, list):
        raise TypeError("A entrada deve ser uma lista de números.")
    if len(numeros) == 0:
        raise ValueError("A lista não pode estar vazia.")

    # Inicialização das variáveis
    soma_total = 0
    maior_valor = menor_valor = numeros[0]

    # Loop único para calcular soma, máximo e mínimo
    for numero in numeros:
        soma_total += numero
        if numero > maior_valor:
            maior_valor = numero
        if numero < menor_valor:
            menor_valor = numero

    # Cálculo da média
    media = soma_total / len(numeros)

    return soma_total, media, maior_valor, menor_valor


def main():
    """
    Função principal para demonstrar o uso da função calcular_estatisticas.
    """
    # Lista de exemplo
    lista_exemplo = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

    # Cálculo das estatísticas
    soma_total, media, maior_valor, menor_valor = calcular_estatisticas(lista_exemplo)

    # Exibição dos resultados
    print("Estatísticas da lista:")
    print(f"Lista: {lista_exemplo}")
    print(f"Total (soma): {soma_total}")
    print(f"Média: {media}")
    print(f"Maior valor: {maior_valor}")
    print(f"Menor valor: {menor_valor}")


if __name__ == "__main__":
    main()