# Coderbyte - Searching Challenge
# Autor: João Vitor
# Descrição:
# Encontra a substring palíndroma mais longa em uma string.
# Se nenhuma for maior que 2 caracteres, retorna "none".
# Depois concatena com o ChallengeToken e substitui cada 3ª letra por 'X'.

def SearchingChallenge(strParam):
    longest = ""

    # Percorre todas as substrings possíveis
    for i in range(len(strParam)):
        for j in range(i + 1, len(strParam) + 1):
            substr = strParam[i:j]
            # Verifica se é palíndromo
            if substr == substr[::-1]:
                # Se for maior que o anterior, atualiza
                if len(substr) > len(longest):
                    longest = substr

    # Se não houver palíndromo maior que 2 caracteres, retorna "none"
    if len(longest) <= 2:
        longest = "none"

    # Token fornecido no desafio
    token = "d4kn5rfbe"

    # Concatena o palíndromo com o token
    final_string = longest + token

    # Substitui cada 3º caractere por 'X'
    result = ""
    for i in range(len(final_string)):
        if (i + 1) % 3 == 0:
            result += "X"
        else:
            result += final_string[i]

    return result

# Entrada pelo terminal (padrão do Coderbyte)
print(SearchingChallenge(input()))
