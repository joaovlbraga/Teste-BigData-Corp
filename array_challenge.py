"""
Desafio: Array Challenge - Coderbyte

Descrição:
Recebe um array de números e verifica se qualquer combinação dos números
(exceto o maior número) pode somar exatamente o valor do maior número.
Se sim, retorna "true". Caso contrário, retorna "false".
"""

from itertools import combinations

def ArrayChallenge(arr):
    # Pega o maior número do array
    largest = max(arr)
    # Remove ele da lista
    arr.remove(largest)

    # Verifica todas as combinações possíveis
    for i in range(1, len(arr)+1):
        for combo in combinations(arr, i):
            if sum(combo) == largest:
                return "true"
    
    return "false"

# Exemplo de execução manual
if __name__ == "__main__":
    # Entrada pelo usuário no formato de string de lista
    user_input = input("Digite os números separados por vírgula (ex: 5,7,16,1,2): ")
    # Converte string em lista de inteiros
    arr = list(map(int, user_input.strip("[]").split(",")))

    # Chama a função e imprime o resultado
    print(ArrayChallenge(arr))
