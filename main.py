# main.py

from algorithms import factorial_recursive, factorial_iterative, is_prime, binary_search

def test_factorial():
    print("--- Teste de Fatorial ---")
    n = 5
    print(f"Fatorial de {n} (Recursivo): {factorial_recursive(n)}")
    print(f"Fatorial de {n} (Iterativo): {factorial_iterative(n)}")
    n = 7
    print(f"Fatorial de {n} (Recursivo): {factorial_recursive(n)}")
    print(f"Fatorial de {n} (Iterativo): {factorial_iterative(n)}")
    print("-" * 25)

def test_is_prime():
    print("--- Teste de Número Primo ---")
    numbers = [2, 13, 15, 29, 100]
    for n in numbers:
        print(f"O número {n} é primo? {is_prime(n)}")
    print("-" * 25)

def test_binary_search():
    print("--- Teste de Busca Binária ---")
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target1 = 23
    target2 = 42
    
    index1 = binary_search(arr, target1)
    print(f"Lista: {arr}")
    print(f"O alvo {target1} está no índice: {index1}")
    
    index2 = binary_search(arr, target2)
    print(f"O alvo {target2} está no índice: {index2}")
    print("-" * 25)

if __name__ == "__main__":
    test_factorial()
    test_is_prime()
    test_binary_search()
