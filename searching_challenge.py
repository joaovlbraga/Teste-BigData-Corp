"""
Coderbyte - Searching Challenge

Descrição:
Recebe uma string contendo palavras separadas por espaço e retorna a primeira palavra
que possui a maior quantidade de letras repetidas. Caso não exista, retorna '-1'.
Depois, concatena essa palavra com um ChallengeToken e substitui cada terceiro caractere da string final por 'X'.

Exemplos:
Input: "Hello apple pie"
Saída: HeXloX4kX5rXbe

Input: "No words"
Saída: -1X4kX5rXbe

ChallengeToken: d4kn5rfbe
"""

def SearchingChallenge(strParam):
    # Divide a string em palavras
    words = strParam.split()
    max_repeats = 0
    result_word = "-1"
    
    # Verifica qual palavra tem a maior quantidade de letras repetidas
    for word in words:
        counts = {}
        for char in word:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
        repeat_count = max(counts.values())
        if repeat_count > max_repeats and repeat_count > 1:
            max_repeats = repeat_count
            result_word = word

    # Concatena com o ChallengeToken
    final_output = result_word + "d4kn5rfbe"
    final_output_list = list(final_output)
    
    # Substitui cada terceiro caractere por 'X'
    for i in range(2, len(final_output_list), 3):
        final_output_list[i] = 'X'
        
    final_output = ''.join(final_output_list)
    return final_output

# Entrada da função
print(SearchingChallenge(input()))
