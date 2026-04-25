"""
Módulo para verificação de números primos.

Este módulo contém funções para determinar se um número é primo,
seguindo os princípios de Clean Code: legibilidade, simplicidade e eficiência.
"""

import math


def is_prime(number: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Um número primo é um número natural maior que 1 que possui
    exatamente dois divisores positivos: 1 e ele mesmo.

    Args:
        number (int): O número a ser verificado. Deve ser um inteiro não negativo.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Raises:
        TypeError: Se o argumento não for um inteiro.
        ValueError: Se o número for negativo.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
    """
    # Validação de entrada
    if not isinstance(number, int):
        raise TypeError("O argumento deve ser um inteiro.")
    if number < 0:
        raise ValueError("O número deve ser não negativo.")

    # Casos base: números menores que 2 não são primos
    if number < 2:
        return False

    # 2 é o único número primo par
    if number == 2:
        return True

    # Números pares maiores que 2 não são primos
    if number % 2 == 0:
        return False

    # Verifica divisibilidade por números ímpares até a raiz quadrada
    # Usamos math.sqrt para maior clareza, embora i*i <= number seja equivalente
    max_divisor = int(math.sqrt(number)) + 1

    for divisor in range(3, max_divisor, 2):
        if number % divisor == 0:
            return False

    return True


def main():
    """
    Função principal para demonstrar o uso da função is_prime.
    """
    test_numbers = [2, 3, 4, 5, 10, 17, 20, 29, 100, 97]

    print("Verificação de números primos:")
    print("-" * 30)

    for num in test_numbers:
        result = is_prime(num)
        status = "é primo" if result else "não é primo"
        print(f"{num} {status}")


if __name__ == "__main__":
    main()
