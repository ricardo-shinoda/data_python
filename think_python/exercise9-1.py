def main():
    # Abrir o arquivo words.txt para leitura
    with open('word.txt', 'r') as file:
        # Iterar sobre cada linha no arquivo
        for line in file:
            # Remover os espaços em branco extras no início e no final da linha
            word = line.strip()
            # Verificar se a palavra tem mais de 20 caracteres (sem contar whitespace)
            if len(word.replace(" ", "")) > 20:
                print(word)


if __name__ == "__main__":
    main()
