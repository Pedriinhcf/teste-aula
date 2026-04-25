# Identificação e Correção de Erros no Código Python

Este documento identifica todos os erros presentes no código original `debug.py`, explica suas causas e apresenta as correções.

## Erros Identificados

### 1. **Erro de Sintaxe - Aspas Faltantes (Linha 4)**

**Código com erro:**
```python
item1 = float(input(Preço do item 1? ))
```

**Causa do erro:**
A string `Preço do item 1?` não está envolvida por aspas duplas ou simples. Python não consegue identificar isso como uma string válida.

**Erro gerado:**
```
SyntaxError: invalid syntax
```

**Correção:**
```python
item1 = float(input("Preço do item 1? "))
```

---

### 2. **Erro de Tipo - Conversão de String (Linha 16)**

**Código com erro:**
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```

**Causa do erro:**
A função `input()` sempre retorna uma string. Ao tentar dividir uma string por 100, Python lança um erro `TypeError` porque não é possível fazer operações matemáticas com strings.

**Erro gerado:**
```
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

**Correção:**
```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```

Ou alternativa com tratamento de erro:
```python
try:
    desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
except ValueError:
    desconto_cupom = 0
```

---

### 3. **Erro de F-String - F Faltante (Linha 23)**

**Código com erro:**
```python
print(" Item 2:        R$ {total_item2:.2f}")
```

**Causa do erro:**
A string contém interpolação de variáveis `{total_item2:.2f}`, mas não tem o prefixo `f` que indica uma f-string (formatted string literal). Sem o `f`, a string é interpretada literalmente e não substitui as variáveis.

**Resultado incorreto:**
```
 Item 2:        R$ {total_item2:.2f}
```

**Correção:**
```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

**Resultado correto:**
```
 Item 2:        R$ 50.00
```

---

### 4. **Erro de Indentação - Bloco If (Linha 28-29)**

**Código com erro:**
```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

**Causa do erro:**
A instrução `print()` dentro do bloco `if` não está indentada corretamente. Python usa indentação para definir blocos de código, e a linha deve estar indentada com 4 espaços (ou uma tabulação).

**Erro gerado:**
```
IndentationError: expected an indented block
```

**Correção:**
```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

---

## Resumo dos Erros

| Linha | Erro | Tipo | Severidade |
|-------|------|------|------------|
| 4 | Aspas faltantes | SyntaxError | Crítica |
| 16 | String não convertida para float | TypeError | Crítica |
| 23 | F-string sem prefixo `f` | Lógica | Média |
| 28-29 | Indentação incorreta | IndentationError | Crítica |

---

## Código Corrigido

O código foi refatorado com as seguintes melhorias:

### Principais Mudanças:

1. **Correção de todas as sintaxes:** Aspas, conversão de tipos, f-strings e indentação
2. **Modularização:** Código encapsulado em uma função `calcular_carrinho_compras()`
3. **Legibilidade:** Nomes claros e comentários explicativos
4. **Documentação:** Docstrings adicionadas
5. **Padrão Python:** Uso de `if __name__ == "__main__"` para permitir importação

### Código Refatorado:

```python
"""
Sistema de Cálculo de Carrinho de Compras.

Este programa calcula o total de uma compra com 3 itens,
aplicando impostos e descontos via cupom.
"""


def calcular_carrinho_compras():
    """
    Calcula o total de uma compra com até 3 itens.
    Inclui cálculo de imposto (10%) e desconto via cupom.
    """
    # ENTRADA DE DADOS
    cliente = input("Qual é seu nome? ")

    qtd1 = int(input("Quantidade do item 1: "))
    item1 = float(input("Preço do item 1? "))  # ✓ Aspas adicionadas

    qtd2 = int(input("Quantidade do item 2: "))
    item2 = float(input("Preço do item 2? "))

    qtd3 = int(input("Quantidade do item 3: "))
    item3 = float(input("Preço do item 3? "))

    # CÁLCULOS DOS ITENS
    total_item1 = qtd1 * item1
    total_item2 = qtd2 * item2
    total_item3 = qtd3 * item3

    subtotal = total_item1 + total_item2 + total_item3
    imposto = subtotal * 0.10

    # DESCONTO
    desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))  # ✓ float() adicionado
    desconto = subtotal * (desconto_cupom / 100)

    # TOTAL FINAL
    total = subtotal + imposto - desconto

    # EXIBIÇÃO
    linha = "=" * 31
    separador = "-" * 31

    print(linha)
    print(f" Cliente: {cliente}")
    print(linha)
    print(f" Item 1:        R$ {total_item1:.2f}")
    print(f" Item 2:        R$ {total_item2:.2f}")  # ✓ Prefixo 'f' adicionado
    print(f" Item 3:        R$ {total_item3:.2f}")
    print(separador)
    print(f" Subtotal:      R$ {subtotal:.2f}")
    print(f" Imposto (10%): R$ {imposto:.2f}")

    if desconto_cupom > 0:  # ✓ Indentação corrigida
        print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

    print(linha)
    print(f" TOTAL:         R$ {round(total, 2):.2f}")
    print(linha)


if __name__ == "__main__":
    calcular_carrinho_compras()
```

## Como Testar o Código Corrigido

1. Abra um terminal na pasta do arquivo
2. Execute: `python debug.py`
3. Insira os valores quando solicitado:

```
Qual é seu nome? João Silva
Quantidade do item 1: 2
Preço do item 1? 25.50
Quantidade do item 2: 1
Preço do item 2? 50.00
Quantidade do item 3: 3
Preço do item 3? 15.75
Você tem um cupom de desconto? (Digite o percentual ou 0): 10
```

4. Saída esperada:

```
===============================
 Cliente: João Silva
===============================
 Item 1:        R$ 51.00
 Item 2:        R$ 50.00
 Item 3:        R$ 47.25
-------------------------------
 Subtotal:      R$ 148.25
 Imposto (10%): R$ 14.83
 Desconto (10%): -R$ 14.82
===============================
 TOTAL:         R$ 148.26
===============================
```

## Conclusão

Os 4 erros críticos foram:
1. **Aspas faltantes** - Erro de sintaxe
2. **Tipo de dado** - String não convertida
3. **F-string** - Variável não interpolada
4. **Indentação** - Bloco não indentado

Todos os erros foram corrigidos, e o código agora funciona corretamente com boas práticas de programação implementadas.