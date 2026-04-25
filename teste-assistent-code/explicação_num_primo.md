# Explicação da Função `is_prime()` em Python

## O que é um Número Primo?

Um **número primo** é um número natural maior que 1 que possui exatamente dois divisores positivos distintos: 1 e ele mesmo. Exemplos incluem: 2, 3, 5, 7, 11, 13, 17, 19, 23, etc.

Números compostos (não primos) têm mais de dois divisores positivos.

## Estrutura da Função

```python
def is_prime(number: int) -> bool:
```

Esta função recebe um parâmetro `number` (inteiro) e retorna um valor booleano (`True` ou `False`). Utiliza anotações de tipo para maior clareza.

## Análise Passo a Passo

### 1. Validação de Entrada

```python
if not isinstance(number, int):
    raise TypeError("O argumento deve ser um inteiro.")
if number < 0:
    raise ValueError("O número deve ser não negativo.")
```

- **Princípio de Clean Code:** Sempre valide entradas para evitar comportamentos inesperados.
- Lança exceções apropriadas para tipos incorretos ou valores negativos.

### 2. Verificação Inicial (números menores que 2)

```python
if number < 2:
    return False
```

- Números menores que 2 (0, 1, e negativos) **não são primos** por definição.
- A função retorna imediatamente `False` para otimizar o desempenho.

### 3. Caso Especial: O número 2

```python
if number == 2:
    return True
```

- O número **2 é o único número primo par**.
- Todos os outros números pares serão descartados na próxima verificação.

### 4. Rejeição de Números Pares

```python
if number % 2 == 0:
    return False
```

- O operador `%` (módulo) retorna o resto da divisão.
- Se `number % 2 == 0`, o número é par e não é primo (exceto o 2, já tratado).
- Essa otimização evita verificações desnecessárias, reduzindo o tempo de execução pela metade.

### 5. Verificação de Divisibilidade (Otimização com Raiz Quadrada)

```python
max_divisor = int(math.sqrt(number)) + 1

for divisor in range(3, max_divisor, 2):
    if number % divisor == 0:
        return False
```

**Por que até a raiz quadrada?**

Se um número `n` tem um divisor maior que sua raiz quadrada, ele necessariamente tem um divisor menor que sua raiz quadrada. Portanto, basta verificar divisores até √n.

**Por que usar `range(3, max_divisor, 2)`?**

- Começamos em `3` (primeiro número ímpar a testar).
- Incrementamos de `2` em `2` para verificar apenas números ímpares.
- Isso reduz pela metade o número de iterações, tornando o algoritmo mais eficiente.

**Exemplo prático:** Para verificar se 29 é primo:
- √29 ≈ 5,4
- Verificamos divisores: 3 (29 % 3 ≠ 0), 5 (29 % 5 ≠ 0)
- Não há divisores até a raiz quadrada.
- Retorna `True` (29 é primo).

### 6. Retorno Final

```python
return True
```

Se nenhum divisor foi encontrado, o número é primo.

## Exemplos de Execução

| Número | Processo de Verificação | Resultado |
|--------|-------------------------|-----------|
| 2 | Caso especial: único primo par | ✓ Primo |
| 3 | Não divisível por 2 | ✓ Primo |
| 4 | Divisível por 2 | ✗ Não é primo |
| 17 | Verifica até √17 ≈ 4,1, sem divisores | ✓ Primo |
| 20 | Divisível por 2 | ✗ Não é primo |
| 97 | Verifica até √97 ≈ 9,8, sem divisores | ✓ Primo |
| 1 | Menor que 2 | ✗ Não é primo |
| 0 | Menor que 2 | ✗ Não é primo |

## Complexidade de Tempo

- **Melhor caso:** O(1) - números pares, menores que 2, ou 2
- **Pior caso:** O(√n) - onde n é o número testado
- **Comparação:** Muito mais eficiente que verificar todos os números até n (O(n))

## Vantagens do Algoritmo

- **Eficiência:** Complexidade O(√n) torna viável para números grandes
- **Simplicidade:** Código fácil de entender e manter
- **Robustez:** Validação de entrada previne erros
- **Legibilidade:** Comentários e estrutura clara seguem Clean Code

## Limitações

- Para números muito grandes (>10^12), algoritmos probabilísticos como Miller-Rabin são mais apropriados
- Não é otimizado para verificação em lote de muitos números

## Uso da Função

```python
# Importação
from verificar_primo import is_prime

# Testes simples
print(is_prime(17))   # True
print(is_prime(20))   # False
print(is_prime(97))   # True

# Tratamento de exceções
try:
    is_prime(-5)  # Levanta ValueError
except ValueError as e:
    print(f"Erro: {e}")

try:
    is_prime(3.14)  # Levanta TypeError
except TypeError as e:
    print(f"Erro: {e}")
```

## Executando o Script

Para executar os exemplos incluídos no módulo:

```bash
python verificar_primo.py
```

Saída esperada:
```
Verificação de números primos:
------------------------------
2 é primo
3 é primo
4 não é primo
5 é primo
10 não é primo
17 é primo
20 não é primo
29 é primo
100 não é primo
97 é primo
```

A função pode ser importada e reutilizada em outros programas Python, promovendo reutilização de código e modularidade.
