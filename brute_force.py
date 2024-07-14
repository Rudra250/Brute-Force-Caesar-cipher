while(True):
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cipher_text = input("Enter the encrypted text: ")
    length = len(cipher_text)
    character_array = list(cipher_text)

    for key in range(26):
        print(f"Possible Plaintext {key}: ", end="")
        for j in range(length):
            if character_array[j] in chars:
                original_index = (chars.index(character_array[j]) + key) % 26
                print(chars[original_index], end="")
            else:
                print(character_array[j], end="")
        print()
    print()
