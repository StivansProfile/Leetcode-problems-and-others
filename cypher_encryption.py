
# https://www.xarg.org/tools/caesar-cipher/

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def cypher_encryption_shift(string, shift_val):

    string_arr = list(string)

    if shift_val == 5 or shift_val > 5:
        for i in range(len(string_arr)):
            element_idx = alphabet.index(string_arr[i])
            string_arr[i] = alphabet[(element_idx + shift_val) % 26]
    else:
        for i in range(len(string_arr)):
            element_idx = alphabet.index(string_arr[i])
            string_arr[i] = alphabet[element_idx + shift_val]

    print(string_arr)


def cypher_decryption_shift(string, shift_val):

    string_arr = list(string)

    if shift_val == 5 or shift_val > 5:
         for i in range(len(string_arr)):
            element_idx = alphabet.index(string_arr[i])
            string_arr[i] = alphabet[(element_idx - shift_val) % 26]
    else:
        for i in range(len(string_arr)):
            element_idx = alphabet.index(string_arr[i])
            string_arr[i] = alphabet[element_idx - shift_val]

    print(string_arr)


cypher_encryption_shift("HELLOTHERE",10)
cypher_decryption_shift("ROVVYDROBO",10)