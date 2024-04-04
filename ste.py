symbols = "QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"
every_n_symbols = 3
slip = 8


if __name__ == "__main__":
    source_text = input('Enter text here: ')
    encrypted_text = ""
    for i in range(len(source_text)):
        if i % every_n_symbols == 0:
            if source_text[i] in symbols:
                current_index = symbols.index(source_text[i])
                new_index = (current_index + slip) % len(symbols)
                encrypted_text += symbols[new_index]
            else:
                encrypted_text += source_text[i]
        else:
            encrypted_text += source_text[i]

    print(encrypted_text)