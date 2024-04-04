symbols = "QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"
every_n_symbols = 3
slip = 8


def decrypt(encrypted_text):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        if i % every_n_symbols == 0:
            if encrypted_text[i] in symbols:
                current_index = symbols.index(encrypted_text[i])
                new_index = (current_index - slip) % len(symbols)
                decrypted_text += symbols[new_index]
            else:
                decrypted_text += encrypted_text[i]
        else:
            decrypted_text += encrypted_text[i]
    return decrypted_text


if __name__ == "__main__":
    encrypted_text = input('Enter encrypted text here: ')
    decrypted_text = decrypt(encrypted_text)
    print(decrypted_text)
