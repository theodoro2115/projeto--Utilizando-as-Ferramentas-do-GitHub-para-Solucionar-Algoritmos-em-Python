# algorithms.py

# 1. Cálculo de Fatorial
# O GitHub Copilot sugere automaticamente a implementação recursiva e iterativa
# ao digitar 'def factorial_'.

def factorial_recursive(n: int) -> int:
    """
    Calcula o fatorial de um número inteiro positivo de forma recursiva.
    """
    if n < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n: int) -> int:
    """
    Calcula o fatorial de um número inteiro positivo de forma iterativa.
    """
    if n < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 2. Verificação de Número Primo
# O Copilot sugere uma implementação otimizada (testando apenas até a raiz quadrada de n)
# ao digitar 'def is_prime'.

def is_prime(n: int) -> bool:
    """
    Verifica se um número inteiro positivo é primo.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# 3. Busca Binária
# O Copilot sugere a implementação clássica e eficiente da busca binária
# ao digitar 'def binary_search'.

def binary_search(arr: list, target: int) -> int:
    """
    Realiza uma busca binária em uma lista ordenada.
    Retorna o índice do alvo ou -1 se não for encontrado.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
