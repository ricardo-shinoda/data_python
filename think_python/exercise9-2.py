def has_no_e(word):
    """
    Retorna True se a palavra não contém a letra 'e', caso contrário, retorna False.
    """
    return 'e' not in word


def words_without_e(words):
    """
    Imprime as palavras da lista que não contêm a letra 'e' e calcula a porcentagem de palavras sem 'e'.
    """
    count_without_e = 0
    total_words = len(words)

    for word in words:
        if has_no_e(word):
            print(word)
            count_without_e += 1

    percentage = (count_without_e / total_words) * 100
    print(f"Porcentagem de palavras sem 'e': {percentage:.2f}%")


# Example:
word_list = ["hello", "world", "python",
             "programming", "example", "without", "e"]
words_without_e(word_list)
