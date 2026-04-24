# Explicação da Função `eh_primo()` em Python

## O que é um Número Primo?

Um **número primo** é um número natural maior que 1 que possui exatamente dois divisores: 1 e ele mesmo. Exemplos: 2, 3, 5, 7, 11, 13...

## Estrutura da Função

```python
def eh_primo(numero):
```

Essa função recebe um parâmetro `numero` (inteiro) e retorna um valor booleano (`True` ou `False`).

## Análise Passo a Passo

### 1. Verificação Inicial (números menores que 2)

```python
if numero < 2:
    return False
```

- Números menores que 2 (0, 1, e negativos) **não são primos** por definição
- A função retorna imediatamente `False`

### 2. Caso Especial: O número 2

```python
if numero == 2:
    return True
```

- O número **2 é o único número primo par**
- Todos os outros números pares serão descartados na próxima verificação

### 3. Rejeição de Números Pares

```python
if numero % 2 == 0:
    return False
```

- O operador `%` (módulo) retorna o resto da divisão
- Se `numero % 2 == 0`, o número é par e não é primo (exceto o 2, já tratado)
- Essa otimização evita verificações desnecessárias

### 4. Verificação de Divisibilidade (Otimização com Raiz Quadrada)

```python
i = 3
while i * i <= numero:
    if numero % i == 0:
        return False
    i += 2
```

**Por que até a raiz quadrada?**

Se um número `n` tem um divisor maior que sua raiz quadrada, ele também deve ter um divisor menor que sua raiz quadrada. Portanto, basta verificar até √n.

**Por que incrementar de 2 em 2?**

- Começamos em `i = 3` (primeiro número ímpar a testar)
- Incrementamos `i += 2` para verificar apenas números ímpares
- Isso reduz pela metade o número de iterações

**Exemplo:** Para verificar se 29 é primo:
- √29 ≈ 5,4
- Verificamos: 3 (29 % 3 ≠ 0), 5 (29 % 5 ≠ 0)
- Não há mais divisores até a raiz quadrada
- Retorna `True` (29 é primo)

### 5. Retorno Final

```python
return True
```

Se nenhuma divisão foi encontrada, o número é primo.

## Exemplos de Execução

| Número | Explicação | Resultado |
|--------|-----------|-----------|
| 2 | Único primo par | ✓ Primo |
| 3 | Não divisível por 2 | ✓ Primo |
| 4 | Divisível por 2 | ✗ Não é primo |
| 17 | Verifica até √17 ≈ 4,1, sem divisores | ✓ Primo |
| 20 | Divisível por 2 | ✗ Não é primo |
| 97 | Verifica até √97 ≈ 9,8, sem divisores | ✓ Primo |

## Complexidade de Tempo

- **Melhor caso:** O(1) - números pares ou menores que 2
- **Pior caso:** O(√n) - onde n é o número testado
- Muito mais eficiente que verificar todos os números até n!

## Uso da Função

```python
# Testando a função
print(eh_primo(17))   # True
print(eh_primo(20))   # False
print(eh_primo(97))   # True
```

A função pode ser importada e reutilizada em outros programas Python.
